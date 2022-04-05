
from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class ProductsModel(TranslatableModel):
    translations = TranslatedFields (
        prod_name = models.CharField( max_length=100),
        description = models.TextField(),
        picture = models.BooleanField(null=True),
        pic =models.ImageField(upload_to=f'image/prod_pic/{now():%Y/%m/%Y%m%d%H%M%S}', blank=True, null=True),
        file = models.FileField(upload_to=f'file/{now():%Y/%m/%Y%m%d%H%M%S}', blank=True, null=True),
    )

    def __str__(self):
        return self.prod_name

    def __repr__(self):
        return self.__str__()


class ProductsImageModel(models.Model):
    prod = models.ForeignKey(ProductsModel, related_name='prod', on_delete=models.CASCADE)
    pictures = models.ImageField(upload_to=f'image/{now():%Y/%m/%Y%m%d%H%M%S}', blank=True, null=True)

    def __str__(self):
        return self.prod.prod_name

    def __repr__(self):
        return self.__str__()

