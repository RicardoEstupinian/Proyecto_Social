from django.contrib import admin
from apps.transaccion.models import Tesoreria, Transaccion, Periodo, PeriodoAnualDirectivo

# Register your models here.
admin.site.register(Tesoreria)
admin.site.register(Transaccion)
admin.site.register(Periodo)
admin.site.register(PeriodoAnualDirectivo)