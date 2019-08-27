from django import forms
from django.contrib.auth.models import User
from .models import Restaurant

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
		model = User
		fields = ['username','first_name','email','password']

		widgets = {
			'password': forms.PasswordInput()
		}

class SigninForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(widget=forms.PasswordInput(), required=True)