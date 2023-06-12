from django.db import models

# Create your models here.

class UserAccount(models.Model):
    account_name = models.CharField(max_length=20)
    base_currency = models.CharField(max_length=20)
    registration_date = models.DateTimeField('registration date')

    def __str__(self):
        return self.account_name


class Transaction(models.Model):
    account_name = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    id = models.IntegerField
    money_amount = models.FloatField
    description = models.CharField(max_length=200)
    transaction_date = models.DateTimeField('transaction date')

    def __str__(self):
        return self.money_amount
