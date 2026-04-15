from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    price = models.FloatField()

class Inventory(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    warehouse_id = models.IntegerField()
    quantity = models.IntegerField()