from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
class TrabajadoresAdmin(admin.ModelAdmin):
	list_display=["__str__","id","nombres","cedula", "fechaIngreso", "fechaNacimiento", "edad", "area", "telefono", "CodigoBarras"]


class Historial_IOAdmin(admin.ModelAdmin):
	list_display=["__str__","idHistorial","horaEntrada","horaSalida","horaDesayuno", "horaDescanso", "horaPausasActivas", "horaAlmuerzo"]

class PermisoAusentismoAdmin(admin.ModelAdmin):
	list_display=["__str__","idPermisoAusentismo","fechaSalida","motivo","periodoIncapacidadInicial","periodoIncapacidadFinal", "diasIncapacidad", "codigoDiagnostico", "descripcion", "idTrabajador"]


admin.site.register(Trabajadores, TrabajadoresAdmin),
admin.site.register(Historial_IO, Historial_IOAdmin),
admin.site.register(PermisoAusentismo, PermisoAusentismoAdmin)
