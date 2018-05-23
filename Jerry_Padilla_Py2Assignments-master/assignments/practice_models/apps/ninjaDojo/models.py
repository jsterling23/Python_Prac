# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()

    def __str__(self):
        return 'Name = {}, City = {}, State = {}, Description = {}'.format(self.name,self.city,self.state, self.desc)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name='ninjas')

    def __str__(self):
        return 'First = {}, Last = {}, Dojo = {}'.format(self.first_name, self.last_name, self.dojo)
