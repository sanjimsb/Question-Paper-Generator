from django import forms
# from .models import admin_signup
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class admin_signup_form(UserCreationForm):
	# password1 = forms.CharField(widget=forms.PasswordInput(
	# attrs={
	# 'placeholder':'********',

	# }))
	# password2 = forms.CharField(widget=forms.PasswordInput(
	# attrs={
	# 'placeholder':'********',

	# }))
	email = forms.EmailField(widget=forms.TextInput(
	attrs={
	'placeholder':'Email',
	}
	))
	# address = forms.CharField(widget=forms.TextInput(
	# attrs={
	# 'class':'form-control',
	# 'placeholder':'Address',

	# }
	# ))

	class Meta:
		model = User
		fields= ("username","password1","password2","email")

