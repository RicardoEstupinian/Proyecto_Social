from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
	path('transaccion/', transaccion, name="transaccion"),
	path('periodo-directivo/', periodoDirectivo, name="periodo_directivo"),
	path('periodo-directivo/nuevo/', crear_periodo, name="crear_periodo"),
	path('periodo-directivo/periodos/<id>/', periodo_list, name="periodo_list"),
	path('periodo-directivo/periodos/periodo/<id>/', periodo_seleccionado, name="periodo_seleccionado"),
]