# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    email = models.EmailField()
    phone = PhoneNumberField()
    last_contacted = models.DateField(default=datetime.date.today)
