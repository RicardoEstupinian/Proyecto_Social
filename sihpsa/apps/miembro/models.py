from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Uniforme(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=50)
    tipo_cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cargo

class Sacramento(models.Model):
    nombre_sacramento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_sacramento

class Medalla(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.color

class Hermandad(models.Model):
    nombre_hermandad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_hermandad

class Miembro(models.Model):
    cuenta = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    sacramentos = models.ManyToManyField(Sacramento)
    uniformes = models.ManyToManyField(Uniforme)
    medalla = models.ManyToManyField(Medalla)
    hermandad = models.ForeignKey(Hermandad, null=True, blank=True, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.CASCADE)
    carnet = models.CharField(max_length=7)
    nombre_m = models.CharField(max_length=100)
    apellido_m = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    fecha_nac = models.DateField()
    estatura = models.FloatField()
    num_contacto = models.CharField(max_length=15)
    nombre_encargado = models.CharField(max_length=50)
    parentesco = models.CharField(max_length=50)
    num_encargado = models.CharField(max_length=15)
    foto_m = models.ImageField(upload_to='static/img', blank=True)

    def __str__(self):
        return self.user.username

class CuentasPorCobrar(models.Model):
    miembro = models.ForeignKey(Miembro, null=True, blank=True, on_delete=models.CASCADE)
    fecha_cc = models.DateField()
    tipo_cc = models.CharField(max_length=50)
    monto_cc = models.FloatField()
    concepto_cc = models.CharField(max_length=50)

