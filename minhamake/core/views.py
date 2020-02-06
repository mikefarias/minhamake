from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import Brand, Product, Shade 


# Create your views here.

def home(request):
    
    brands = Brand.objects.all()
    return render(request, 'home.html', {'brands':brands})


def get_products(request, pk):
    
    products = Product.objects.filter(brand=pk)
    products_dict = {}
    for product in products:
        products_dict[product.id] = product.name
    return HttpResponse(json.dumps(products_dict), content_type="application/json")


def get_shades(request, pk):
    
    shades = Shade.objects.filter(brand=pk)
    shades_dict = {}
    for shade in shades:
        shades_dict[shade.id] = shade.name
    return HttpResponse(json.dumps(shades_dict), content_type="application/json")
