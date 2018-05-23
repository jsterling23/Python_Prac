# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    template = 'blogs/index.html'
    return render(request, template)


def new_blog(request):
    template = 'blogs/new_blog.html'
    return render(request, template)

def create(request):

    return redirect('/')

def show(request, number):

    template = 'blogs/show_blog.html'
    context = {
        'number':number
    }
    return render(request, template, context)

def edit(request, number):

    template = 'blogs/edit.html'
    context = {
        'number':number
    }
    return render(request, template, context)

def destroy(request, number):
    return redirect('/')
