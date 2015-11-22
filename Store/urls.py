from django.conf.urls import url
from Store.models import *
from . import views

#urlpatterns start here
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customer/', views.customer,name='customer'),
    url(r'^inventory/', views.inventory,name='inventory'),
    url(r'^purchase/', views.purchase,name='purchase'),
]