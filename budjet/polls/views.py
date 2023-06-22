from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import FormView

# from polls.forms import RegisterUserForm
from .forms import *
from .models import UserAccounts

def index(request):
    return render(request, "polls/landing/index.html")


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("polls:profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def about(request):
    return render(request, "polls/landing/about.html")


# def login(request):
#     return render(request, "polls/landing/login.html")


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
    return render(request, 'polls/profile/profile.html', {'user_accounts': user_accounts})

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
#     return render(request, 'polls/profile/profile.html')
