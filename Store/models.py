from django.db import models

# Create your models here.
class Customer(models.Model):
	Name = models.CharField(max_length=50)
	Location = models.CharField(max_length=200)
	def __str__(self):
		return "Id : " + str(self.id) + "\nName : " + str(self.Name) + "\nLocation : " + str(self.Location)

class Inventory(models.Model):
	Name = models.CharField(max_length=50)
	Batch = models.CharField(max_length=25)
	Quantity = models.IntegerField()
	Price = models.IntegerField()
	EntryDate = models.DateField(auto_now=True)
	ExpiryDate = models.DateField()
	RemainingQuantity = models.IntegerField()
	def __str__(self):
		return "Id : " + str(self.id) + "\nName : " + str(self.Name) + "\nBatch : " + str(self.Batch) + "\nRemaining : " + str(self.RemainingQuantity)


class Purchase(models.Model):
	PurchaseInventory = models.ForeignKey(Inventory)
	SoldDateTime = models.DateTimeField(auto_now=True)
	PurchaseCustomer = models.ForeignKey(Customer)
	PurchaseQuantity = models.IntegerField()
	def __str__(self):
		return "Id : " + str(self.id) + "\nInventory : " + str(self.PurchaseInventory) + "\nCustomer : " + str(self.PurchaseCustomer) + "\nQuantity : " + str(self.PurchaseQuantity)