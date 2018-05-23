# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..register.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
import bcrypt

# Create your views here.

def index(request):
    template = 'login/login.html'
    return render(request, template)

def process_login_data(request):

    if request.method == "POST":
        errors = NewUser.objectsTwo.login_validator(request.POST)

        if errors != None:
            if len(errors):
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect(reverse('login:index'))

        user = NewUser.objects.get(email=request.POST['email'])
        username = user.username

        request.session['username'] = username
        request.session['logged_in'] = 'logged_in'

        return redirect(reverse('home:index'))

    return redirect(reverse('login:index'))

def log_out(request):
    del request.session['logged_in']
    del request.session['username']
    return redirect('home:kicked')
