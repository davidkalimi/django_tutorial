
from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Home page view function
    path('properties/', views.property_list, name='property_list'),  # List of properties
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),  # Property details
    path('investments/', views.investments, name='investments'),  # User investments
    #path('invest/<int:property_id>/', views.invest, name='invest'),  # Investing in a property
    path('add_property/', views.add_property, name='add_property'),  # Add new property

    # Redirect root URL to home page
    path('', RedirectView.as_view(url='/home/', permanent=False)),
]


