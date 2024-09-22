from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Property, Investment
from .forms import PropertyForm


def home(request):
    featured_properties = Property.objects.filter(is_available=True).order_by('-date_added')[:3]
    return render(request, 'main/home.html', {
        'featured_properties': featured_properties
    })



def property_list(request):
    properties = Property.objects.filter(is_available=True)
    
    sort_by = request.GET.get('sort', 'date_added')
    if sort_by == 'price':
        properties = properties.order_by('price')
    elif sort_by == 'rooms':
        properties = properties.order_by('num_rooms')
    elif sort_by == 'return':
        properties = properties.order_by('-average_annual_return')
    else:
        properties = properties.order_by('-date_added')
    
    # Filtering by additional parameters
    min_price = request.GET.get('price_min')
    max_price = request.GET.get('price_max')
    num_rooms = request.GET.get('num_rooms')
    min_return = request.GET.get('average_annual_return')

    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    if num_rooms:
        properties = properties.filter(num_rooms=num_rooms)
    if min_return:
        properties = properties.filter(average_annual_return__gte=min_return)

    return render(request, 'main/property_list.html', {
        'properties': properties
    })



def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'main/property_detail.html', {
        'property': property
    })



#@login_required
def investments(request):
    user_investments = Investment.objects.filter(user=request.user, is_active=True)
    return render(request, 'main/investments.html', {
        'investments': user_investments
    })


def login_view(request):
    login(request)
    return render(request,'main/login.html', {})




def logout_view(request):
    logout(request)
    return redirect('home')


#def register_view(request):
 #   if request.method == 'POST':
  #      form = UserCreationForm(request.POST)
   #     if form.is_valid():
    #        user = form.save()
     #       login(request, user)  # Automatically log in the user after registration
      #      return redirect('home')  # Redirect to the home page after registration
    #else:
     #   form = UserCreationForm()

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'main/add_property.html', {'form': form})