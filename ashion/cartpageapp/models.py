from django.db import models

# Create your models here.
class cartpage_data(models.Model):
    product_image = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    