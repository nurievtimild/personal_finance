from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("landing/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def registration(request):
    template = loader.get_template("landing/registration.html")
    context = {}
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template("landing/about.html")
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template("landing/login.html")
    context = {}
    return HttpResponse(template.render(context, request))