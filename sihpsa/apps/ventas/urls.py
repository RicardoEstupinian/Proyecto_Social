
from apps.ventas import views
from django.urls import path
from apps.ventas.views import Cargar, Lista
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

app_name = "ventas"

urlpatterns = [
    path('', login_required(views.Cargar),name="venta"),
    path('Lista/', login_required(views.Lista.as_view()), name="Lista"),
]
