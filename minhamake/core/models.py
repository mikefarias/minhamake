from django.db import models

# Create your models here.


class Brand(models.Model):
    
    name = models.CharField(max_length=50)
    ative = models.BooleanField
    image = models.ImageField

    def __str__(self):
        return self.name


class Shade(models.Model):
    
    name = models.CharField(max_length=50)
    ative = models.BooleanField
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    image = models.ImageField

    def __str__(self):
        return self.name


class SkinTone(models.Model): 
    
    name = models.CharField(max_length=50)
    ative = models.BooleanField
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    image = models.ImageField

    def __str__(self):
        return self.name

class Product(models.Model): 

    name = models.CharField(max_length=50)
    ative = models.BooleanField
    shade = models.ManyToManyField(Shade)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    image = models.ImageField

    def __str__(self):
        return self.name

class SelectedProductManager(models.Manager): 
    
    def create_selected_product(self, product, shade):
        selected_product = self.create(product=product, shade=shade)
        return selected_product


class SelectedProduct(models.Model): 

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    shade = models.ForeignKey(Shade, on_delete=models.PROTECT)

    objects = SelectedProductManager()