# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Employee(models.Model):
    fullname = models.TextField(max_length=100)
    emp_code = models.TextField(max_length=3)
    mobile = models.TextField(max_length=20)

    #create a new employee / POST

    #read a employee / GET

    #update a employee / PUT

    #delete a employee / DELETE
