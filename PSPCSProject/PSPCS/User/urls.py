# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other paths
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
]
