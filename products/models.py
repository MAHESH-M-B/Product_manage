
# Create your models here.
from django.db import models

class Product(models.Model):
    item_code = models.CharField(max_length=50)
    item_name = models.CharField(max_length=100)
    category_l1 = models.CharField(max_length=50)
    category_l2 = models.CharField(max_length=50)
    upc = models.CharField(max_length=50)
    parent_code = models.CharField(max_length=50, null=True, blank=True)
    mrp_price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    enabled = models.CharField(max_length=50)
