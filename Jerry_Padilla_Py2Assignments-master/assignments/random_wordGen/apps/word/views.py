# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.


def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1;

    template = 'word/index.html'
    return render(request, template)



def random_string(request):
    word = get_random_string(length=14)

    context = {
        'word':word,
    }
    template = 'word/show_word.html'
    return render(request, template, context)



def delete_session(request):
    del request.session['count']

    return redirect('/')
