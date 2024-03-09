from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from Core.models import Product

def search_products(request):
    search_term = request.GET.get('searchTerm')
    if search_term:
        search_term = search_term.lower()
        # Find the product with the exact name matching the search term
        try:
            product = Product.objects.get(name__iexact=search_term)
            product_id = product.id
            return redirect(reverse('product_description', args=[product_id]))
        except Product.DoesNotExist:
            return redirect('products')
    else:
        return render(request, 'search_form.html')

def product_description(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    formatted_description = product.description.replace("->", "<br>")
    last_product_viewed = request.session.get('last_product_viewed', [])

    # Ensure last_product_viewed is always a list
    if not isinstance(last_product_viewed, list):
        last_product_viewed = [last_product_viewed]

    # Append the current product ID to the list of last viewed products
    if product_id not in last_product_viewed:
        last_product_viewed.append(product_id)

    # Limit the list to the last 4 viewed products
    last_product_viewed = last_product_viewed[-4:]

    # Update the session variable
    request.session['last_product_viewed'] = last_product_viewed

    # Retrieve the product objects for the last viewed products
    last_viewed_products = Product.objects.filter(pk__in=last_product_viewed)

    # Ensure the current product is not included in the last viewed products
    last_viewed_products = last_viewed_products.exclude(pk=product_id)

    return render(request, 'product_description.html', {'product': product, 'last_viewed_products': last_viewed_products,'formatted_description': formatted_description})
