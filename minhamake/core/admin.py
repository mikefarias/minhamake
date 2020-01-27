from django.contrib import admin

from .models import Brand, Product, SkinTone, Shade

# Register your models here.

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(SkinTone)
admin.site.register(Shade)