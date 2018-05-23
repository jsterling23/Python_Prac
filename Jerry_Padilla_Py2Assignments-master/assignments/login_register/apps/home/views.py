# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from ..register.models import *

# Create your views here.

def index(request):
    if 'logged_in' not in request.session:
        return redirect('home:kicked')

    template = 'home/index.html'
    context = {
        'users':NewUser.objects.all(),
    }
    return render(request, template, context)

def kicked(request):
    template = 'home/kicked.html'
    return render(request, template)
