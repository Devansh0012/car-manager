from django import forms
from .models import Car
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'color', 'photo']
        labels = {
            'make': 'Make',
            'model': 'Model',
            'year': 'Year',
            'color': 'Color',
            'photo': 'Photo'
        }
        help_texts = {
            'make': 'Enter the make of the car',
            'model': 'Enter the model of the car',
            'year': 'Enter the year of the car',
            'color': 'Enter the color of the car',
            'photo': 'Upload a photo of the car'
        }
        error_messages = {
            'make': {
                'required': 'This field is required'
            }
        }
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        