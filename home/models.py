from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
LABELS = (('hot','hot'),('new','new') , ('','default'))

class Category(models.Model):
    name = models.CharField(max_length=400)
    icon = models.CharField(max_length=200)
    slug = models.CharField(max_length=300,unique = True)

    def __self__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField (upload_to= 'media')
    description = models.TextField(blank = True)
    url = models.CharField(max_length=250,null = True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField (upload_to= 'media')
    url = models.CharField(max_length=250,null = True)
    rank = models.ImageField()

    def __self__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField (upload_to= 'media')
    slug = models.CharField(max_length=300,unique = True)

    def __self__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField (upload_to= 'media')
    price = models.IntegerField()
    discount_price = models.IntegerField(default = 0)
    size = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    description = models.TextField(blank = True)
    specification = models.TextField(blank = True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    labels = models.CharField(choices= LABELS,max_length=200,blank=True)
    brand = models.ForeignKey(Brand,on_delete=CASCADE)

    def __self__(self):
        return self.name


