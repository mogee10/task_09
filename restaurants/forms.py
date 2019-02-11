from django import forms
from .models import Restaurant
from django.contrib.auth import login

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }
class SignupForm(forms.ModelForm):
	class Meta:
		model = user
		fields =['username', 'email', 'password']

		widgets = {"password": forms.PasswordInput()

		}

class SigninForm(forms.ModelForm):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())
