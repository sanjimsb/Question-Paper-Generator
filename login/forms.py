from django import forms
from . models import login_forms

class login_forms(forms.Form):
	username = forms.CharField(widget=InputField(
		attrs={
	'class':'prestine',
	'placeholder':'Username',

	}
		))
	password = forms.CharField()
