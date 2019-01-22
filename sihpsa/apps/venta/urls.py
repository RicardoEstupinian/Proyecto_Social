from django.urls import path
from apps.venta import views
from django.contrib.auth.decorators import login_required

app_name = "venta"

urlpatterns = [
    path('', login_required(views.buscar), name="listar"),
    path('editar/<pk>', login_required(views.ArticuloUpdate.as_view()), name="editar"),
    path('crear/', login_required(views.ArticuloCreate.as_view()), name="crear"),
]
