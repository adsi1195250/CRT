from django.conf.urls import url
from main.views import *

urlpatterns = [
    url(r'^$', index, name='inicio'),
    url(r'^trabajadores/$', ListarTrabajador.as_view(), name="listado_trabajadores"),
    url(r'^crear_trabajador/$', CrearTrabajador.as_view(), name="crear_trabajador"),
    url(r'^modificar_trabajador/(?P<pk>.+)/$',ModificarTrabajador.as_view(), name="modificar_trabajador"),
    url(r'^detalle_trabajador/(?P<pk>.+)/$',DetalleTrabajador.as_view(), name="detalle_trabajador"),
    url(r'^eliminar_trabajador/(?P<pk>.+)/$',EliminarTrabajador.as_view(), name="eliminar_trabajador"),
    url(r'^registrarJornada/',registrarJornada, name="registrarJornada"),
]
