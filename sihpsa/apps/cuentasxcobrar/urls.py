from django.urls import path,re_path
from apps.cuentasxcobrar.views import *
from django.contrib.auth.decorators import login_required

app_name = 'cuentasxcobrar'

urlpatterns = [
    path('', login_required(cargarDeuda), name='cargarDeuda'),
    path('lista', login_required(lista_deudores), name="listaDeudores"),
    path('lista/<id>/', login_required(saldar_deuda), name= "saldarDeuda"),

]
