# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from signup.models import admin_signup
from . forms import login_forms
from signup.hash import check_hash
# Create your views here.

class login(TemplateView):
	template_name = 'login/index.html'

	def get(self,request,*args,**kwargs):
		form = login_forms()
		return render(request,self.template_name,{'form':form})

	def post(self,request,*args,**kwargs):
		form = login_forms(request.POST)
		# if form.is_valid():
		# 		username = form.cleaned_data['username']
		# 		password = form.cleaned_data['password']
		# 		request.session['un'] = username
		# 		a = admin_signup.objects.filter(user_name=request.POST['username'])
		# 		pwd = a[0].password 
		# 		if check_hash(password,pwd):
		# 			return redirect('/add_question_paper/')
		# 		else:
		# 			print('failed')
		return render(request,self.template_name,{'form':form})


	
