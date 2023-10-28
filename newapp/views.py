from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def indexhtml(request):
    template = loader.get_template('new.html')
    return HttpResponse(template.render())

def indexhtml1(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def indexhtml2(request):
    template = loader.get_template('calender.html')
    return HttpResponse(template.render())