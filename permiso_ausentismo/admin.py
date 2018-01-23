from django.contrib import admin

# Register your models here.
from permiso_ausentismo.models import PermisoAusentismo


class PermisoAusentismoAdmin(admin.ModelAdmin):
	list_display=["__str__","idPermisoAusentismo","mes_evento","tipo_evento","periodoIncapacidadInicial","periodoIncapacidadFinal","prorroga", "totalDiasIncapacidad","diasCargados", "codigoDiagnostico", "observaciones", "idTrabajador"]

admin.site.register(PermisoAusentismo, PermisoAusentismoAdmin)