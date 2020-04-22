from django import forms
from . models import question_details
from . choices import *

class question_details_form(forms.Form):
	question = forms.CharField()
	subject = forms.CharField()
	level = forms.IntegerField()
	group = forms.ChoiceField(choices = group_choice)
	question_weight = forms.ChoiceField(choices = question_marks_choice)
	question_type = forms.ChoiceField(choices = question_type_choice)
	
	def clean_message(self):
		sub = self.cleaned_data.get("subject")
		if sub == '':
			raise forms.ValidationError("the field is required")

		return username

	class Meta:
		model = question_details
		fields = ("question_id","question","subject","level","group","question_weight","question_type")
