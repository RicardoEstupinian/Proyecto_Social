from django.urls import path
from apps.venta import views

app_name = "venta"

urlpatterns = [
    path('',views.buscar, name="listar"),
    path('editar/<pk>',views.ArticuloUpdate.as_view(), name="editar"),
    path('crear/',views.ArticuloCreate.as_view(), name="crear"),
]
