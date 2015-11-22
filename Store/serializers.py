from rest_framework import *
from Store.models import *
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('id','Name','Location')

class InventorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Inventory
		fields = ('id','Name','Batch','Quantity','Price','EntryDate','ExpiryDate','RemainingQuantity')

class PurchaseSerializer(serializers.ModelSerializer):
	PurchaseId = serializers.CharField(source='id')
	PurchaseInventory = InventorySerializer()
	PurchaseCustomer = CustomerSerializer()
	class Meta:
		model = Purchase
		fields = ('PurchaseId','PurchaseInventory','SoldDateTime','PurchaseCustomer','PurchaseQuantity')