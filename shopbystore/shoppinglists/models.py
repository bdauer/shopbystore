from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    signup_date = DateTimeField()
    last_login = DateTimeField()
    user_type = models.CharField(max_length=10)
    stores = models.ManyToManyField(Store, through='User_Store')
    last_location = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.username

class Store(models.Model):
    name = models.CharField(max_length=50)
    coordinates = models.DecimalField(max_digits=9, decimal_places=6)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=4)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.name + " in " + self.city + ", " + self.state


class User_Store(models.Model):
    user = models.ForeignKey(User)
    store = models.ForeignKey(Store)
    public_view = models.BooleanField(default=True)
    public_edit = models.BooleanField(default=False)
