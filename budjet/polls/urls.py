from django.urls import path

from . import views
from .views import profile_view

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('about/', views.about, name='about'),
    # path('login/', views.login, name='login'),
    path("profile/", profile_view, name='profile'),
]
