from django.shortcuts import render

import os
from os.path import join, exists, basename
from urllib import response

from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import render
from django.views.generic import ListView

from products.models import ProductsModel, ProductsImageModel
from svale_website import settings


class ProductsListView(ListView):
    model = ProductsModel
    template_name = 'products.html'


def productsList(request):
    prod = ProductsModel.objects.all()
    return render(request, 'home.html', {'prod': prod})


def productsAll(request):
    p = ProductsModel.objects.all()
    return render(request, 'products.html', {'p': p})


def productsPictures(request, pk):
    pic = ProductsImageModel.objects.all().filter(prod_id=pk)
    return render(request, 'gallery.html', {'pic': pic})

"""
A specification.html nem mukodik, ezert lett kikommentelve
def productsSpecification(request, pk):
    spec = ProductsModel.objects.all().filter(id=pk)
    return render(request, 'specification.html', {'spec': spec})
"""


def download(request, path):
    file_path = join(settings.MEDIA_ROOT, path)
    if exists(file_path):
        with open(file_path, 'rb') as fh:
            res = HttpResponse(fh.read(), content_type="application/file")
            res['Content-Disposition'] = 'inline;filename=' + basename(file_path)
            return res
    raise Http404

