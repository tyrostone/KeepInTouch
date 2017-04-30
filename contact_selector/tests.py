# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class MockContact(object):
    def __init__(self, name, company, email, phone):
        self.name = name
        self.company = company
        self.email = email
        self.phone = phone
