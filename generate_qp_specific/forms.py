from django import forms
from add_question_paper.models import question_details

class g_qp_specific(forms.Form):
	Institute_Name			=	forms.CharField(widget=forms.TextInput(
		attrs={
		'placeholder':'Institute name',
		'class':'form-control',

		}))

	Choose_term			=	forms.CharField(widget=forms.TextInput(
			attrs={
			'placeholder':'Institute name',
			'class':'form-control',

			}))

	Class			=	forms.CharField(widget=forms.TextInput(
			attrs={
			'placeholder':'Institute name',
			'class':'form-control',

			}))

	Exam_Time			=	forms.CharField(widget=forms.TextInput(
			attrs={
			'placeholder':'Institute name',
			'class':'form-control',

			}))

	Subject			=	forms.CharField(widget=forms.TextInput(
			attrs={
			'placeholder':'Institute name',
			'class':'form-control',

			}))
	Group_A_questions			=	forms.CharField(widget=forms.TextInput(
			attrs={
			'placeholder':'Institute name',
			'class':'form-control',

			}))
	Group_A_compulsory_questions			=	forms.CharField(widget=forms.TextInput(
			attrs={
			'placeholder':'Institute name',
			'class':'form-control',

			}))
	Group_B_questions			=	forms.CharField(widget=forms.TextInput(
			attrs={
			'placeholder':'Institute name',
			'class':'form-control',

			}))
	Group_B_compulsory_questions			=	forms.CharField(widget=forms.TextInput(
			attrs={
			'placeholder':'Institute name',
			'class':'form-control',

			}))
	Group_C_questions			=	forms.CharField(widget=forms.TextInput(
			attrs={
			'placeholder':'Institute name',
			'class':'form-control',

			}))
	Group_C_compulsory_questions			=	forms.CharField(widget=forms.TextInput(
			attrs={
			'placeholder':'Institute name',
			'class':'form-control',

			}))



		