# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from . forms import question_details_form
from . models import question_details
from django.core.exceptions import ValidationError
import json
# Create your views here.


class add_question_main(TemplateView):
	template_name = 'add_question_paper/index.html'

	def get_no_txt(self):
		return self.request.GET.get('num')

	def get(self,request,*args,**kwargs):
		form = question_details_form()
		return render(request,self.template_name,{'form':form})


	def post(self,request,*args,**kwargs):
		if request.method == 'POST':
			form = question_details_form(request.POST)
			if 'add' in request.POST:
				form = question_details_form()
				a = self.get_no_txt()
				sub = request.POST['subject']
				level = request.POST['level']
				errors = []
				errors_c = []
				if sub == '':
					errors.append('this field must be filled')
					return render(request,self.template_name,{'errors':errors,'level':level})
				if level == '':
					errors_c.append('class field must be filled')
					return render(request,self.template_name,{'errors_c':errors_c,'level':level})


				b = int(a)
				for x in range(1, b + 1):					
					subject = request.POST['subject']
					level = request.POST['level']
					group = request.POST['group']
					question_weight = request.POST['question_weight']
					question_type = request.POST['question_type']
					question = request.POST['textarea%d' % x]
					data = {
					'question':question,
					'level':level,
					'subject':subject,
					'group':group,
					'question_weight':question_weight,
					'question_type':question_type

					}
					question_details.objects.create(**data)
		else:
			print('fail')
			
		return render(request,self.template_name,{'form':form})

	def validation_errors(self,request):
		sub = request.GET.get('subject')
		print sub 
		return None

# def start(request,*args,**kwargs):
# 	form = question_details_form()
# 	if request.method == 'GET':
# 		no_txt = request.GET.get('num')
# 		print no_txt
		
# 	else:
# 		form = question_details_form(request.POST)
# 		if 'add' in request.POST:
# 			print no_txt

# 	return render(request,'add_question_paper/index.html',{'form':form})
