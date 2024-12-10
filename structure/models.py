from django.db import models

from users.models import User


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=128,unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='collections_imgs')

    def __str__(self):
        return self.name


class Year(models.Model):
    year = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.year


class Artwork(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    collection = models.ForeignKey(to=Collection, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artworks_imgs')
    year = models.ForeignKey(to=Year, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return f"Name:{self.name}; Collection:{self.collection}; Year:{self.year}"


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def for_user(self, user):
        return self.filter(user=user)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Artwork, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'{self.user} basket'

    def sum(self):
        return self.quantity * self.product.price

    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': self.sum()
        }
        return basket_item

