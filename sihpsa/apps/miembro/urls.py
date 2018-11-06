from django.urls import path
from apps.miembro import views

app_name = "miembro"

urlpatterns = [
	#path('registrar/', views.MiembroCreate.as_view(), name="registrar"),
	path('registrar/', views.registro, name="registrar"),
	path('carnet/', views.carnet, name="carnet"),
	path('listar/<id_miembro>/', views.miembro_list, name="listar"),
]