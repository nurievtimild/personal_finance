from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# from django.template import loader
from django.urls import reverse_lazy, reverse
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
        if form.is_valid():
            # print(form.cleaned_data)
            # form.nameofuser = request.user.id
            instance = form.save(commit=False)
            instance.nameofuser = request.user
            instance.account_current_balance = request.POST.get('account_start_balance')
            instance.save()
            return redirect('profile')
    user_accounts = UserAccounts.objects.order_by('account_start_date')

    return render(request, 'polls/profile/profile.html', {'user_accounts': user_accounts, })


@login_required
def add_transaction(request, account_id):
    if request.method == 'POST':
        form = AddTransactionForm(request.POST)
        user_account = UserAccounts.objects.get(account_id=account_id)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.account_id = UserAccounts.objects.get(pk=account_id)
            if instance.is_expense:
                instance.amount = -float(request.POST.get('amount'))
                user_account.account_current_balance -= float(request.POST.get('amount'))
            elif instance.is_income:
                user_account.account_current_balance += float(request.POST.get('amount'))
            elif instance.is_transfer:
                transfer_account = UserAccounts.objects.get(account_id=instance.transfer_account_id)
                transfer_account.account_current_balance += float(request.POST.get('amount'))
                user_account.account_current_balance -= float(request.POST.get('amount'))
                transfer_account.save()
            user_account.account_new = False
            user_account.save()
            instance.save()

            return redirect('profile')
        else:
            # Do something in case if form is not valid
            raise ValidationError(form.errors)

    # account_transaction = Transaction.objects.all()
    return render(request, 'polls/profile/profile.html')

def delete_account(request, account_id):
    account = UserAccounts.objects.get(pk=account_id)
    account.delete()
    return redirect('profile')

@login_required
def edit_account(request, account_id):
    account = UserAccounts.objects.get(pk=account_id)
    if request.method == 'POST':
        account.account_name = request.POST.get('account_name')
        if account.account_new:
            account.account_start_balance = request.POST.get('account_start_balance')
            account.account_current_balance = request.POST.get('account_start_balance')
        account.save()
        return redirect('profile')
    else:
        return render(request, 'profile.html')

@login_required
def history_accounts(request, account_id):
    transactions = Transaction.objects.filter(account_id=account_id)

    return render(request, 'polls/profile/history_accounts.html', {'transactions': transactions, })


def delete_transaction(request, transaction_id):
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    account_id = transaction.account_id
    transaction.delete()
    return redirect('history_accounts', account_id)


