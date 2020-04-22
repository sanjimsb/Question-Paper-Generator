# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class admin_signup(models.Model):
	username = models.CharField(max_length=150,default='')
	password1 = models.CharField(max_length=30,default='')
	password2 = models.CharField(max_length=30,default='')
	institute_name = models.CharField(max_length=30,default='')
	address = models.CharField(max_length=500,default='')

	def __str__(self):
		return self.username + ' - ' + self.password1
	