
from apps.ventas import views
from django.urls import path 
from apps.ventas.views import Cargar

app_name = "ventas"

urlpatterns = [
    path('', views.Cargar,name="venta"),
]
