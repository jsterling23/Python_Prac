# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.

def index(request):
    template = 'show_time/index.html'
    return render(request, template)


def show_time(request):
    
    template = 'show_time/display_time.html'
    time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

    context = {
        'time':time
    }

    return render(request, template, context)
