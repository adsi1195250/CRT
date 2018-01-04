import urllib

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.shortcuts import redirect
from datetime import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


from main.forms import *
from main.models import *


def index(request):
    return render(request,'base.html')

class ListarTrabajador(ListView):
    model = Trabajadores
    template_name = 'Trabajadores/trabajadores.html'
    context_object_name = 'trabajador'

    """
    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion primero del  context
        context = super(ListarTrabajador, self).get_context_data(**kwargs)
        # Agregamos el publisher
        epa = 'Fucionaaaaaaaaa'
        context['epa'] = epa
        print(context)
        return context
    """
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


class listarInformeIO(ListView):
    model = Historial_IO
    template_name = 'registrarJornada/listarInformeIO.html'
    def get_context_data(self, **kwargs):
        context = super(listarInformeIO,self).get_context_data(**kwargs)
        hoy = str(date.today())
        mes = str(date.today().month)
        año = str(date.today().year)
        aa = '2018-01-03'
        #print("HOYYYYYYYY",hoy)
        if hoy == aa:
            pass
            #print("LO pase a string")
        else:
            pass
            #print("YESaaaaaaaaaaaaaa")
        filtro = Historial_IO.objects.filter(id_trabajadores__cedula = 'asdasd')
        #filtro = Historial_IO.objects.filter(hora = hoy)
        #filtro = Historial_IO.objects.filter(hora__month = mes)
        #filtro = Historial_IO.objects.filter(hora__year = año)
        nb = Historial_IO.objects.all()
        kk = []
        for i in Historial_IO.objects.all():
            ia = i.id_trabajadores
            kk.append(i.id_trabajadores)
        print(filtro)
        for i in nb:
            datee = i.hora
            #print (datee)
            #print ("  ----  ")
        #print("Hora ",nb)
        a = {}
        self.b= []
        for x in Trabajadores.objects.all():
            for i in filtro:
                if x.cedula == i.id_trabajadores.cedula:
                    a['nombre'] = i.id_trabajadores.nombres
                    a[i.accion_jornada] = i.hora
            self.b.append(a)
            a={}
        #print(self.b)
        context['b'] = self.b
        return context


"""
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
"""


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
    print('Codigo',codigo)
    return render(request, 'registrarJornada/registrarJornada.html')

"""
class registrarJornadaModal(CreateView):
    model = Historial_IO
    form_class = Historial_IOForms

    def get(self, request, *args, **kwargs):
        print(request)
        codigo = request.GET.get('CodigoBarras', '')
        print(codigo)
        return HttpResponse(request)
        #codigo = request.GET.get('CodigoBarras', '')

    def get_context_data(self, **kwargs):
        context = super(registrarJornadaModal, self).get_context_data(**kwargs)
        context['trabajador'] = Trabajadores.objects.all().first()
        print(context)
        return context
    template_name =  'registrarJornada/registrarJornadaModal.html'
"""


def registrarJornadaModal(request):
    trabajador = Trabajadores.objects.all().first()
    codigo = request.POST.get('CodigoBarras', '')
    print("valor:",codigo)
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


def buscar(request):
    errors = []
    id=-1
    if 'CodigoBarras' in request.GET:
        q = request.GET['CodigoBarras']
        print(q)
        if not q:
            errors.append('Por favor introduce un termino de busqueda.')
        else:
            trabajadores = Trabajadores.objects.filter(CodigoBarras=q)
            #modelo=Historial_IO.objects.all()
           #print(trabajadores.values()[0])
            if trabajadores.count() > 0:
                id = trabajadores.get().id
                #print(id)
            a = {}
            b= []
            cont=0
            for x in Trabajadores.objects.all():
                for i in Historial_IO.objects.all():
                    if x.cedula == i.id_trabajadores.cedula:
                        a['nombre'] = i.id_trabajadores.nombres
                        a[i.accion_jornada] = i.hora.ctime()
                        cont=cont+1
                b.append(a)
                a={}
            #print(b)
            #print(cont)
            form = Historial_IOForms(request.POST or None, initial={"id_trabajadores": id})
            # form.data.get('id_trabajador',trabajador)
            cp = request.GET.copy()
            #cp.pop('CodigoBarras')
            print(cp)
            #params = urllib.urlencode(cp)
            #print(params)
            context = {
                'form': form,
                'trabajadores': trabajadores,
                'query': q,
            }
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return redirect('registrarJornada')
                # print(form)
            return render(request, 'registrarJornada/registrarJornada.html',context)

    return render(request, 'registrarJornada/registrarJornada.html', {'errors': errors})
