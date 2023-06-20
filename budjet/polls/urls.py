from django.urls import path

from . import views
from .views import profile_view, RegisterView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('about/', views.about, name='about'),
    path("profile/", profile_view, name='profile'),


]
