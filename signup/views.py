# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from . forms import admin_signup_form
# from . hash import hash_this
# Create your views here.

class signup(TemplateView):
	template_name = 'signup/index.html'

	def get(self,request,*args,**kwargs):
		form = admin_signup_form()
		return render(request,self.template_name,{'form':form})

	def post(self,request,*args,**kwargs):
		form = admin_signup_form(request.POST)
		if form.is_valid():
			if 'login' in request.POST:	
				form.save()
				username = form.cleaned_data.get('username')
				return redirect('login')
				# username = form.cleaned_data['username']
				# password = form.cleaned_data['password1']
				# re_password = form.cleaned_data['password2']
				# institute_name = form.cleaned_data['institute_name']
				# address = form.cleaned_data['address']
				# if(password == re_password):
				# 	hashed_password = hash_this(password)
				# 	login_information = {
				# 		'username':username,
				# 		'password':hashed_password,
				# 		# 'institute_name':institute_name,
				# 		# 'address':address
				# 	}
				# 	admin_signup.objects.create(**login_information)
		return render(request,self.template_name,{'form':form})