from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.models import  User,auth
from django.contrib import messages

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

def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user = auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'homepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')

    else:
        return render(request,'login.html')
def register(request):
    return render(request,'register.html')

def register1(request):
 if request.method=="POST":
    username=request.POST['username']
    pass1=request.POST['password']
    pass2=request.POST['password1']
    if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
    else:
            messages.info(request,'Password do not match')
            return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return render(request, 'dashboard.html')
