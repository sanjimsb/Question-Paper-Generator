# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-22 06:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='admin_login',
            new_name='admin_signup',
        ),
    ]