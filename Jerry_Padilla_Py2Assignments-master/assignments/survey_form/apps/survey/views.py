# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.


def index(request):

    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1

    template = 'survey/index.html'
    return render(request, template)


def process_form_data(request, methods="POST"):

    template = 'survey/results.html'

    context = {
        'name':request.POST['name'],
        'dojo_location':request.POST['dojo_location'],
        'favorite_language':request.POST['favorite_language'],
        'comment':request.POST['comment'],
    }

    return render(request, template, context)

def delete_session(request):
    del request.session['count']

    return redirect('/')
