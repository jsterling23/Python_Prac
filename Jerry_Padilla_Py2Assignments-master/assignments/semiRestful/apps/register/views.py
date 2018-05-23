# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..users.models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
import bcrypt

# Create your views here.


def index(request):
    template = 'register/register.html'

    return render(request, template)

def process_reg_data(request):
    if request.method == 'POST':

        errors = Users.objects.basic_validator(request.POST)

        db_errors = {}


        if Users.objects.filter(email=request.POST['email']).exists():
            db_errors['db_query'] = "Email already exists"
            if len(db_errors):
                for tag, error in db_errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                    return redirect(reverse('register:index'))
        else:
            errors = Users.objects.basic_validator(request.POST)

        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
                return redirect(reverse('register:index'))


        first = request.POST['first_name']
        last = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        pw_db = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        Users.objects.create(
            first_name = first,
            last_name = last,
            email = email,
            password = pw_db,
        )
        

        return redirect(reverse('users:index'))
