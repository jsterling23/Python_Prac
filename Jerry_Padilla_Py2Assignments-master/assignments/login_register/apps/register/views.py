# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import *
import bcrypt

# register views

def index(request):
    template = 'register/register.html'
    return render(request, template)

def process_data(request):

    if request.method == "POST":
        first_name = request.POST['first_name'].lower()
        last_name = request.POST['last_name'].lower()
        email = request.POST['email'].lower()
        username = request.POST['username'].lower()
        form_password = request.POST['password']


        form_errors = NewUser.objects.register_validator(request.POST)
        db_errors = {}

        if len(form_errors):
            for tag, error in form_errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('register:index'))


        if NewUser.objects.filter(email=email).exists():
            db_errors['email_exists'] = "That email already exists! Please try again..."
        if NewUser.objects.filter(username=username).exists():
            db_errors['username_exists'] = "That username already exists!\n Please choose another Username..."

        if len(db_errors):
            for tag, error in db_errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('register:index'))

        db_password = bcrypt.hashpw(form_password.encode(), bcrypt.gensalt())

        NewUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=db_password,
        )
        messages.success(request, "Thank you for registering!")
        messages.success(request, "Please login to access the site")

        return redirect(reverse('login:index'))
    else:
        messages.error(request, "No No No! You cannot bypass my python!... If you can email me bro...")
        return redirect(reverse('home:index'))
