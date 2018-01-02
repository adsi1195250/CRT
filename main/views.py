from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from datetime import datetime, date, time, timedelta
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

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


cont=0
class listarInformeIO(ListView):
    model = Historial_IO
    template_name = 'registrarJornada/listarInformeIO.html'
    trabajador = Trabajadores.objects.all()
    boolean = False
    #dica = ['nombre', 'horaEnt', 'horaAlm', 'horaSal']
    dica = []
    trabajador2 = []
    for i in trabajador:
        for Historial_IO in model.objects.all():
            if i == Historial_IO.id_trabajadores:
                boolean = True
                dic = {'nombres':i.nombres ,'accion' : Historial_IO.accion_jornada, 'hora' : Historial_IO.hora}
                dica.append(Historial_IO.accion_jornada)
            else:
                trabajador2 = i


        #dic = { Historial_IO.id_trabajadores : Historial_IO.accion_jornada }


            #print(trabajadores.nombres)
            #print(Historial_IO.id_trabajadores, "---")
    print(dica)
    print(trabajador2)


def registrarJornada(request):

    #all_trab = Trabajadores.objects.all()
    codigoBarritas = request.GET.get('CodigoBarras', '')
    #print(codigoBarritas)
    all_trab1 = Trabajadores.objects.filter(CodigoBarras=codigoBarritas)
    print("xsaddsa", all_trab1)
    ahora = datetime.now()  # Obtiene fecha y hora actual
    #print("Fecha y Hora:", ahora)
    codigo = request.GET.get('CodigoBarras', '')
    if codigo:
        return render(request,'Trabajadores/detalle_trabajador.html')
    print(codigo)
    return render(request, 'registrarJornada/registrarJornada.html')

"""
class registrarJornadaModal(CreateView):
    model = Trabajadores
    form_class = Historial_IOForms
    template_name =  'registrarJornada/registrarJornadaModal.html'
"""

def registrarJornadaModal(request):
    trabajador = Trabajadores.objects.all().first()
    form=Historial_IOForms(request.POST or None,initial={"id_trabajadores": trabajador})
    #form.data.get('id_trabajador',trabajador)

    context={
        'form':form,
        'trabajador':trabajador,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        print(instance)
        instance.save()
        return render(request, 'registrarJornada/registrarJornada.html', context)
        #print(form)
    return render(request, 'registrarJornada/registrarJornadaModal.html',context)


def detail(request, CodigoBarras):
    print("dfsef")
    try:
        p = Trabajadores.objects.get(CodigoBarras=CodigoBarras)
    except Trabajadores.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'Trabajadores/detalle_trabajador.html', {'poll': p})
