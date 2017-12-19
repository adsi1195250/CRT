from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Trabajadores(models.Model):
	id = models.AutoField(primary_key=True)
	nombres = models.CharField(max_length=100,blank=True,null=True)
	cedula = models.IntegerField(unique=True)
	fechaIngreso = models.DateField()
	fechaNacimiento = models.DateField()
	edad = models.SmallIntegerField()
	cargo = models.BooleanField()
	telefono = models.IntegerField()
	foto = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)
	def __str__(self):
		return self.cedula

class CodigoBarras(models.Model):
	idCodigoBarras = models.AutoField(primary_key=True)
	CodigoBarras = models.CharField(max_length=200)
	idTrabajadores = models.ForeignKey(Trabajadores, on_delete= models.CASCADE)
	def __str__(self):
		return self.idCodigoBarras

class Historial_IO(models.Model):
	idHistorial = models.AutoField(primary_key=True)
	horaEntrada = models.DateTimeField()
	horaSalida = models.DateTimeField()
	horaDesayuno = models.DateTimeField()
	horaDescanso = models.DateTimeField()
	horaPausasActivas = models.DateTimeField()
	horaAlmuerzo = models.DateTimeField()
	def __str__(self):
		return self.idHistorial


class PermisoAusentismo(models.Model):
	idPermisoAusentismo = models.AutoField(primary_key=True)
	fechaSalida = models.DateTimeField()
	totalHoras = models.SmallIntegerField()
	motivo = models.SmallIntegerField()
	observacion= models.CharField(max_length=500)
	idTrabajador = models.ForeignKey(Trabajadores, on_delete= models.CASCADE)
	def __str__(self):
		return self.idPermisoAusentismo
