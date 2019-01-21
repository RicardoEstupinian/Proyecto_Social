from django.urls import path,re_path
from apps.cuentasxcobrar import views

app_name = 'cuentasxcobrar'

urlpatterns = [
    path('',views.cargarDeudaCreate.as_view(), name="cargarDeuda"),
    path('lista',views.cargarDeudaList.as_view(), name="ListaDeudores"),
    path('editar/<pk>', views.cargarDeudaUpdate.as_view(), name= "editar"),

]
