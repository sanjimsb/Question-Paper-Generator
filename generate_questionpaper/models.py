# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . choices import *
from django.db import models

# Create your models here.



class generate_options(models.Model):
	institute_name = models.CharField(max_length=1000,default='')
	subject = models.CharField(max_length=1000,default='')
	level = models.IntegerField(choices = level_choice,default='')
	group_a_question = models.IntegerField(choices = group_a_choice,default='')
	group_a_cq = models.IntegerField(choices = group_a_cq,default='')
	group_b_question = models.IntegerField(choices = group_b_choice,default='')
	group_b_qc = models.IntegerField(choices = group_b_cq,default='')
	group_c_question = models.IntegerField(choices = group_c_choice,default='')
	group_c_qc = models.IntegerField(choices = group_c_cq,default='')

	
	def __str__(self):
		return self.question + ' - ' + self.subject