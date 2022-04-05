from django.conf.urls import url
from django.urls import path

from products.views import productsAll, productsPictures

urlpatterns = [
    path('', productsAll, name='products'),
    path('gallery/<int:pk>/', productsPictures, name='gallery'),
]
