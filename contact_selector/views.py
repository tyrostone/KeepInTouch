# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.shortcuts import render
from django.http import HttpResponse

from models import Contact


def index(request):
    stalest_contacts = Contact.objects.order_by('last_contacted')[::5]
    contact = stalest_contacts[random.randint(0, len(stalest_contacts))]
    return HttpResponse("Contact {} this week: {} or {}".format(contact.name, contact.email, contact.phone))