from django.urls import path
from apps.venta import views

app_name = "venta"

urlpatterns = [
    path('',views.buscar, name="listar"),
    path('editar/<articulo_id>',views.editar, name="editar"),
    path('crear/',views.ArticuloCreate.as_view(), name="crear"),
]