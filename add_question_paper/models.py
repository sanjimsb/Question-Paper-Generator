# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . choices import *
from django.db import models

# Create your models here.



class question_details(models.Model):
	question_id = models.AutoField(primary_key=True)
	question = models.CharField(max_length=1000,default='')
	subject = models.CharField(max_length=1000,default='')
	level = models.IntegerField(default='')
	group = models.CharField(choices = group_choice,max_length = 30,default='')
	question_weight = models.CharField(choices = question_marks_choice,max_length = 30,default='')
	question_type = models.CharField(choices = question_type_choice,max_length = 30,default='')

	def __str__(self):
		return  self.question + ' - ' + self.subject