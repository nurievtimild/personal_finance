from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import FormView

# from polls.forms import RegisterUserForm
from .forms import *
from .models import UserAccounts



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
    if request.method == 'POST':
        print('4516111')
        form = AddAccountForm(request.POST)
        print(form)

        if form.is_valid():
            # print(form.cleaned_data)
            print('111')
            # form.nameofuser = request.user.id
            instance = form.save(commit=False)
            instance.nameofuser = request.user
            instance.save()

            print('1222')
            return redirect('profile')
        print('565656')
    user_accounts = UserAccounts.objects.all()
    accounts_names = []
    for acc in user_accounts:
        accounts_names.append(acc.account_name)
    return render(request, 'polls/profile.html', {'user_accounts': user_accounts})

# class AccountView(FormView):
#     form_class = AddAccountForm
#     success_url = reverse_lazy("polls:profile")
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# def add_account(request):
#     print('123')
#     if request.method == 'POST':
#         print('456')
#         form = AddAccountForm(request.POST)
#         print('987')
#         if form.is_valid():
#             # print(form.cleaned_data)
#             print('111')
#             form.save()
#             print('1222')
#             return redirect('profile')
#         print('565656')
#
#     return render(request, 'polls/profile.html')
