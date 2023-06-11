from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:account_name', views.account, name='account'),
    path('<int:account_name>/transactions/', views.transactions, name='transactions'),
    path('<int:account_name>/transactions/<int:transaction_id>', views.single_transaction, name='single_transaction'),
]
