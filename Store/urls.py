from django.conf.urls import url
from Store.models import *
from . import views

#urlpatterns start here
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^login$', views.login, name='login'),
	url(r'^(?P<customerId>[0-9]+)/customer/$', views.customerDetails, name = "customerDetails"),
    url(r'^customer/', views.customer, name='customer'),
    url(r'^(?P<inventoryId>[0-9]+)/inventory/$', views.inventoryDetails, name = "inventoryDetails"),
    url(r'^inventory/', views.inventory, name='inventory'),
    url(r'^(?P<purchaseId>[0-9]+)/purchase/$', views.purchaseDetails, name = "purchaseDetails"),
    url(r'^purchase/', views.purchase, name='purchase'),
]