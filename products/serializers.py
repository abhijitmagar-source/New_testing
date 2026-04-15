from rest_framework import serializers
from .models import Product,Inventory

class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class InventorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'