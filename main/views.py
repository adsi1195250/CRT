from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from main.forms import trabajadoresForms
from main.models import Trabajadores


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

class ModificarTrabajdor(UpdateView):
    model = Trabajadores
    form_class = trabajadoresForms
    template_name = 'Trabajadores/trabajador_modal.html'
    success_url = reverse_lazy('listado_trabajadores')

class DetalleTrabajador(DetailView):
    model = Trabajadores
    template_name = 'Trabajadores/detalle_trabajador.html'

def registrarJornada(request):
    return render(request, 'registrarJornada/registrarJornada.html')
