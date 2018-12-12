from django.db import models

# Create your models here.

class Tesoreria(models.Model):
    nombre_tesoreria = models.CharField(max_length=50)
    saldo_tesoreria = models.FloatField()

    def __str__(self):
        return self.nombre_tesoreria


class Transaccion(models.Model):
    tesoreria = models.ForeignKey(
        Tesoreria, null=True, on_delete=models.CASCADE)
    fecha_transaccion = models.DateField()
    concepto_transaccion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    monto_transaccion = models.FloatField()


class Periodo(models.Model):
    transacciones = models.ForeignKey(
        Transaccion, null=True, on_delete=models.CASCADE)
    inicio_periodo = models.DateField()
    final_periodo = models.DateField()
    estado_periodo=models.BooleanField()


class PeriodoAnualDirectivo(models.Model):
    periodo = models.ForeignKey(Periodo, null=True, on_delete=models.CASCADE)
    inicio_periodo_anual = models.DateField()
    final_periodo_anual = models.DateField()
    nombre_periodo = models.CharField(max_length=50)
    estado_periodo_anual=models.BooleanField()
