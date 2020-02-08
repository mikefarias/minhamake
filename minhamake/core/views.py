from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import Brand, Product, Shade 


# Create your views here.

def home(request):
    
    return render(request, 'home.html')


def get_brands(request):
    
    brands = Brand.objects.all()
    brands_dict = {}
    for brand in brands:
        brands_dict[brand.id] = brand.name
    return HttpResponse(json.dumps(brands_dict), content_type="application/json")


def get_products(request, brand_id):
    
    products = Product.objects.filter(brand=brand_id)
    products_dict = {}
    for product in products:
        products_dict[product.id] = product.name
    return HttpResponse(json.dumps(products_dict), content_type="application/json")


def get_shades(request, product_id):
    
    shades = Shade.objects.filter(product=product_id)
    shades_dict = {}
    for shade in shades:
        shades_dict[shade.id] = shade.name
    return HttpResponse(json.dumps(shades_dict), content_type="application/json")
