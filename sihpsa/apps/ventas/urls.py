
from apps.ventas import views
from django.urls import path 
from apps.ventas.views import Cargar

urlpatterns = [
    path('venta/', views.Cargar),
]
