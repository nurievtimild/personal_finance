from django.http import HttpResponse


def index(request):
    return HttpResponse("Salam, world. You're at the MoneyOperation index.")


from django.shortcuts import render

# Create your views here.
