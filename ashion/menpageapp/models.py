from django.db import models

# Create your models here.
class men_poster_carousel(models.Model):
    poster_img = models.CharField(max_length=50)


class men_poster_offer(models.Model):
    offer_img = models.CharField(max_length=50)


class men_product_carousel(models.Model):
    product_img = models.CharField(max_length=50)
    product_title = models.CharField(max_length=50)
    product_des = models.TextField(max_length=200)
    product_price = models.CharField(max_length=50)


class men_product_collection(models.Model):
    product_img = models.CharField(max_length=50)
    product_title = models.CharField(max_length=50)
    product_des = models.TextField(max_length=200)
    product_price = models.CharField(max_length=50)


class men_bottom_poster(models.Model):
    bottom_img = models.CharField(max_length=50)
    