from django.urls import path
from apps.cuentasxcobrar import views

app_name = "cuentasxcobrar"

urlpatterns = [
    path('',views.cargarDeuda, name="cargarDeuda"),

]
