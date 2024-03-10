# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Core.models import Product
from .models import CartItem

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user = request.user
    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # Redirect to the view cart page after adding to cart
    return redirect('view_cart')

@login_required
def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    return render(request, 'view_cart.html', {'cart_items': cart_items})
