from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)


class AddAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccounts
        fields = ('nameofuser', 'account_name', 'account_start_balance')

