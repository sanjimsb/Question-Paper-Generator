# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class login_details(models.Model):
	username = models.CharField(max_length=100,default='')
	password =models.CharField(max_length=50,default='')


	def __str__(self):
		return self.username