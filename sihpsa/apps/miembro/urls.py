from django.urls import path, re_path
from apps.miembro import views

app_name = "miembro"

urlpatterns = [
	#path('registrar/', views.MiembroCreate.as_view(), name="registrar"),
	path('registrar/', views.miembro_register, name="registrar"),
	path('carnet/', views.carnet, name="carnet"),
	path('listar/<id_miembro>/', views.miembro_list, name="listar"),
	path('administrar/<cargo_m>/', views.miembro_administrations, name="administrar"),
	path('editar/<id_miembro>/', views.miembro_update, name="editar"),
]