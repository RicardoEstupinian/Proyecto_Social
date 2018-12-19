from django.db import models
from apps.miembro.models import Miembro

# Create your models here.

class Tesoreria(models.Model):
    nombre_tesoreria = models.CharField(max_length=50)
    saldo_tesoreria = models.FloatField()

    def __str__(self):
        return self.nombre_tesoreria

class PeriodoAnualDirectivo(models.Model):
    inicio_periodo_anual = models.DateField()
    final_periodo_anual = models.DateField()
    nombre_periodo = models.CharField(max_length=50)
    estado_periodo_anual=models.BooleanField()
    directiva_asignada =models.BooleanField(default=False)


class Periodo(models.Model):
    periodo_anual = models.ForeignKey(PeriodoAnualDirectivo, null=True, on_delete=models.CASCADE)
    inicio_periodo = models.DateField()
    final_periodo = models.DateField()
    estado_periodo=models.BooleanField()

class Transaccion(models.Model):
    periodo = models.ForeignKey(Periodo, null=True, on_delete=models.CASCADE)
    tesoreria = models.ForeignKey(Tesoreria, null=True, on_delete=models.CASCADE)
    fecha_transaccion = models.DateField()
    concepto_transaccion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    monto_transaccion = models.FloatField()

class CargoDirectivo(models.Model):
    nombre_cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cargo

class Directivo(models.Model):
    miembro = models.ForeignKey(Miembro, null=True, blank=True, on_delete=models.CASCADE)
    cargo = models.ForeignKey(CargoDirectivo, null=True, blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(PeriodoAnualDirectivo, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)