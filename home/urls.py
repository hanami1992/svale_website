from django.urls import path

from products.views import productsList

urlpatterns = [
    path('', productsList, name='home')
]
