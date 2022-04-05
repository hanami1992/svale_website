
from django.contrib import admin
from parler.admin import TranslatableAdmin

from products.models import ProductsModel, ProductsImageModel


class ProductImageAdmin(admin.StackedInline):
    model = ProductsImageModel


@admin.register(ProductsModel)
class ProductsAdmin(TranslatableAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
        model = ProductsModel


@admin.register(ProductsImageModel)
class ProductImageAdmin(admin.ModelAdmin):
    pass

