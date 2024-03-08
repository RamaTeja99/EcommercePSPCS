from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView  # Import the correct LoginView

urlpatterns = [
    path('', homepage, name='homepage'),
    path('dashboard/',dashboard,name='dashboard'),
    path('products/', products, name='products'),
    path('categories/', categories, name='categories'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('login1/',login1,name='login1'),
    path('register1/',register1,name='register1'),
    path('logout/',logout,name='logout'),
    path('products/', products, name='products'),
    path('products/<int:page_number>/', products, name='products_page'),
]
