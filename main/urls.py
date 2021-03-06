
from django.conf.urls import url
from django.urls import include


from django.conf.urls import url, include

from main.views import *


urlpatterns = [
    url(r'^$', index, name='inicio'),
    url(r'^trabajadores/$', ListarTrabajador.as_view(), name="listado_trabajadores"),
    url(r'^crear_trabajador/$', CrearTrabajador, name="crear_trabajador"),
    url(r'^modificar_trabajador/(?P<pk>.+)/$',ModificarTrabajador.as_view(), name="modificar_trabajador"),
    url(r'^detalle_trabajador/(?P<pk>.+)/$',DetalleTrabajador.as_view(), name="detalle_trabajador"),
    url(r'^eliminar_trabajador/(?P<pk>.+)/$',EliminarTrabajador.as_view(), name="eliminar_trabajador"),
    url(r'^registrarJornada/$',buscar, name="registrarJornada"),
    url(r'^report/$', ReportePersonasPDF.as_view(), name="report"),
    #url(r'^report/(?P<value>\d+)/$', ReportePersonasPDF.as_view(), name="report"),
    #url(r'^registrarJornadaModal/$',registrarJornadaModal.as_view(), name="registrarJornadaModal"),
    url(r'^registrarJornadaModal/$',buscar, name="registrarJornadaModal"),
    #url(r'^codigo_barras/(?P<CodigoBarras>\d+)/$', ConsultaCodBarras, name='codigo_barras'),
    url(r'^codigo_barras/$', detail, name='detail'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^codigo_barras/(?P<CodigoBarras>\d+)/$', ConsultaCodBarras.as_view(), name='codigo_barras'),
    url(r'^listarInformeIO/$', listarInformeIO.as_view(), name="listado_informe"),
    url(r'^listar_festivos/$', ListarFestivos.as_view(), name="festivos"),
    url(r'^crear_festivos/$', CrearFestivos.as_view(), name="crear_festivos"),
    url(r'^modificar_festivos/(?P<pk>.+)/$', ModificarFestivos.as_view(), name="modificar_festivos"),
    url(r'^eliminar_festivos/(?P<pk>.+)/$', EliminarFestivos.as_view(), name="eliminar_festivos"),
    

]
