from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.views import LoginView as BaseLoginView

class DashBoardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')

def homepage(request):
    return render(request,'homepage.html')
def products(request):
    return render(request, 'products.html')

def categories(request):
    return render(request, 'categories.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

