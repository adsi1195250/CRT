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
	#edad = models.SmallIntegerField()
	administrador = models.BooleanField()
	telefono = models.CharField(max_length=11, blank=True,null=True)
	CodigoBarras = models.CharField(max_length=500)
	#foto = models.ImageField()
	def __str__(self):
		return '%s'%(self.nombres)

class dias_festivos(models.Model):
	id = models.AutoField(primary_key=True)
	festivos = models.DateField()

"""class dias_festivos(models.Model):
	id = models.AutoField(primary_key=True)
	festivos = models.DateField()
	def __str__(self):
		return '%s'%(self.festivos)
"""
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
		(DESAYUNO_INICIO, 'Inicio Desayuno'),
		(ALMUERZO_INICIO, 'Inicio Almuerzo'),
		(PAUSAS_ACTIVAS_INICIO, 'Inicio Pausas Activas'),
		(DESCANSO_INICIO, 'Inicio Descanso'),
		(SALIDA, 'Salida'),
		(DESAYUNO_FIN, 'Fin Desayuno'),
		(ALMUERZO_FIN, 'Fin Almuerzo'),
		(PAUSAS_ACTIVAS_FIN, 'Fin Pausas Activas'),
		(DESCANSO_FIN, 'Fin Descanso'),
	)
	accion_jornada = models.CharField(
		max_length=3,
		choices=ELECCIONES,
		default=ENTRADA,
	)
	HORA_ENTRADA = 'HEN'
	HORA_SALIDA = 'HSA'
	HORA_DESAYUNO_INICIO = 'HDYI'
	HORA_DESAYUNO_FIN = 'HDYF'
	HORA_DESCANSO_INICIO = 'HDCI'
	HORA_DESCANSO_FIN = 'HDCF'
	HORA_PAUSAS_ACTIVAS_INICIO = 'HPAI'
	HORA_PAUSAS_ACTIVAS_FIN = 'HPAF'
	HORA_ALMUERZO_INICIO = 'HALI'
	HORA_ALMUERZO_FIN = 'HALF'
	ELECCIONES_HORA = (
		(HORA_ENTRADA, 'Hora Entrada'),
		(HORA_DESAYUNO_INICIO, 'Hora Inicio Desayuno'),
		(HORA_ALMUERZO_INICIO, 'Hora Inicio Almuerzo'),
		(HORA_PAUSAS_ACTIVAS_INICIO, 'Hora Inicio Pausas Activas'),
		(HORA_DESCANSO_INICIO, 'Hora Inicio Descanso'),
		(HORA_SALIDA, 'Hora Salida'),
		(HORA_DESAYUNO_FIN, 'Hora Fin Desayuno'),
		(HORA_ALMUERZO_FIN, 'Hora Fin Almuerzo'),
		(HORA_PAUSAS_ACTIVAS_FIN, 'Hora Fin Pausas Activas'),
		(HORA_DESCANSO_FIN, 'Hora Fin Descanso'),
	)
	accion_jornada_hora = models.CharField(
		max_length=4,
		choices=ELECCIONES_HORA,
		default= HORA_ENTRADA,
	)
	fecha = models.DateField(auto_now_add=True)
	hora = models.TimeField(auto_now_add=True)
	id_trabajadores = models.ForeignKey(Trabajadores,on_delete=models.CASCADE)
	def __str__(self):
		return '%s'%self.idHistorial

