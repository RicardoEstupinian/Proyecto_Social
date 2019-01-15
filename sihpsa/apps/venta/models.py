from django.db import models
from django.urls import reverse

# Create your models here.


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_categoria


class Articulo(models.Model):
    categoria = models.ForeignKey(
        Categoria, null=True, on_delete=models.PROTECT)
    nombre_articulo = models.CharField(max_length=100)
    precio = models.FloatField()
    estado = models.CharField(max_length=100)
    existencia = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    imagen_articulo = models.ImageField(upload_to='static/img', blank=True,null=True)
    vendible = models.BooleanField()


    def __str__(self):
        return self.nombre_articulo


class Venta(models.Model):
    articulo = models.ForeignKey(Articulo, null=True, on_delete=models.PROTECT)
    concepto_venta = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_venta_unitario = models.IntegerField()
    monto_total = models.IntegerField()
    fecha_venta = models.DateField()
