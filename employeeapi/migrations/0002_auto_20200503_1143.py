# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-03 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_code',
            field=models.TextField(max_length=3),
        ),
        migrations.AlterField(
            model_name='employee',
            name='fullname',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.TextField(max_length=20),
        ),
    ]
