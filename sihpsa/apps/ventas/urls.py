
from apps.ventas import views
from django.urls import path 
from apps.ventas.views import Cargar, Lista
from django.conf.urls import url, include

app_name = "ventas"

urlpatterns = [
    path('', views.Cargar,name="venta"),
    path('Lista/', views.Lista.as_view(), name="Lista"),
]
