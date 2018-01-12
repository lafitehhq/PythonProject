from django.test import TestCase

# Create your tests here.

from app01.models import *

class Person():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

Person.name



