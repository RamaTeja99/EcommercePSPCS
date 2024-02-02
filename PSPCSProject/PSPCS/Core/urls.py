from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView  # Import the correct LoginView

urlpatterns = [
    path('', homepage, name='homepage'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('products/', products, name='products'),
    path('categories/', categories, name='categories'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
