from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Trabajadores(models.Model):
	id = models.AutoField(primary_key=True)
	nombres = models.CharField(max_length=255,blank=True,null=True)
	cedula = models.CharField(max_length=11)
	fechaIngreso = models.DateField()
	fechaNacimiento = models.DateField()
	edad = models.SmallIntegerField()
	area = models.BooleanField()
	telefono = models.CharField(max_length=11)
	foto = models.ImageField(height_field=None, width_field=None, max_length=100)
	def __str__(self):
		return '%s'%self.cedula

class CodigoBarras(models.Model):
	idCodigoBarras = models.AutoField(primary_key=True)
	CodigoBarras = models.CharField(max_length=200)
	idTrabajadores = models.ForeignKey(Trabajadores, on_delete= models.CASCADE)
	def __str__(self):
		return self.CodigoBarras

class Historial_IO(models.Model):
	idHistorial = models.AutoField(primary_key=True)
	horaEntrada = models.DateTimeField()
	horaSalida = models.DateTimeField()
	horaDesayuno = models.DateTimeField()
	horaDescanso = models.DateTimeField()
	horaPausasActivas = models.DateTimeField()
	horaAlmuerzo = models.DateTimeField()


class PermisoAusentismo(models.Model):
	idPermisoAusentismo = models.AutoField(primary_key=True)
	fechaSalida = models.DateTimeField()
	#totalHoras = models.SmallIntegerField()
	motivo = models.SmallIntegerField()
	periodoIncapacidadInicial = models.DateField()
	periodoIncapacidadFinal = models.DateField()
	diasIncapacidad= models.SmallIntegerField()
	codigoDiagnostico = models.CharField(max_length=10)
	descripcion= models.CharField(max_length=500)
	idTrabajador = models.ForeignKey(Trabajadores, on_delete= models.CASCADE)
	def __str__(self):
		return self.idPermisoAusentismo

class PermisoDeAusentismo(models.Model):
	idPermisoAusentismo = models.AutoField(primary_key=True)
	fechaSalida = models.DateTimeField()
	#totalHoras = models.SmallIntegerField()
	motivo = models.SmallIntegerField()
	periodoIncapacidadInicial = models.DateField()
	periodoIncapacidadFinal = models.DateField()
	diasIncapacidad= models.SmallIntegerField()
	codigoDiagnostico = models.CharField(max_length=10)
	descripcion= models.CharField(max_length=500)
	idTrabajador = models.ForeignKey(Trabajadores, on_delete= models.CASCADE)
	def __str__(self):
		return self.idPermisoAusentismo

