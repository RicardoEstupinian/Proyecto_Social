from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('transaccion/', login_required(transaccion), name="transaccion"),
	path('factura/<tipo_aux>/', login_required(factura_pdf.as_view()), name="factura_pdf"),
	path('periodo-directivo/', login_required(periodoDirectivo), name="periodo_directivo"),
	path('periodo-directivo/asignacion/', login_required(asignar_directiva), name="asignar_directiva"),
	path('periodo-directivo/periodos/<id>/', login_required(periodo_list), name="periodo_list"),
	path('periodo-directivo/periodos/periodo/<id>/', login_required(periodo_seleccionado), name="periodo_seleccionado"),
	path('periodo/<id>/<tipo>/', login_required(periodo_pdf.as_view()), name="periodo_pdf"),
]