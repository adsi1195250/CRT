from django.contrib import admin
from .models import *

# Register your models here.
class TrabajadoresAdmin(admin.ModelAdmin):
	list_display=["__str__","id","nombres","cedula", "fechaIngreso", "fechaNacimiento", "edad", "cargo", "telefono", "foto"]

admin.site.register(Trabajadores, TrabajadoresAdmin)
