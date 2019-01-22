
from apps.ventas import views
from django.urls import path 
from apps.ventas.views import Cargar
from django.contrib.auth.decorators import login_required

app_name = "ventas"

urlpatterns = [
    path('', login_required(views.Cargar),name="venta"),
]
