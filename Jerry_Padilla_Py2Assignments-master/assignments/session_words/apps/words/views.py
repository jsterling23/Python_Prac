# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.


def index(request):

    template = 'words/index.html'
    return render(request,template)


def process_data(request, methods="POST"):
    new_word = {}

    # print request.session['new_words']

    for key,value in request.POST.iteritems():
        if key != 'csrfmiddlewaretoken':
            new_word[key] = value

    new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")


    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    temp_list = request.session['words']
    temp_list.append(new_word)
    request.session['words'] = temp_list
    
    return redirect('/')

def clear_session(request):
    del request.session['words']
    return redirect('/')
