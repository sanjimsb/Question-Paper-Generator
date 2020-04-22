from django import forms
from . choices import *
from . models import generate_options

class generate_q(forms.Form):
	institute_name			=	forms.CharField(widget=forms.TextInput(
		attrs={
		'placeholder':'Institute name',
		'class':'form-control',

		}))
	Subject						=	forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',

		}))
	Level 						=	forms.ChoiceField(choices = level_choice,widget=forms.Select(
		attrs={
		'class':'form-control',

	}))
	Group_A_questions			=	forms.ChoiceField(choices = group_a_choice,widget=forms.Select(
		attrs={
		'class':'form-control',

		}))	
	Group_A_required_questions	=	forms.ChoiceField(choices = group_a_cq,widget=forms.Select(
		attrs={
		'class':'form-control',

		}))
	group_b_questions			=	forms.ChoiceField(choices = group_b_choice,widget=forms.Select(
		attrs={
		'class':'form-control',

		}))	
	group_b_required_questions	=	forms.ChoiceField(choices = group_b_cq,widget=forms.Select(
		attrs={
		'class':'form-control',

		}))
	group_c_questions			=	forms.ChoiceField(choices = group_c_choice,widget=forms.Select(
		attrs={
		'class':'form-control',

		}))
	group_c_required_questions	=	forms.ChoiceField(choices = group_c_cq,widget=forms.Select(
		attrs={
		'class':'form-control',

		}))	


	class Meta:
		model   =	generate_options
		fields  =	("institute_name","subject","level","group_a_question","group_a_cq","group_b_question","group_b_qc","group_c_question","group_c_qc") 












