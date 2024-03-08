from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth


def dashboard(request):
     return render(request, 'dashboard.html')


def homepage(request):
    return render(request, 'homepage.html')




def categories(request):
    return render(request, 'categories.html')


def login(request):
    return render(request, 'login.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'dashboard.html')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def register1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Usename already taken')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Password do not match')
            return render(request, 'register.html')


@login_required
def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been successfully logged out.')
    return render(request, 'homepage.html')

@login_required
def custom_logout(request):
    # Log out the user
    auth.logout(request)
    # Add a message for the user
    messages.info(request, 'You have been successfully logged out.')
    # Redirect the user to the login page or any other desired page
    return render(request, 'homepage.html')

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

def products(request):
    # Retrieve all products from the database
    all_products = Product.objects.all()

    # Pagination
    paginator = Paginator(all_products, 9)  # 9 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products.html', {'page_obj': page_obj})



from bs4 import BeautifulSoup
import requests


def scrape_and_update_price(product):
    # Send a GET request to the URL
    response = requests.get(product.link)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the element containing the price
        price_element = soup.find('span', class_='price')

        # Extract the price text
        if price_element:
            price = price_element.text.strip()
            # Update the price field of the product
            product.price = price
            product.save()


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Product


def update_price(request, product_id):
    # Retrieve the product object
    product = get_object_or_404(Product, pk=product_id)

    # Call the function to scrape and update price
    scrape_and_update_price(product)
    return HttpResponse("Price updated successfully!")
