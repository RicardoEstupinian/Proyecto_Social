from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
	path('transaccion/', transaccion, name="transaccion"),
	path('factura/<tipo_aux>/', factura_pdf.as_view(), name="factura_pdf"),
	path('periodo-directivo/', periodoDirectivo, name="periodo_directivo"),
	path('periodo-directivo/asignacion/', asignar_directiva, name="asignar_directiva"),
	path('periodo-directivo/periodos/<id>/', periodo_list, name="periodo_list"),
	path('periodo-directivo/periodos/periodo/<id>/', periodo_seleccionado, name="periodo_seleccionado"),
	path('periodo/<id>/', periodo_pdf.as_view(), name="periodo_pdf"),
]