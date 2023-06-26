from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import FormView, DeleteView, UpdateView

# from polls.forms import RegisterUserForm
from .forms import *
from .models import UserAccounts


# Отображение основной страницы
def index(request):
    return render(request, "polls/landing/index.html")


# Отображение регистрационной формы и переход к профилю при успешной регистрации
class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("polls:profile")

    # Проверка формы
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Отображение страницы описания
def about(request):
    return render(request, "polls/landing/about.html")


# def login(request):
#     return render(request, "polls/landing/login.html")


# Отображение профиля со счетами с проверкой входа пользователя
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = AddAccountForm(request.POST)
        print(form)
        if form.is_valid():
            # print(form.cleaned_data)
            # form.nameofuser = request.user.id
            instance = form.save(commit=False)
            instance.nameofuser = request.user
            instance.save()
            return redirect('profile')
    user_accounts = UserAccounts.objects.all()
    return render(request, 'polls/profile/profile.html', {'user_accounts': user_accounts, })


def delete_account(request, account_id):
    account = UserAccounts.objects.get(pk=account_id)
    account.delete()
    return redirect('profile')


# def edit_account(request, account_id):
#     account = UserAccounts.objects.get(pk=account_id)
#     fields = ['account_name', 'account_start_balance']
#     if request.method == 'POST':
#         form = AddAccountForm(request.POST, instance=account)
#         if form.is_valid():
#             fields = ['account_name', 'account_start_balance']
#             form.update()
#             return redirect('profile')
#     else:
#         form = AddAccountForm(instance=account)
#     return render(request, 'polls/profile/profile.html', {'form': form})

# class AccountDeleteView(DeleteView):
#     model = UserAccounts
#     success_url = reverse_lazy("profile")
#     template_name = 'polls/profile/delete_account.html'


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
