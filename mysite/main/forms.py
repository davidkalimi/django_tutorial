
from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'title', 'location', 'price', 'description', 'square_meters', 
            'num_rooms', 'is_available','image','owner'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'is_available': forms.CheckboxInput(),
        }
