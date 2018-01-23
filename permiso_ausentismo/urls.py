from django.conf.urls import url
from django.urls import include

from main.views import *
from permiso_ausentismo.views import ListarPermisoAusentismo, CrearPermisoAusentismo, DetallePermisoAusentismo, \
    prueba_ajax, EliminarPermisoAusentismo, EditarPermisoAusentismo, report

urlpatterns = [
    url(r'^listar/$', ListarPermisoAusentismo, name="listado_permiso_ausentismo"),
    url(r'^crear/$', CrearPermisoAusentismo, name="crear_permiso_ausentismo"),
    #url(r'^detalle/(?P<pk>.+)/$',DetallePermisoAusentismo, name="detalle_permiso_ausentismo"),
    url(r'^detalle/(?P<pk>.+)/$',DetallePermisoAusentismo.as_view(), name="detalle_permiso_ausentismo"),
    url(r'^eliminar/(?P<pk>.+)/$',EliminarPermisoAusentismo.as_view(), name="eliminar_permiso_ausentismo"),
    url(r'^editar/(?P<pk>.+)/$',EditarPermisoAusentismo, name="editar_permiso_ausentismo"),
    url(r'^prueba_ajax/$', prueba_ajax, name="prueba_ajax"),
    url(r'^reporte/$',report,name='reporte')
]
