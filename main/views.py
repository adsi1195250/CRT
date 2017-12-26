from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from main.forms import *
from main.models import *


def index(request):
    return render(request,'base.html')

class ListarTrabajador(ListView):
    model = Trabajadores
    template_name = 'Trabajadores/trabajadores.html'
    context_object_name = 'trabajador'

class CrearTrabajador(CreateView):
    template_name = 'Trabajadores/trabajador_modal.html'
    form_class = trabajadoresForms
    success_url = reverse_lazy('inicio')

class ModificarTrabajador(UpdateView):
    model = Trabajadores
    form_class = trabajadoresForms
    success_url = reverse_lazy('inicio')

class DetalleTrabajador(DetailView):
    model = Trabajadores
    template_name = 'Trabajadores/detalle_trabajador.html'

def registrarJornada(request):
    return render(request, 'registrarJornada/registrarJornada.html')

class registrarJornadaModal(CreateView):
    form_class = Historial_IOForms
    template_name =  'registrarJornada/registrarJornadaModal.html'
