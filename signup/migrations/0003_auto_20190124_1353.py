# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-24 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20190122_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin_signup',
            old_name='password',
            new_name='password1',
        ),
        migrations.RemoveField(
            model_name='admin_signup',
            name='user_name',
        ),
        migrations.AddField(
            model_name='admin_signup',
            name='password2',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='admin_signup',
            name='username',
            field=models.CharField(default='', max_length=150),
        ),
    ]
