from django.urls import path,re_path
from apps.cuentasxcobrar.views import *

app_name = 'cuentasxcobrar'

urlpatterns = [
    path('', cargarDeuda, name='cargarDeuda'),
    path('lista',lista_deudores, name="listaDeudores"),
    path('lista/<id>/', saldar_deuda, name= "saldarDeuda"),

]
