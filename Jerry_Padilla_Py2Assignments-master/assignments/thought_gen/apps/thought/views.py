# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from .models import *
from django.shortcuts import render, redirect

# Create your views here.


def index(req):
    template = 'thought/index.html'
    context = {
        'data':NewUser.objects.all(),
    }
    return render(req,template, context)



def thought_form(req):
    template = 'thought/form.html'
    return render(req,template)




def add_thought(req, methods='POST'):

    name = req.POST['name']
    thought = req.POST['thought']

    if len(name) < 1:
        messages.add_message(req, messages.INFO, 'Must enter name')
        return redirect('/thought_form')
    if len(thought) < 10:
        messages.add_message(req, messages.INFO, 'Must enter thought')
        return redirect('/thought_form')
    else:
        Thought.objects.create(
            name=name,
            thought=thought,
        )


    return redirect('/results')

def results(req):
    template = 'thought/result.html'

    context = {
        'thought':Thought.objects.all()
    }
    return render(req,template, context)
