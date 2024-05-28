from django.db import models

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=128,unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='collections_imgs')

    def __str__(self):
        return self.name

class Year(models.Model):
    year=models.CharField(max_length=4,unique=True)
    def __str__(self):
        return self.year

class Artwork(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    collection = models.ForeignKey(to=Collection, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artworks_imgs')
    year = models.ForeignKey(to=Year, on_delete=models.CASCADE)
    def __str__(self):
        return f"Name:{self.name}; Collection:{self.collection}; Year:{self.year}"
