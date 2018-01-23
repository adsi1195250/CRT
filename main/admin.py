from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
class TrabajadoresAdmin(admin.ModelAdmin):
	list_display=["__str__","id","nombres","cedula", "fechaIngreso", "fechaNacimiento", "edad", "administrador", "telefono", "CodigoBarras"]

"""
class Historial_IOAdmin(admin.ModelAdmin):
	list_display=["__str__","idHistorial",'horaEntrada',
	'horaSalida',
	'horaInicioDesayuno',
	'horaFinDesayuno',
	'horaInicioDescanso',
	'horaFinDescanso',
	'horaInicioPausasActivas',
	'horaFinPausasActivas',
	'horaInicioAlmuerzo',
	'horaFinAlmuerzo',
	'id_trabajadores',]
"""

class Historial_IOAdmin(admin.ModelAdmin):
	list_display=["__str__","idHistorial","accion_jornada","accion_jornada_hora","fecha" ,"hora","id_trabajadores"]




admin.site.register(Trabajadores, TrabajadoresAdmin),
admin.site.register(Historial_IO, Historial_IOAdmin),

