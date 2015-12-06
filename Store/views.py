from django.shortcuts import render
from django.http import HttpResponse
from Store.models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Store.serializers import *

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.

# Main page of project at index
def index(request):
	return render(request, 'Store/index.html');

# About page of project at about
def about(request):
	return render(request, 'Store/about.html');

# About page of project at login
def login(request):
	return render(request, 'Store/works.html');

# Contact page of project at contact
def contact(request):
	return render(request, 'Store/contact.html');

# Lists json response of all the customers
def customer(request):
	if request.method == 'GET':
		customer = Customer.objects.all()
		serializer = CustomerSerializer(customer, many=True)
		return JSONResponse(serializer.data)

# Lists json response of a single customer at a time
# Ex: /store/1/customer
def customerDetails(request,customerId):
	if request.method == 'GET':
		customer = Customer.objects.get(pk=customerId)
		serializer = CustomerSerializer(customer, many=False)
		return JSONResponse(serializer.data)

# Lists the json response of all the inventory items
# Ex: /store/inventory
def inventory(request):
	if request.method == 'GET':
		inventory = Inventory.objects.all()
		serializer = InventorySerializer(inventory, many=True)
		return JSONResponse(serializer.data)

# Lists json response of a single inventory at a time
# Ex: /store/1/inventory
def inventoryDetails(request,inventoryId):
	if request.method == 'GET':
		inventory = Inventory.objects.get(pk=inventoryId)
		serializer = InventorySerializer(inventory, many=False)
		return JSONResponse(serializer.data)

# Lists the purcahses by all customers
# Ex: /store/purchase
def purchase(request):
	if request.method == 'GET':
		purchase = Purchase.objects.all()
		serializer = PurchaseSerializer(purchase, many=True)
		return JSONResponse(serializer.data)

# Lists json response of a single purchase at a time
# Ex: /store/1/purchase
def purchaseDetails(request,purchaseId):
	if request.method == 'GET':
		purchase = Purchase.objects.get(pk=purchaseId)
		serializer = PurchaseSerializer(purchase, many=False)
		return JSONResponse(serializer.data)
