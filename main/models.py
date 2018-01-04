from django.db import models
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, date, time, timedelta
from time import gmtime, strftime

# Create your models here.
class Trabajadores(models.Model):
	id = models.AutoField(primary_key=True)
	nombres = models.CharField(max_length=255)
	cedula = models.CharField(max_length=11)
	fechaIngreso = models.DateField()
	fechaNacimiento = models.DateField()
	edad = models.SmallIntegerField()
	administrador = models.BooleanField()
	telefono = models.CharField(max_length=11, blank=True,null=True)
	CodigoBarras = models.CharField(max_length=500)
	#foto = models.ImageField()
	def __str__(self):
		return '%s'%(self.nombres)

"""
class CodigoBarras(models.Model):
	idCodigoBarras = models.AutoField(primary_key=True)
	CodigoBarras = models.CharField(max_length=200)
	idTrabajadores = models.ForeignKey(Trabajadores, on_delete= models.CASCADE)
	def __str__(self):
		return self.CodigoBarras
"""

"""
class Historial_IO(models.Model):
	idHistorial = models.AutoField(primary_key=True)
	horaEntrada =  models.BooleanField(default=False)
	horaSalida = models.BooleanField(default=True)
	horaInicioDesayuno = models.DateTimeField()
	horaFinDesayuno = models.DateTimeField()
	horaInicioDescanso = models.DateTimeField()
	horaFinDescanso = models.DateTimeField()
	horaInicioPausasActivas = models.DateTimeField()
	horaFinPausasActivas = models.DateTimeField()
	horaInicioAlmuerzo = models.DateTimeField()
	horaFinAlmuerzo = models.DateTimeField()
	id_trabajadores = models.ForeignKey(Trabajadores,on_delete=models.CASCADE)
	def __str__(self):
		return '%s'%self.idHistorial
"""

class Historial_IO(models.Model):
	idHistorial = models.AutoField(primary_key=True)
	ENTRADA = 'EN'
	SALIDA = 'SA'
	DESAYUNO_INICIO = 'DYI'
	DESAYUNO_FIN = 'DYF'
	DESCANSO_INICIO = 'DCI'
	DESCANSO_FIN = 'DCF'
	PAUSAS_ACTIVAS_INICIO = 'PAI'
	PAUSAS_ACTIVAS_FIN = 'PAF'
	ALMUERZO_INICIO = 'ALI'
	ALMUERZO_FIN = 'ALF'
	ELECCIONES = (
		(ENTRADA, 'Entrada'),
		(SALIDA, 'Salida'),
		(DESAYUNO_INICIO, 'Inicio Desayuno'),
		(DESAYUNO_FIN, 'Fin Desayuno'),
		(DESCANSO_INICIO, 'Inicio Descanso'),
		(DESCANSO_FIN, 'Fin Descanso'),
		(PAUSAS_ACTIVAS_INICIO, 'Inicio Pausas Activas'),
		(PAUSAS_ACTIVAS_FIN, 'Fin Pausas Activas'),
		(ALMUERZO_INICIO, 'Inicio Almuerzo'),
		(ALMUERZO_FIN, 'Fin Almuerzo'),
	)
	accion_jornada = models.CharField(
		max_length=3,
		choices=ELECCIONES,
		default=ENTRADA,
	)
	hora = models.DateField(auto_now_add=True)
	id_trabajadores = models.ForeignKey(Trabajadores,on_delete=models.CASCADE)
	def __str__(self):
		return '%s'%self.idHistorial


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
		return '%s'%self.idPermisoAusentismo
