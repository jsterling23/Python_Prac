# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
# Create your models here.


class NewUserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Must enter first name"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Must enter last name"
        if len(postData['email']) < 2:
            errors['email'] = "Must enter an email"
        if len(postData['username']) < 2:
            errors['username'] = "Must enter username"
        if len(postData['password']) < 2:
            errors['password'] = "Must enter password"
        if postData['password'] != postData['confirm_password']:
            errors['pass_match'] = "Passwords do not match"
        return errors

class NewUserManager_login(models.Manager):
    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) < 5:
            errors['email'] = "Must enter an email"
        if len(postData['password']) < 2:
            errors['password'] = "Must enter password"
        if len(errors):
            return errors

        if NewUser.objects.filter(email=postData['email']).exists():
            user = NewUser.objects.get(email=postData['email'])
        else:
            errors['email_not_exists'] = "That email doesn't exist"
            return errors

        db_password = user.password
        login_password = postData['password']

        if bcrypt.checkpw(login_password.encode(), db_password.encode()) == False:
            errors['password_incorrect'] = "Password is incorrect"
            return errors
        else:
            return 


class NewUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = NewUserManager()
    objectsTwo = NewUserManager_login()

    def __str__(self):
        return "First: {} - Last: {} - Email: {} - Username: {} - Password-Hashed: {}".format(self.first_name, self.last_name, self.email, self.username, self.password)
