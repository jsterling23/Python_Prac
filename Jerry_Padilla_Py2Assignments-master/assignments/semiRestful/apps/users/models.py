# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Must enter a first name"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Must enter last name"
        if len(postData['email']) < 1:
            errors['email'] = "Must enter a valid email"
        if len(postData['password']) < 1:
            errors['password'] = "Password must be at least 8 characters long"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()

    def __str__(self):
        return "First: {}, Last: {}, Email: {}, Password: {}".format(self.first_name,self.last_name,self.email,self.password)
