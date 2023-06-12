from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from polls.forms import RegisterUserForm
from .forms import *


def index(request):
    template = loader.get_template("landing/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def registration(request):
    template = loader.get_template("landing/registration.html")
    context = {}
    form_class = UserCreationForm
    model = User
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template("landing/about.html")
    context = {}
    return HttpResponse(template.render(context, request))


# def login(request):
#     template = loader.get_template("landing/login.html")
#     context = {}
#     return HttpResponse(template.render(context, request))


@login_required
def profile_view(request):
    return render(request, 'polls/profile.html')
