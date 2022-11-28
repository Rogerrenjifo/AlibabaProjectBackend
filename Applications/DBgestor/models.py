"""Administrate db."""
import datetime
from django.db import models
class Product (models.Model):
    """a"""
    Title=models.CharField(max_length=60)
    ID_product=models.BigIntegerField(default=0)
    Score=models.FloatField(default=1)
    Price=models.FloatField(default=0.00)
    Image=models.URLField()
    Track=models.BooleanField(default=False)
    product=models.CharField(max_length=60)
    num_of_searchs=models.IntegerField(default=0)

class Search(models.Model):
    """b"""
    search= models.CharField(max_length=60)
    num_of_searchs=models.IntegerField(default=0)
    dateInput=models.DateTimeField(default= datetime.datetime.now())
