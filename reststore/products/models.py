from django.db import models

# Create your models here.


class Product(models.Model):
    """
    Product model
    Defines product attributes
    """
    idnum = models.IntegerField()
    name = models.CharField(max_length=255)
    colour = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_brand(self):
        return self.name + ' product number %s' + ' is ' + self.brand % self.idnum

    def __repr__(self):
        return self.name + ' product number %s' + ' is added.'
