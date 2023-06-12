from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import FormView

# from polls.forms import RegisterUserForm
from .forms import *


def index(request):
    template = loader.get_template("landing/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("polls:profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


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
