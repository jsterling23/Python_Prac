# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def index(request):
    template = 'users/index.html'
    context = {
        'users':Users.objects.all(),
    }
    return render(request, template, context)

def add(request):
    template = 'users/add.html'
    return render(request,template)

def process_add(request):

    if request.method == 'POST':
        errors = Users.objects.basic_validator(request.POST)

        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
                print "i make it here"
            return redirect(reverse('users:add'))
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']

            Users.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            return redirect('/')

def show(request, user_id):
    template = 'users/show.html'
    context = {
        'user':Users.objects.get(id=user_id),
    }
    return render(request, template, context)

def edit(request, user_id):
    template = 'users/edit.html'
    context = {
        'user':Users.objects.get(id=user_id),
    }
    return render(request, template, context)

def process_edit(request, user_id):
    if request.method == "POST":
        errors = Users.objects.basic_validator(request.POST)

        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
                return redirect(reverse('users:edit', kwargs={'user_id': user_id}))
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']

            person = Users.objects.get(id=user_id)
            person.first_name = first_name
            person.last_name = last_name
            person.email = email
            person.save()

            return redirect('/')

def destroy(request, user_id):
    user = Users.objects.get(id=user_id)
    user.delete()
    return redirect('/')
