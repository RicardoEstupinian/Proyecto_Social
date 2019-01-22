from django.urls import path, re_path
from apps.miembro import views
from django.contrib.auth.decorators import login_required

app_name = "miembro"

urlpatterns = [
	path('registrar/', login_required(views.miembro_register), name="registrar"),
	path('carnet/', login_required(views.carnet), name="carnet"),
	path('ver/<id_miembro>/', login_required(views.miembro_view), name="ver"),
	path('administrar/<cargo_m>/', login_required(views.miembro_administrations), name="administrar"),
	path('editar/<id_miembro>/', login_required(views.miembro_update), name="editar"),
]