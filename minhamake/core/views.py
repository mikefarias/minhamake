from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json

from .models import Brand, Product, Shade, SelectedProduct


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


def add_product(request):

    product_id = request.POST.get('product', None)
    product = get_object_or_404(Product, pk=product_id)

    shade_id = request.POST.get('shade', None)
    shade = get_object_or_404(Shade, pk=shade_id)

    selected_product = SelectedProduct.objects.create_selected_product(product, shade)
    
    print(product, shade)
    print(selected_product)

    return HttpResponse(json.dumps(''), content_type="application/json")