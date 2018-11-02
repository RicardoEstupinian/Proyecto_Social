from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Miembro(models.Model):
    cuenta = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    nombre_m = models.CharField(max_length=100)
    apellido_m = models.CharField(max_length=100)
    anio_ingreso = models.CharField(max_length=4)
    fecha_nac = models.DateField()
    estatura = models.FloatField()
    num_contacto = models.CharField(max_length=15)
    medalla_green = models.BooleanField(default=False)
    medalla_purple = models.BooleanField(default=False)
    cargo_religioso = models.CharField(max_length=50)
    nombre_religioso = models.CharField(max_length=50)
    nombre_encargado = models.CharField(max_length=50)
    parentesco = models.CharField(max_length=50)
    num_ecargado = models.CharField(max_length=15)
    foto_m = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.nombre_m


class Sacramento(models.Model):
    miembro = models.ManyToManyField(Miembro)
    nombre_sacramento = models.CharField(max_length=50)


class CuentasPorCobrar(models.Model):
    miembro = models.ForeignKey(
        Miembro, null=True, blank=True, on_delete=models.CASCADE)
    fecha_cc = models.DateField()
    tipo_cc = models.CharField(max_length=50)
    monto_cc = models.FloatField()
    concepto_cc = models.CharField(max_length=50)


class Uniforme(models.Model):
    miembro = models.ManyToManyField(Miembro)
    tipo = models.CharField(max_length=50)


class Cargo(models.Model):
    miembro = models.ManyToManyField(Miembro)
    nombre_cargo = models.CharField(max_length=50)
    tipo_cargo = models.CharField(max_length=50)
