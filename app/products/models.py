from django.db import models

class ProductModel(models.Model):

    name_product = models.CharField('Name Product', max_length=255, null=True, blank=True)
    plataform = models.CharField('Plataform', max_length=255)
    price = models.FloatField('Price', default=0, null=True, blank=True)
    restaurant = models.CharField('Restaurant', max_length=255, null=True, blank=True)
    category = models.CharField('Category', max_length=255, null=True, blank=True)


    def __str__(self):
        return self.name_product