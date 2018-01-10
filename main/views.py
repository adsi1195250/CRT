import urllib

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
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
    def get_queryset(self):
        q = Historial_IO.objects.filter(id_trabajadores__cedula=self.request.GET.get('cedula'))
        hoy = str(date.today().day)
        #filtro = Historial_IO.objects.filter(hora = hoy)
        #for f in q:
        #    fq = f.hora
        #    print(fq)
        a = {}
        j = {}
        ocho = {}
        nueve = {}
        self.b= []
        self.z= []
        for i in q:
            fq = i.fecha.day
            a['nombre'] = i.id_trabajadores.nombres
            if fq == 4:
                a[i.accion_jornada] = i.fecha
            elif fq==5:
                j[i.accion_jornada] = i.fecha
            elif fq==8:
                ocho[i.accion_jornada] = i.fecha
                ocho[i.accion_jornada_hora] = i.hora
            elif fq==9:
                nueve[i.accion_jornada] = i.fecha
                nueve[i.accion_jornada_hora] = i.hora
            #print("Here",fq)
            #if fq == 5:
            #   j[i.accion_jornada] = i.hora

        #print("None",i)
        self.b.append(a)
        self.b.append(j)
        self.b.append(ocho)
        self.b.append(nueve)
        # a.update(j)  //Combinar dos  diccionarios
        #print(self.z)
        #self.b.append(a)
        #print(self.b)
        # print(m)
        #print(self.b)
        a={}
        j={}
        return self.b

    """
    def get_context_data(self, **kwargs):
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
        q = 0
        context = {
            'context': super(listarInformeIO,self).get_context_data(**kwargs),
            'q': self.request.GET.get('cedula', ''),
        }
        #print("YESaaaaaaaaaaaaaa", context)
        filtro = Historial_IO.objects.filter(id_trabajadores__cedula = q)
        #filtro = Historial_IO.objects.filter(hora = hoy)
        #filtro = Historial_IO.objects.filter(hora__month = mes)
        #filtro = Historial_IO.objects.filter(hora__year = año)
        nb = Historial_IO.objects.all()
        kk = []
        for i in Historial_IO.objects.all():
            ia = i.id_trabajadores
            kk.append(i.id_trabajadores)
        print(context)
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
        print(context)
        context['b'] = self.b
        return context
    """

"""
class listarInformeIO(ListView):
    model = Historial_IO
    template_name = 'registrarJornada/listarInformeIO.html'

    def get_context_data(self, **kwargs):
        context = super(listarInformeIO, self).get_context_data(**kwargs)
        q = self.request.GET.get("cedula")
        context['cedula'] = q
        print(context)
        return context

    def get_queryset(self):
        queryset = Historial_IO.objects.filter(id_trabajadores__cedula=self.request.GET.get("cedula"))
        a = {}
        self.b = []
        for i in queryset:
            a['nombre'] = i.id_trabajadores.nombres
            a[i.accion_jornada] = i.hora
        self.b.append(a)
        a = {}

        print(self.b)
        #self.request.GET.get("browse")
        #print(queryset)
        return self.b

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
filtro = Historial_IO.objects.filter(id_trabajadores__cedula = '')
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


def registrarJornadaModal(request,pk):
    trabajador = Trabajadores.objects.all().first()
    pk = request.POST.get('CodigoBarras', '')
    print("valor:",pk)
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
    success = False
    if 'cb' in request.GET:
        q = request.GET['cb']
        #print(q)
        existe_colaborador=Trabajadores.objects.all()

        if not q:
            errors.append('Por favor introduce un termino de busqueda.')
            print(errors)
        else:
            trabajadores = Trabajadores.objects.filter(CodigoBarras=q)
            #modelo=Historial_IO.objects.all()
           #print(trabajadores.values()[0])
            if trabajadores.count() > 0:
                id = trabajadores.get().id
                #print(id)
            else:
                if not existe_colaborador.count() != 0:
                    errors.append('Por favor registre primero un Colaborador.')
                else:
                    errors.append('Colaborador no econtrado.')
            a = {}
            b= []
            cont=0
            for x in Trabajadores.objects.all():
                for i in Historial_IO.objects.all():
                    if x.cedula == i.id_trabajadores.cedula:
                        a['nombre'] = i.id_trabajadores.nombres
                        a[i.accion_jornada] = i.hora
                        cont=cont+1
                b.append(a)
                a={}
            #print(b)
            #print(cont)


            form = Historial_IOForms(request.POST or None, initial={"id_trabajadores": id,"accion_jornada_hora":'HEN'})

            #print(form.data)
            # form.data.get('id_trabajador',trabajador)
            cp = request.GET.copy()
            cp.pop('cb')
            #print(request.GET)
            
            #print(cp)

            #params = urllib.urlencode(cp)
            #print(params)
            context = {
                'form': form,
                'trabajadores': trabajadores,
                'query': q,
                'errors':errors,
            }

            if request.method == 'POST':
                if form.is_valid():
                    instance = form.save(commit=False)
                    accion_jornada = instance.accion_jornada
                    if accion_jornada == 'EN':
                        instance.accion_jornada_hora = 'HEN'
                    elif accion_jornada == 'SA':
                        instance.accion_jornada_hora = 'HSA'
                    elif accion_jornada == 'DYI':
                        instance.accion_jornada_hora = 'HDYI'
                    elif accion_jornada == 'DYF':
                        instance.accion_jornada_hora = 'HDYF'
                    elif accion_jornada == 'DCI':
                        instance.accion_jornada_hora = 'HDCI'
                    elif accion_jornada == 'DCF':
                        instance.accion_jornada_hora = 'HDCF'
                    elif accion_jornada == 'PAI':
                        instance.accion_jornada_hora = 'HPAI'
                    elif accion_jornada == 'PAF':
                        instance.accion_jornada_hora = 'HPAF'
                    elif accion_jornada == 'ALI':
                        instance.accion_jornada_hora = 'HALI'
                    elif accion_jornada == 'ALF':
                        instance.accion_jornada_hora = 'HALF'
                    #print(instance.accion_jornada_hora)
                    instance.save()
                    mensaje_exitoso=[]
                    mensaje_exitoso.append('Se ha registrado con exito !')
                    success=True
                    #return HttpResponseRedirect('',mensaje_exitoso)
                    return redirect('registrarJornada')
                    #return render(request,'registrarJornada/registrarJornada.html', {'mensaje': mensaje_exitoso})
                    # print(form)
                else:
                    print('no entra')
                    errors.append('La acción ya se encuntra registrada en este día.')

            return render(request, 'registrarJornada/registrarJornada.html',context)

    return render(request, 'registrarJornada/registrarJornada.html', {'errors': errors})
