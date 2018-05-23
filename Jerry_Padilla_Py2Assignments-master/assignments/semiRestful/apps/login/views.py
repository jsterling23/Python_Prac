# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..users.models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
import bcrypt

# Create your views here.



def index(request):
    template = 'login/login.html'
    return render(request, template)

def process_log_data(request):

    if request.method == "POST":

        form_errors = {}
        db_errors = {}

        form_password = request.POST['password']
        form_email = request.POST['email']


        # validating form data to make sure it is filled before querying the DB

        if len(form_password) < 1:
            form_errors['password'] = "Must enter a password"

        if len(form_email) < 1:
            form_errors['email'] = "Must enter an email"

        if len(form_errors):
            for tag, error in form_errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('login:index'))



        # querying the DB then checks for errors

        if Users.objects.filter(email=form_email).exists():
            db_password = Users.objects.get(email=form_email).password

            if bcrypt.checkpw(form_password.encode(),db_password.encode()) == True:
                print "passwords match"
                user = Users.objects.get(email=form_email).first_name
                request.session['user_name'] = user
                print request.session['user_name']
                return redirect(reverse('users:index'))
            else:
                db_errors['db_password_query'] = "Password Incorrect"

        else:
            db_errors['db_email_query'] = "Email not registered"

        if len(db_errors):
            for tag, error in db_errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('login:index'))


        return redirect(reverse('login:index'))
