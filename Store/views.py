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
def index(request):
	return HttpResponse("Index page of Store")

def customer(request):
	if request.method == 'GET':
		customer = Customer.objects.all()
		serializer = CustomerSerializer(customer, many=True)
		return JSONResponse(serializer.data)

def inventory(request):
	if request.method == 'GET':
		inventory = Inventory.objects.all()
		serializer = InventorySerializer(inventory, many=True)
		return JSONResponse(serializer.data)

def purchase(request):
	if request.method == 'GET':
		purchase = Purchase.objects.all()
		serializer = PurchaseSerializer(purchase, many=True)
		return JSONResponse(serializer.data)