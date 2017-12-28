from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from datetime import datetime, date, time, timedelta

from main.forms import *
from main.models import *


def index(request):
    return render(request,'base.html')

class ListarTrabajador(ListView):
    model = Trabajadores
    template_name = 'Trabajadores/trabajadores.html'
    context_object_name = 'trabajador'

class CrearTrabajador(CreateView):
    model = Trabajadores
    template_name = 'Trabajadores/trabajador_modal.html'
    form_class = trabajadoresForms
    success_url = reverse_lazy('listado_trabajadores')

class ModificarTrabajador(UpdateView):
    model = Trabajadores
    form_class = trabajadoresForms
    template_name = 'Trabajadores/trabajador_modal.html'
    success_url = reverse_lazy('listado_trabajadores')

class DetalleTrabajador(DetailView):
    model = Trabajadores
    template_name = 'Trabajadores/detalle_trabajador.html'

class EliminarTrabajador(DeleteView):
    model = Trabajadores
    template_name = 'Trabajadores/trabajador_eliminar.html'
    success_url = reverse_lazy('listado_trabajadores')

def registrarJornada(request):
    #all_trab = Trabajadores.objects.all()
    codigoBarritas = request.GET.get('CodigoBarras', '')
    #print(codigoBarritas)
    all_trab1 = Trabajadores.objects.filter(CodigoBarras=codigoBarritas)
    #print(all_trab1)
    ahora = datetime.now()  # Obtiene fecha y hora actual
    print("Fecha y Hora:", ahora)
    return render(request, 'registrarJornada/registrarJornada.html')

class registrarJornadaModal(CreateView):
    model = Historial_IO
    form_class = Historial_IOForms
    template_name =  'registrarJornada/registrarJornadaModal.html'
