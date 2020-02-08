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
