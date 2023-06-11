from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import UserAccount


def index(request):
    account_list = UserAccount.objects.order_by('-registration_date')
    return render(request, 'MoneyOperation/index.html', {'account_list': account_list})


def account(request, account_name):
    acc = get_object_or_404(UserAccount, pk=account_name)
    return render(request, 'MoneyOperation/account.html', {'account': acc})


def transactions(request, account_name):
    response = "You're looking at the transactions of account %s."
    return HttpResponse(response % account_name)


def single_transaction(request, account_name, transaction_id):
    return HttpResponse("You're looking at the transaction %s." % transaction_id)
