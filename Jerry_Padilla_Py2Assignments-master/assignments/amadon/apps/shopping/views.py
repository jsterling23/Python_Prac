# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .itemList import items
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    template = 'shopping/index.html'

    context = {
        'items':items
    }

    return render(request,template, context)



def process_purchase(request, methods=['POST']):

    # I see the easier solution on the learning platform and will make a note that it can be done by passing in the item number into the url

    request.session['quantity'] = request.POST['quantity']

    if request.POST['quantity'] == '1':
        quantity = 1
    elif request.POST['quantity'] == '2':
        quantity = 2
    else:
        quantity = 3

    if request.POST['product_id'] == '1':
        request.session['name'] = items[0]['name']
        request.session['price'] = items[0]['price']
        request.session['total'] = request.session['price'] * quantity
        print request.session['total']
    if request.POST['product_id'] == '2':
        request.session['name'] = items[1]['name']
        request.session['price'] = items[1]['price']
        request.session['total'] = request.session['price'] * quantity
        print request.session['total']
    if request.POST['product_id'] == '3':
        request.session['name'] = items[2]['name']
        request.session['price'] = items[2]['price']
        request.session['total'] = request.session['price'] * quantity
        print request.session['total']

    return redirect('checkout/')



def checkout(request):
    template = 'shopping/checkout.html'
    return render(request,template)



def clear_cart(request):
    del request.session['name']
    del request.session['price']
    del request.session['total']
    del request.session['quantity']
    return redirect('/')
