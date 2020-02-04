from django.shortcuts import render
from .models import Brand, Product, Shade 

# Create your views here.

def home(request):
    
    brands = Brand.objects.all()
    return render(request, 'home.html', {'brands':brands})


