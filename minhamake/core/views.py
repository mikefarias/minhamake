from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
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


def add_selected(request):

    product_id = request.POST.get('product', None)
    product = get_object_or_404(Product, pk=product_id)

    shade_id = request.POST.get('shade', None)
    shade = get_object_or_404(Shade, pk=shade_id)

    SelectedProduct.objects.create_selected_product(product, shade)

    data = load_selected()
    
    return HttpResponse(json.dumps({'instance': data}), content_type="application/json")

def del_selected(request, pk):

    selected_product = get_object_or_404(SelectedProduct, id=pk)
    selected_product.delete()

    data = load_selected()
    return HttpResponse(json.dumps({'instance': data}), content_type="application/json")


def load_selected():

    selected_products = SelectedProduct.objects.all()
    data = []
    if(selected_products):
        for selected_product in selected_products:
            data.append({'id_product': selected_product.product.id, 'name_product': selected_product.product.name, 
                          'id_brand': selected_product.product.brand.id, 'name_brand':selected_product.product.brand.name, 
                          'id_shade': selected_product.shade.id, 'name_shade': selected_product.shade.name, 
                          'id_selected':selected_product.id})          
    return data

