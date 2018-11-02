from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)


class Articulo(models.Model):
    categoria = models.ForeignKey(
        Categoria, null=True, on_delete=models.PROTECT)
    nombre_articulo = models.CharField(max_length=100)
    precio = models.FloatField()
    estado = models.CharField(max_length=100)
    existencia = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    imagen_articulo = models.ImageField(upload='static/img')
    vendible = models.BooleanField()


class Venta(models.Model):
    articulo = models.ForeignKey(Articulo, null=True, on_delete=models.PROTECT)
    concepto_venta = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_venta_unitario = models.FloatField()
    monto_total = models.FloatField()
    fecha_venta = models.DateField()


class Transaccion(models.Model):
    fecha_transaccion = models.DateField()
    concepto_transaccion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    monto_transaccion = models.FloatField()


class Periodo(models.Model):
    transacciones=models.ForeignKey(Transaccion,null=True,on_delete=models.CASCADE)
    inicio_periodo = models.DateField()
    final_periodo = models.DateField()


class PeriodoAnualDirectivo(models.Model):
    periodo=models.ForeignKey(Periodo,null=True,on_delete=models.CASCADE)
    inicio_periodo_anual = models.DateField()
    final_periodo_anual = models.DateField()
    nombre_periodo = models.CharField(max_length=50)
