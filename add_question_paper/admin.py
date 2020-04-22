# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . models import question_details
from django.contrib import admin


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('question_id','question', 'subject', 'level', 'group', 'question_weight', 'question_type')
	# list_display = ('user', 'user_info')

	def group(self, obj):
		return obj.group



# Register your models here.
admin.site.register(question_details, UserProfileAdmin)