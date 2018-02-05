import urllib
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.shortcuts import redirect
from datetime import *
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from django.http import HttpResponse
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image, SimpleDocTemplate
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import *
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

class ListarFestivos(ListView):
    model = dias_festivos
    template_name = 'Festivos/festivos.html'
    context_object_name = 'dias_festivos'
    

def CrearTrabajador(request):
    form = trabajadoresForms(request.POST or None)
    context = {
        'form':form,
    }
    if form.is_valid():
        instace = form.save(commit=False)
        instace.save()
        return redirect('listado_trabajadores')

    return render(request,'Trabajadores/form_trabajadores.html',context)
    
class CrearFestivos(CreateView):
    model = dias_festivos
    form_class = Dias_FestivosForms
    template_name = 'Festivos/crear_festivos.html'
    success_url = reverse_lazy('listado_informe')
    
class ModificarFestivos(UpdateView):
    model = dias_festivos
    form_class = Dias_FestivosForms
    template_name = 'Festivos/crear_festivos.html'
    success_url = reverse_lazy('listado_informe')    

class EliminarFestivos(DeleteView):
    model = dias_festivos
    template_name = 'Festivos/eliminar_festivos.html'
    success_url = reverse_lazy('listado_informe')    

class ModificarTrabajador(UpdateView):
    model = Trabajadores
    form_class = trabajadoresForms
    template_name = 'Trabajadores/form_trabajadores.html'
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
        errors = {}
        hoy = str(date.today().month)
        #q = Historial_IO.objects.filter(id_trabajadores__cedula=self.request.GET.get('cedula'))
        #filtroMes = Historial_IO.objects.filter(fecha__month=hoy)
        #print("Filtro", filtroMes, hoy)
        if 'cedula' in self.request.GET and 'mes' in self.request.GET:
            qa = self.request.GET['cedula']
            qames = self.request.GET['mes']
            existe_colaborador=Trabajadores.objects.all()
            Historial = Historial_IO.objects.all()
            #print("wames" ,existe_colaborador)
            if not qa or not qames:
                errors['error'] =('Por favor ingrese todos los datos.')
            else:
                print(errors)
                q = Historial_IO.objects.filter(id_trabajadores__cedula=self.request.GET.get('cedula'))
                jaa = Trabajadores.objects.filter(cedula=self.request.GET.get('cedula'))
                filtroMes = Historial_IO.objects.filter(fecha__month=self.request.GET.get('mes'))
                #modelo=Historial_IO.objects.all()
                #print(trabajadores.values()[0])
                if q.count() > 0 and filtroMes.count() > 0:
                    #id = q.get().id
                    print(id)
                #else:
                #    if not existe_colaborador.count() != 0:
                #        errors['error'] =('Por favor registre primero un Colaborador.')
                #    else:
                #        errors['error'] =('Colaborador no encontrado.')
                #        #print(errors)

                lis = []
                for p in q:
                    lis.append(p.fecha.month)
                kaa = {}
                for z in jaa:
                    kaa['nombres'] = z
                
                print(kaa, "NOMBRESSS")

                ja = False
                if int(qames) in lis:
                    ja = True
                else:
                    errors['error'] = ('El Colaborador no tiene registro en este fecha.')
                    ja = False


                lis_cedula = []
                for j in existe_colaborador:
                    lis_cedula.append(j.cedula)

                for k in lis_cedula:
                    #print(lis_cedula, qa, "QSA")
                    if qa in lis_cedula and not q:
                        errors['error'] = ('El Colaborador no tiene ningún registro.')
                        #print("Colaborar existe, pero no tiene registro")
                    elif not qa in lis_cedula:
                        errors['error'] =('Colaborador no encontrado, Por favor regístrelo.')
                        #print("Colaborar no existe")
                print(errors)

                """for p in Historial:
                    print("Month" ,p.fecha.month)
                    print("a" ,qames)
                    if qames != p.fecha.month:
                        errors['error'] = ('El Colaborador No tiene registro en este fecha.')
                """
                #print("Naddaaa",errors)
                #filtro = Historial_IO.objects.filter(hora = hoy)
                #for f in q:
                #    fq = f.hora
                #    print(fq)
                a = {}
                j = {}
                uno = {}
                dos = {}
                tres = {}
                cuatro={}
                cinco={}
                seis={}
                siete={}
                ocho = {}
                nueve = {}
                diez={}
                once={}
                doce = {}
                trece = {}
                catorce = {}
                quince = {}
                dieciseis = {}
                diecisiete = {}
                dieciocho = {}
                diecinueve = {}
                veinte = {}
                veintiuno = {}
                veintidos = {}
                veintitres = {}
                veinticuatro={}
                veinticinco = {}
                veintiseis = {}
                veintisiete = {}
                veintiocho = {}
                veintinueve = {}
                treinta = {}
                treintauno = {}
                self.b= []
                hoy = datetime.today()  # Asigna fecha-hora
                for i in q:
                    mes1 = i
                    for mes in filtroMes:
                        if mes == mes1:
                            if mes.fecha.year == hoy.year:
                                fq = i.fecha.day
                                #fqmes = i.fecha.month
                                a['nombre'] = i.id_trabajadores.nombres
                                a['cedula'] = i.id_trabajadores.cedula
                                a['mes'] = mes.fecha.month
                                a['year'] = mes.fecha.year
                                #if fqmes == 1:
                                if mes.fecha.day == 1 and fq == 1:
                                    uno[i.accion_jornada] = i.fecha
                                    uno[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 2 and fq ==2:
                                    dos[i.accion_jornada] = i.fecha
                                    dos[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 3 and fq ==3:
                                    tres[i.accion_jornada] = i.fecha
                                    tres[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 4 and fq ==4:
                                    cuatro[i.accion_jornada] = i.fecha
                                    cuatro[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day ==5 and fq ==5:
                                    cinco[i.accion_jornada] = i.fecha
                                    cinco[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 6 and fq ==6:
                                    seis[i.accion_jornada] = i.fecha
                                    seis[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 7 and fq ==7:
                                    siete[i.accion_jornada] = i.fecha
                                    siete[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==8 and fq ==8:
                                    ocho[i.accion_jornada] = i.fecha
                                    ocho[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==9 and fq ==9:
                                    nueve[i.accion_jornada] = i.fecha
                                    nueve[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 10 and fq==10:
                                    diez[i.accion_jornada] = i.fecha
                                    diez[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 11 and fq == 11:
                                    once[i.accion_jornada] = i.fecha
                                    once[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==12 and fq ==12:
                                    doce[i.accion_jornada] = i.fecha
                                    doce[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==13 and fq ==13:
                                    trece[i.accion_jornada] = i.fecha
                                    trece[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==14 and fq ==14:
                                    catorce[i.accion_jornada] = i.fecha
                                    catorce[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 15 and fq ==15:
                                    quince[i.accion_jornada] = i.fecha
                                    quince[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 16 and fq ==16:
                                    dieciseis[i.accion_jornada] = i.fecha
                                    dieciseis[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 17 and fq ==17:
                                    diecisiete[i.accion_jornada] = i.fecha
                                    diecisiete[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 18 and fq ==18:
                                    dieciocho[i.accion_jornada] = i.fecha
                                    dieciocho[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==19 and fq ==19:
                                    diecinueve[i.accion_jornada] = i.fecha
                                    diecinueve[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 20 and fq ==20:
                                    veinte[i.accion_jornada] = i.fecha
                                    veinte[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 21 and fq ==21:
                                    veintiuno[i.accion_jornada] = i.fecha
                                    veintiuno[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==22 and fq ==22:
                                    veintidos[i.accion_jornada] = i.fecha
                                    veintidos[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==23 and fq ==23:
                                    veintitres[i.accion_jornada] = i.fecha
                                    veintitres[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 24 and fq ==24:
                                    veinticuatro[i.accion_jornada] = i.fecha
                                    veinticuatro[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day == 25 and fq ==25:
                                    veinticinco[i.accion_jornada] = i.fecha
                                    veinticinco[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==26 and fq ==26:
                                    veintiseis[i.accion_jornada] = i.fecha
                                    veintiseis[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==27 and fq ==27:
                                    veintisiete[i.accion_jornada] = i.fecha
                                    veintisiete[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==28 and fq ==28:
                                    veintiocho[i.accion_jornada] = i.fecha
                                    veintiocho[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==29 and fq ==29:
                                    veintinueve[i.accion_jornada] = i.fecha
                                    veintinueve[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==30 and fq ==30:
                                    treinta[i.accion_jornada] = i.fecha
                                    treinta[i.accion_jornada_hora] = i.hora
                                elif mes.fecha.day==31 and fq ==31:
                                    treintauno[i.accion_jornada] = i.fecha
                                    treintauno[i.accion_jornada_hora] = i.hora
                self.b.append(a)
                self.b.append(uno)
                self.b.append(dos)
                self.b.append(tres)
                self.b.append(cuatro)
                self.b.append(cinco)
                self.b.append(seis)
                self.b.append(siete)
                self.b.append(ocho)
                self.b.append(nueve)
                self.b.append(diez)
                self.b.append(once)
                self.b.append(doce)
                self.b.append(trece)
                self.b.append(catorce)
                self.b.append(quince)
                self.b.append(dieciseis)
                self.b.append(diecisiete)
                self.b.append(dieciocho)
                self.b.append(diecinueve)
                self.b.append(veinte)
                self.b.append(veintiuno)
                self.b.append(veintidos)
                self.b.append(veintitres)
                self.b.append(veinticuatro)
                self.b.append(veinticinco)
                self.b.append(veintiseis)
                self.b.append(veintisiete)
                self.b.append(veintiocho)
                self.b.append(veintinueve)
                self.b.append(treinta)
                self.b.append(treintauno)
                self.b.append(errors)
                self.b.append(kaa)
                # a.update(j)  //Combinar dos  diccionarios
                #print(self.z)
                #self.b.append(a)
                #print(self.b)
                # print(m)
                #print("Selfbaa" ,self.b)
                a={}
                j={}
                return self.b
            self.b = []
            self.b.append(errors)
            return self.b

class ReportePersonasPDF(View):
    def cabecera(self,pdf):
        a = {}
        b= []
        q = Historial_IO.objects.filter(id_trabajadores__cedula=self.request.GET.get('cedula'))
        filtroMes = Historial_IO.objects.filter(fecha__month = self.request.GET.get('mes'))
        filtroMes1 = self.request.GET['mes1']
        año = self.request.GET['año']
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.STATIC_ROOT+'/img/index.jpg'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 650, 120, 80,preserveAspectRatio=True)
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 25)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(300, 700, u"Siete Colinas S.A.S")
        pdf.line(300, 692, 545, 692)
        pdf.setFont("Helvetica", 14)
        pdf.drawString(300, 673 , u"REPORTE DE REGISTRO JORNADA")
        pdf.setFont('Helvetica-Bold', 12)
        pdf.drawString(355, 652 , u"MES: "+ filtroMes1 + " " + año)
        pdf.setFont("Helvetica", 18)
        pdf.drawString(720, 710, u"Colaborador:")
        pdf.setFont("Helvetica", 15)
        #print(filtroMes)
        for jh in q:
            jnombre = jh.id_trabajadores.nombres
            jcedula = jh.id_trabajadores.cedula
        pdf.drawString(680,687, jnombre)
        pdf.setFont("Helvetica", 14)
        pdf.drawString(740, 668, u"Cédula:")
        pdf.setFont("Helvetica", 15)
        pdf.drawString(722,650, jcedula)

    def tabla(self,pdf,y):

        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Día', 'Entrada', 'Desayuno', 'Fin desayuno', 'Almuerzo', 'Fin Almuerzo', 'Pausas Activas', 'Fin pausas activas', 'Descanso', 'Fin Descanso', 'Salida', 'Horas Trabajadas', 'Firma',)
        #Creamos una lista de tuplas que van a contener a las personas
        q = Historial_IO.objects.filter(id_trabajadores__cedula=self.request.GET.get('cedula'))
        filtroMes = Historial_IO.objects.filter(fecha__month=self.request.GET.get('mes'))
        festivos = dias_festivos.objects.all()
        a = {}
        j = {}
        uno = {}
        dos = {}
        tres = {}
        cuatro={}
        cinco={}
        seis={}
        siete={}
        ocho = {}
        nueve = {}
        diez={}
        once={}
        doce = {}
        trece = {}
        catorce = {}
        quince = {}
        dieciseis = {}
        diecisiete = {}
        dieciocho = {}
        diecinueve = {}
        veinte = {}
        veintiuno = {}
        veintidos = {}
        veintitres = {}
        veinticuatro={}
        veinticinco = {}
        veintiseis = {}
        veintisiete = {}
        veintiocho = {}
        veintinueve = {}
        treinta = {}
        treintauno = {}

        uno['EN'] = date(13, 1, 2)
        uno['HEN'] = time(00, 00, 00)
        uno['HDYI'] = time(00, 00, 00)
        uno['HDYF'] = time(00, 00, 00)
        uno['HALI'] = time(00, 00, 00)
        uno['HALF'] = time(00, 00, 00)
        uno['HPAI'] = time(00, 00, 00)
        uno['HPAF'] = time(00, 00, 00)
        uno['HDCI'] = time(00, 00, 00)
        uno['HDCF'] = time(00, 00, 00)
        uno['HSA'] = time(00, 00, 00)

        dos['EN'] = date(13, 1, 1)
        dos['HEN'] = time(00, 00, 00)
        dos['HDYI'] = time(00, 00, 00)
        dos['HDYF'] = time(00, 00, 00)
        dos['HALI'] = time(00, 00, 00)
        dos['HALF'] = time(00, 00, 00)
        dos['HPAI'] = time(00, 00, 00)
        dos['HPAF'] = time(00, 00, 00)
        dos['HDCI'] = time(00, 00, 00)
        dos['HDCF'] = time(00, 00, 00)
        dos['HSA'] = time(00, 00, 00)


        tres['EN'] = date(13, 1, 1)
        tres['HEN'] = time(00, 00, 00)
        tres['HDYI'] = time(00, 00, 00)
        tres['HDYF'] = time(00, 00, 00)
        tres['HALI'] = time(00, 00, 00)
        tres['HALF'] = time(00, 00, 00)
        tres['HPAI'] = time(00, 00, 00)
        tres['HPAF'] = time(00, 00, 00)
        tres['HDCI'] = time(00, 00, 00)
        tres['HDCF'] = time(00, 00, 00)
        tres['HSA'] = time(00, 00, 00)

        cuatro['EN'] = date(13, 1, 1)
        cuatro['HEN'] = time(00, 00, 00)
        cuatro['HDYI'] = time(00, 00, 00)
        cuatro['HDYF'] = time(00, 00, 00)
        cuatro['HALI'] = time(00, 00, 00)
        cuatro['HALF'] = time(00, 00, 00)
        cuatro['HPAI'] = time(00, 00, 00)
        cuatro['HPAF'] = time(00, 00, 00)
        cuatro['HDCI'] = time(00, 00, 00)
        cuatro['HDCF'] = time(00, 00, 00)
        cuatro['HSA'] = time(00, 00, 00)


        cinco['EN'] = date(13, 1, 1)
        cinco['HEN'] = time(00, 00, 00)
        cinco['HDYI'] = time(00, 00, 00)
        cinco['HDYF'] = time(00, 00, 00)
        cinco['HALI'] = time(00, 00, 00)
        cinco['HALF'] = time(00, 00, 00)
        cinco['HPAI'] = time(00, 00, 00)
        cinco['HPAF'] = time(00, 00, 00)
        cinco['HDCI'] = time(00, 00, 00)
        cinco['HDCF'] = time(00, 00, 00)
        cinco['HSA'] = time(00, 00, 00)

        seis['EN'] = date(13, 1, 1)
        seis['HEN'] = time(00, 00, 00)
        seis['HDYI'] = time(00, 00, 00)
        seis['HDYF'] = time(00, 00, 00)
        seis['HALI'] = time(00, 00, 00)
        seis['HALF'] = time(00, 00, 00)
        seis['HPAI'] = time(00, 00, 00)
        seis['HPAF'] = time(00, 00, 00)
        seis['HDCI'] = time(00, 00, 00)
        seis['HDCF'] = time(00, 00, 00)
        seis['HSA'] = time(00, 00, 00)

        siete['EN'] = date(13, 1, 1)
        siete['HEN'] = time(00, 00, 00)
        siete['HDYI'] = time(00, 00, 00)
        siete['HDYF'] = time(00, 00, 00)
        siete['HALI'] = time(00, 00, 00)
        siete['HALF'] = time(00, 00, 00)
        siete['HPAI'] = time(00, 00, 00)
        siete['HPAF'] = time(00, 00, 00)
        siete['HDCI'] = time(00, 00, 00)
        siete['HDCF'] = time(00, 00, 00)
        siete['HSA'] = time(00, 00, 00)

        ocho['EN'] = date(13, 1, 1)
        ocho['HEN'] = time(00, 00, 00)
        ocho['HDYI'] = time(00, 00, 00)
        ocho['HDYF'] = time(00, 00, 00)
        ocho['HALI'] = time(00, 00, 00)
        ocho['HALF'] = time(00, 00, 00)
        ocho['HPAI'] = time(00, 00, 00)
        ocho['HPAF'] = time(00, 00, 00)
        ocho['HDCI'] = time(00, 00, 00)
        ocho['HDCF'] = time(00, 00, 00)
        ocho['HSA'] = time(00, 00, 00)

        nueve['EN'] = date(13, 1, 1)
        nueve['HEN'] = time(00, 00, 00)
        nueve['HDYI'] = time(00, 00, 00)
        nueve['HDYF'] = time(00, 00, 00)
        nueve['HALI'] = time(00, 00, 00)
        nueve['HALF'] = time(00, 00, 00)
        nueve['HPAI'] = time(00, 00, 00)
        nueve['HPAF'] = time(00, 00, 00)
        nueve['HDCI'] = time(00, 00, 00)
        nueve['HDCF'] = time(00, 00, 00)
        nueve['HSA'] = time(00, 00, 00)

        diez['EN'] = date(13, 1, 1)
        diez['HEN'] = time(00, 00, 00)
        diez['HDYI'] = time(00, 00, 00)
        diez['HDYF'] = time(00, 00, 00)
        diez['HALI'] = time(00, 00, 00)
        diez['HALF'] = time(00, 00, 00)
        diez['HPAI'] = time(00, 00, 00)
        diez['HPAF'] = time(00, 00, 00)
        diez['HDCI'] = time(00, 00, 00)
        diez['HDCF'] = time(00, 00, 00)
        diez['HSA'] = time(00, 00, 00)

        once['EN'] = date(13, 1, 1)
        once['HEN'] = time(00, 00, 00)
        once['HDYI'] = time(00, 00, 00)
        once['HDYF'] = time(00, 00, 00)
        once['HALI'] = time(00, 00, 00)
        once['HALF'] = time(00, 00, 00)
        once['HPAI'] = time(00, 00, 00)
        once['HPAF'] = time(00, 00, 00)
        once['HDCI'] = time(00, 00, 00)
        once['HDCF'] = time(00, 00, 00)
        once['HSA'] = time(00, 00, 00)

        doce['EN'] = date(13, 1, 1)
        doce['HEN'] = time(00, 00, 00)
        doce['HDYI'] = time(00, 00, 00)
        doce['HDYF'] = time(00, 00, 00)
        doce['HALI'] = time(00, 00, 00)
        doce['HALF'] = time(00, 00, 00)
        doce['HPAI'] = time(00, 00, 00)
        doce['HPAF'] = time(00, 00, 00)
        doce['HDCI'] = time(00, 00, 00)
        doce['HDCF'] = time(00, 00, 00)
        doce['HSA'] = time(00, 00, 00)

        trece['EN'] = date(13, 1, 1)
        trece['HEN'] = time(00, 00, 00)
        trece['HDYI'] = time(00, 00, 00)
        trece['HDYF'] = time(00, 00, 00)
        trece['HALI'] = time(00, 00, 00)
        trece['HALF'] = time(00, 00, 00)
        trece['HPAI'] = time(00, 00, 00)
        trece['HPAF'] = time(00, 00, 00)
        trece['HDCI'] = time(00, 00, 00)
        trece['HDCF'] = time(00, 00, 00)
        trece['HSA'] = time(00, 00, 00)


        catorce['EN'] = date(13, 1, 1)
        catorce['HEN'] = time(00, 00, 00)
        catorce['HDYI'] = time(00, 00, 00)
        catorce['HDYF'] = time(00, 00, 00)
        catorce['HALI'] = time(00, 00, 00)
        catorce['HALF'] = time(00, 00, 00)
        catorce['HPAI'] = time(00, 00, 00)
        catorce['HPAF'] = time(00, 00, 00)
        catorce['HDCI'] = time(00, 00, 00)
        catorce['HDCF'] = time(00, 00, 00)
        catorce['HSA'] = time(00, 00, 00)

        quince['EN'] = date(13, 1, 1)
        quince['HEN'] = time(00, 00, 00)
        quince['HDYI'] = time(00, 00, 00)
        quince['HDYF'] = time(00, 00, 00)
        quince['HALI'] = time(00, 00, 00)
        quince['HALF'] = time(00, 00, 00)
        quince['HPAI'] = time(00, 00, 00)
        quince['HPAF'] = time(00, 00, 00)
        quince['HDCI'] = time(00, 00, 00)
        quince['HDCF'] = time(00, 00, 00)
        quince['HSA'] = time(00, 00, 00)


        dieciseis['EN'] = date(13, 1, 1)
        dieciseis['HEN'] = time(00, 00, 00)
        dieciseis['HDYI'] = time(00, 00, 00)
        dieciseis['HDYF'] = time(00, 00, 00)
        dieciseis['HALI'] = time(00, 00, 00)
        dieciseis['HALF'] = time(00, 00, 00)
        dieciseis['HPAI'] = time(00, 00, 00)
        dieciseis['HPAF'] = time(00, 00, 00)
        dieciseis['HDCI'] = time(00, 00, 00)
        dieciseis['HDCF'] = time(00, 00, 00)
        dieciseis['HSA'] = time(00, 00, 00)

        diecisiete['EN'] = date(13, 1, 1)
        diecisiete['HEN'] = time(00, 00, 00)
        diecisiete['HDYI'] = time(00, 00, 00)
        diecisiete['HDYF'] = time(00, 00, 00)
        diecisiete['HALI'] = time(00, 00, 00)
        diecisiete['HALF'] = time(00, 00, 00)
        diecisiete['HPAI'] = time(00, 00, 00)
        diecisiete['HPAF'] = time(00, 00, 00)
        diecisiete['HDCI'] = time(00, 00, 00)
        diecisiete['HDCF'] = time(00, 00, 00)
        diecisiete['HSA'] = time(00, 00, 00)

        dieciocho['EN'] = date(13, 1, 1)
        dieciocho['HEN'] = time(00, 00, 00)
        dieciocho['HDYI'] = time(00, 00, 00)
        dieciocho['HDYF'] = time(00, 00, 00)
        dieciocho['HALI'] = time(00, 00, 00)
        dieciocho['HALF'] = time(00, 00, 00)
        dieciocho['HPAI'] = time(00, 00, 00)
        dieciocho['HPAF'] = time(00, 00, 00)
        dieciocho['HDCI'] = time(00, 00, 00)
        dieciocho['HDCF'] = time(00, 00, 00)
        dieciocho['HSA'] = time(00, 00, 00)

        diecinueve['EN'] = date(13, 1, 1)
        diecinueve['HEN'] = time(00, 00, 00)
        diecinueve['HDYI'] =time(00, 00, 00)
        diecinueve['HDYF'] =time(00, 00, 00)
        diecinueve['HALI'] =time(00, 00, 00)
        diecinueve['HALF'] =time(00, 00, 00)
        diecinueve['HPAI'] =time(00, 00, 00)
        diecinueve['HPAF'] =time(00, 00, 00)
        diecinueve['HDCI'] =time(00, 00, 00)
        diecinueve['HDCF'] =time(00, 00, 00)
        diecinueve['HSA'] = time(00, 00, 00)

        veinte['EN'] = date(13, 1, 1)
        veinte['HEN'] = time(00, 00, 00)
        veinte['HDYI'] = time(00, 00, 00)
        veinte['HDYF'] = time(00, 00, 00)
        veinte['HALI'] = time(00, 00, 00)
        veinte['HALF'] = time(00, 00, 00)
        veinte['HPAI'] = time(00, 00, 00)
        veinte['HPAF'] = time(00, 00, 00)
        veinte['HDCI'] = time(00, 00, 00)
        veinte['HDCF'] = time(00, 00, 00)
        veinte['HSA'] = time(00, 00, 00)

        veintiuno['EN'] = date(13, 1, 1)
        veintiuno['HEN'] = time(00, 00, 00)
        veintiuno['HDYI'] = time(00, 00, 00)
        veintiuno['HDYF'] = time(00, 00, 00)
        veintiuno['HALI'] = time(00, 00, 00)
        veintiuno['HALF'] = time(00, 00, 00)
        veintiuno['HPAI'] = time(00, 00, 00)
        veintiuno['HPAF'] = time(00, 00, 00)
        veintiuno['HDCI'] = time(00, 00, 00)
        veintiuno['HDCF'] = time(00, 00, 00)
        veintiuno['HSA'] = time(00, 00, 00)

        veintidos['EN'] = date(13, 1, 1)
        veintidos['HEN'] = time(00, 00, 00)
        veintidos['HDYI'] = time(00, 00, 00)
        veintidos['HDYF'] = time(00, 00, 00)
        veintidos['HALI'] = time(00, 00, 00)
        veintidos['HALF'] = time(00, 00, 00)
        veintidos['HPAI'] = time(00, 00, 00)
        veintidos['HPAF'] = time(00, 00, 00)
        veintidos['HDCI'] = time(00, 00, 00)
        veintidos['HDCF'] = time(00, 00, 00)
        veintidos['HSA'] = time(00, 00, 00)

        veintitres['EN'] = date(13, 1, 1)
        veintitres['HEN'] = time(00, 00, 00)
        veintitres['HDYI'] = time(00, 00, 00)
        veintitres['HDYF'] = time(00, 00, 00)
        veintitres['HALI'] = time(00, 00, 00)
        veintitres['HALF'] = time(00, 00, 00)
        veintitres['HPAI'] = time(00, 00, 00)
        veintitres['HPAF'] = time(00, 00, 00)
        veintitres['HDCI'] = time(00, 00, 00)
        veintitres['HDCF'] = time(00, 00, 00)
        veintitres['HSA'] = time(00, 00, 00)

        veinticuatro['EN'] = date(13, 1, 1)
        veinticuatro['HEN'] = time(00, 00, 00)
        veinticuatro['HDYI'] = time(00, 00, 00)
        veinticuatro['HDYF'] = time(00, 00, 00)
        veinticuatro['HALI'] = time(00, 00, 00)
        veinticuatro['HALF'] = time(00, 00, 00)
        veinticuatro['HPAI'] = time(00, 00, 00)
        veinticuatro['HPAF'] = time(00, 00, 00)
        veinticuatro['HDCI'] = time(00, 00, 00)
        veinticuatro['HDCF'] = time(00, 00, 00)
        veinticuatro['HSA'] = time(00, 00, 00)


        veinticinco['EN'] = date(13, 1, 1)
        veinticinco['HEN'] = time(00, 00, 00)
        veinticinco['HDYI'] = time(00, 00, 00)
        veinticinco['HDYF'] = time(00, 00, 00)
        veinticinco['HALI'] = time(00, 00, 00)
        veinticinco['HALF'] = time(00, 00, 00)
        veinticinco['HPAI'] = time(00, 00, 00)
        veinticinco['HPAF'] = time(00, 00, 00)
        veinticinco['HDCI'] = time(00, 00, 00)
        veinticinco['HDCF'] = time(00, 00, 00)
        veinticinco['HSA'] = time(00, 00, 00)

        veintiseis['EN'] = date(13, 1, 1)
        veintiseis['HEN'] = time(00, 00, 00)
        veintiseis['HDYI'] = time(00, 00, 00)
        veintiseis['HDYF'] = time(00, 00, 00)
        veintiseis['HALI'] = time(00, 00, 00)
        veintiseis['HALF'] = time(00, 00, 00)
        veintiseis['HPAI'] = time(00, 00, 00)
        veintiseis['HPAF'] = time(00, 00, 00)
        veintiseis['HDCI'] = time(00, 00, 00)
        veintiseis['HDCF'] = time(00, 00, 00)
        veintiseis['HSA'] = time(00, 00, 00)

        veintisiete['EN'] = date(13, 1, 1)
        veintisiete['HEN'] = time(00, 00, 00)
        veintisiete['HDYI'] = time(00, 00, 00)
        veintisiete['HDYF'] = time(00, 00, 00)
        veintisiete['HALI'] = time(00, 00, 00)
        veintisiete['HALF'] = time(00, 00, 00)
        veintisiete['HPAI'] = time(00, 00, 00)
        veintisiete['HPAF'] = time(00, 00, 00)
        veintisiete['HDCI'] = time(00, 00, 00)
        veintisiete['HDCF'] = time(00, 00, 00)
        veintisiete['HSA'] = time(00, 00, 00)

        veintiocho['EN'] = date(13, 1, 1)
        veintiocho['HEN'] = time(00, 00, 00)
        veintiocho['HDYI'] = time(00, 00, 00)
        veintiocho['HDYF'] = time(00, 00, 00)
        veintiocho['HALI'] = time(00, 00, 00)
        veintiocho['HALF'] = time(00, 00, 00)
        veintiocho['HPAI'] = time(00, 00, 00)
        veintiocho['HPAF'] = time(00, 00, 00)
        veintiocho['HDCI'] = time(00, 00, 00)
        veintiocho['HDCF'] = time(00, 00, 00)
        veintiocho['HSA'] = time(00, 00, 00)

        veintinueve['EN'] = date(13, 1, 1)
        veintinueve['HEN'] = time(00, 00, 00)
        veintinueve['HDYI'] = time(00, 00, 00)
        veintinueve['HDYF'] = time(00, 00, 00)
        veintinueve['HALI'] = time(00, 00, 00)
        veintinueve['HALF'] = time(00, 00, 00)
        veintinueve['HPAI'] = time(00, 00, 00)
        veintinueve['HPAF'] = time(00, 00, 00)
        veintinueve['HDCI'] = time(00, 00, 00)
        veintinueve['HDCF'] = time(00, 00, 00)
        veintinueve['HSA'] = time(00, 00, 00)

        treinta['EN'] = date(13, 1, 1)
        treinta['HEN'] = time(00, 00, 00)
        treinta['HDYI'] = time(00, 00, 00)
        treinta['HDYF'] = time(00, 00, 00)
        treinta['HALI'] = time(00, 00, 00)
        treinta['HALF'] = time(00, 00, 00)
        treinta['HPAI'] = time(00, 00, 00)
        treinta['HPAF'] = time(00, 00, 00)
        treinta['HDCI'] = time(00, 00, 00)
        treinta['HDCF'] = time(00, 00, 00)
        treinta['HSA'] = time(00, 00, 00)

        treintauno['EN'] = date(13, 1, 1)
        treintauno['HEN'] = time(00, 00, 00)
        treintauno['HDYI'] = time(00, 00, 00)
        treintauno['HDYF'] = time(00, 00, 00)
        treintauno['HALI'] = time(00, 00, 00)
        treintauno['HALF'] = time(00, 00, 00)
        treintauno['HPAI'] = time(00, 00, 00)
        treintauno['HPAF'] = time(00, 00, 00)
        treintauno['HDCI'] = time(00, 00, 00)
        treintauno['HDCF'] = time(00, 00, 00)
        treintauno['HSA'] = time(00, 00, 00)

        self.b= []
        formato2 = "%a"
        #print(filtroMes)
        hoy = datetime.today()
        hora_domi_fes = 0
        min_domi_fes = 0
        for i in q:
            mes1 = i
            for mes in filtroMes:
                if mes == mes1:
                    if mes.fecha.year == hoy.year:
                        fq = i.fecha.day
                        a['nombre'] = i.id_trabajadores.nombres
                        a['cedula'] = i.id_trabajadores.cedula
                        a['mes'] = mes.fecha.month
                        if mes.fecha.day == 1 and fq == 1:
                            uno[i.accion_jornada] = i.fecha
                            uno[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 2 and fq ==2:
                            dos[i.accion_jornada] = i.fecha
                            dos[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 3 and fq ==3:
                            tres[i.accion_jornada] = i.fecha
                            tres[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 4 and fq ==4:
                            cuatro[i.accion_jornada] = i.fecha
                            cuatro[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day ==5 and fq ==5:
                            cinco[i.accion_jornada] = i.fecha
                            cinco[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 6 and fq ==6:
                            seis[i.accion_jornada] = i.fecha
                            seis[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 7 and fq ==7:
                            siete[i.accion_jornada] = i.fecha
                            siete[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==8 and fq ==8:
                            ocho[i.accion_jornada] = i.fecha
                            ocho[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==9 and fq ==9:
                            nueve[i.accion_jornada] = i.fecha
                            nueve[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 10 and fq==10:
                            diez[i.accion_jornada] = i.fecha
                            diez[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 11 and fq == 11:
                            once[i.accion_jornada] = i.fecha
                            once[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==12 and fq ==12:
                            doce[i.accion_jornada] = i.fecha
                            doce[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==13 and fq ==13:
                            trece[i.accion_jornada] = i.fecha
                            trece[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==14 and fq ==14:
                            catorce[i.accion_jornada] = i.fecha
                            catorce[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 15 and fq ==15:
                            quince[i.accion_jornada] = i.fecha
                            quince[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 16 and fq ==16:
                            dieciseis[i.accion_jornada] = i.fecha
                            dieciseis[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 17 and fq ==17:
                            diecisiete[i.accion_jornada] = i.fecha
                            diecisiete[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 18 and fq ==18:
                            dieciocho[i.accion_jornada] = i.fecha
                            dieciocho[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==19 and fq ==19:
                            diecinueve[i.accion_jornada] = i.fecha
                            diecinueve[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 20 and fq ==20:
                            veinte[i.accion_jornada] = i.fecha
                            veinte[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 21 and fq ==21:
                            veintiuno[i.accion_jornada] = i.fecha
                            veintiuno[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==22 and fq ==22:
                            veintidos[i.accion_jornada] = i.fecha
                            veintidos[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==23 and fq ==23:
                            veintitres[i.accion_jornada] = i.fecha
                            veintitres[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 24 and fq ==24:
                            veinticuatro[i.accion_jornada] = i.fecha
                            veinticuatro[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day == 25 and fq ==25:
                            veinticinco[i.accion_jornada] = i.fecha
                            veinticinco[i.accion_jornada_hora] = i.hora
                            #print(veinticinco, "VEINTICIC")
                        elif mes.fecha.day==26 and fq ==26:
                            veintiseis[i.accion_jornada] = i.fecha
                            veintiseis[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==27 and fq ==27:
                            veintisiete[i.accion_jornada] = i.fecha
                            veintisiete[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==28 and fq ==28:
                            veintiocho[i.accion_jornada] = i.fecha
                            veintiocho[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==29 and fq ==29:
                            veintinueve[i.accion_jornada] = i.fecha
                            veintinueve[i.accion_jornada_hora] = i.hora
                        elif mes.fecha.day==30 and fq ==30:
                            treinta[i.accion_jornada] = i.fecha
                            treinta[i.accion_jornada_hora] = i.hora
                            #print(treinta)
                        elif mes.fecha.day==31 and fq ==31:
                            treintauno[i.accion_jornada] = i.fecha
                            treintauno[i.accion_jornada_hora] = i.hora
        #print("Fecha en formato ISO 8601:", trece['EN'].strftime(formato2))
        #print("Fecha en formato ISO 8601:", veintisiete['EN'].strftime(formato2))
        #print("Fecha en formato ISO 8601:", veintisiete[i.accion_jornada])
        #print("Fecha en formato ISO 8601:", veinte[i.accion_jornada].strftime(formato2))
        #print("Fecha en formato ISO 8601:", veintiuno[i.accion_jornada].strftime(formato2))
            
        self.b.append(a)
        self.b.append(uno)
        self.b.append(dos)
        self.b.append(tres)
        self.b.append(cuatro)
        self.b.append(cinco)
        self.b.append(seis)
        self.b.append(siete)
        self.b.append(ocho)
        self.b.append(nueve)
        self.b.append(diez)
        self.b.append(once)
        self.b.append(doce)
        self.b.append(trece)
        self.b.append(catorce)
        self.b.append(quince)
        self.b.append(dieciseis)
        self.b.append(diecisiete)
        self.b.append(dieciocho)
        self.b.append(diecinueve)
        self.b.append(veinte)
        self.b.append(veintiuno)
        self.b.append(veintidos)
        self.b.append(veintitres)
        self.b.append(veinticuatro)
        self.b.append(veinticinco)
        self.b.append(veintiseis)
        self.b.append(veintisiete)
        self.b.append(veintiocho)
        self.b.append(veintinueve)
        self.b.append(treinta)
        self.b.append(treintauno)

        #FORMATO HORA, MINUTOS Y SEGUNDOS
        formato1 = "%H:%M:%S"
        # Asigna formato de ejemplo2
        
        #TOTAL MES
        totalMes = 0
        totalMesMinutos = 0

        #UNO
        if uno['HEN'] != time(00, 00, 00) and uno['HSA'] != time(00, 00, 00):
            horasTrabajadas = uno['HSA'].hour - uno['HEN'].hour
        else:
            horasTrabajadas = 0
        if uno['HEN'] != time(00, 00, 00) and uno['HSA'] != time(00, 00, 00):
            minutosTrabajadas = uno['HSA'].minute - uno['HEN'].minute
        else:
            minutosTrabajadas = 0
        if uno['HALI'] != time(00, 00, 00) and uno['HALF'] != time(00, 00, 00):
            horasAlmuerzo = uno['HALF'].hour -uno['HALI'].hour
        else:
            horasAlmuerzo = 0
        if uno['HALI'] != time(00, 00, 00) and uno['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = uno['HALF'].minute -uno['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """
        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if uno['HSA'] == 'NA':
            minutosTotal = 0
        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if uno['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = uno['HEN'].strftime(formato1)
    
        if uno['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = uno['HDYI'].strftime(formato1)
    
        if uno['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = uno['HDYF'].strftime(formato1)
    
        if uno['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = uno['HALI'].strftime(formato1)
    
        if uno['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = uno['HALF'].strftime(formato1)
    
        if uno['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = uno['HPAI'].strftime(formato1)
    
        if uno['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = uno['HPAF'].strftime(formato1)
    
        if uno['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = uno['HDCI'].strftime(formato1)
    
        if uno['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = uno['HDCF'].strftime(formato1)
    
        if uno['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = uno['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if uno['EN'].month ==  d.festivos.month and uno['EN'].year == d.festivos.year:
                if d.festivos.day ==  uno['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if uno['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal
            min_domi_fes = minutosTotal            
    
        if uno['EN'].day == 1:
            uno1= uno['EN'].strftime(formato2)
            print(uno1, "UNO1111")
            detalles1 = [('1 ' + uno1, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles1 = [(1 , 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DOS
        if dos['HEN'] != time(00, 00, 00) and dos['HSA'] != time(00, 00, 00):
            horasTrabajadas = dos['HSA'].hour - dos['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if dos['HEN'] != time(00, 00, 00) and dos['HSA'] != time(00, 00, 00):
            minutosTrabajadas = dos['HSA'].minute - dos['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if dos['HALI'] != time(00, 00, 00) and dos['HALF'] != time(00, 00, 00):
            horasAlmuerzo = dos['HALF'].hour -dos['HALI'].hour
        else:
            horasAlmuerzo = 0
        if dos['HALI'] != time(00, 00, 00) and dos['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = dos['HALF'].minute -dos['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """
        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if dos['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)
        
        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos

        if dos['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = dos['HEN'].strftime(formato1)
    
        if dos['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = dos['HDYI'].strftime(formato1)
    
        if dos['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = dos['HDYF'].strftime(formato1)
    
        if dos['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = dos['HALI'].strftime(formato1)
    
        if dos['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = dos['HALF'].strftime(formato1)
    
        if dos['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = dos['HPAI'].strftime(formato1)
    
        if dos['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = dos['HPAF'].strftime(formato1)
    
        if dos['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = dos['HDCI'].strftime(formato1)
    
        if dos['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = dos['HDCF'].strftime(formato1)
    
        if dos['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = dos['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if dos['EN'].month ==  d.festivos.month and dos['EN'].year == d.festivos.year:
                if d.festivos.day ==  dos['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if dos['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if dos['EN'].day == 2:
            uno2= dos['EN'].strftime(formato2)
            detalles2 = [('2'+ uno2, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles2 = [(2 , 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #TRES
        if tres['HEN'] != time(00, 00, 00) and tres['HSA'] != time(00, 00, 00):
            horasTrabajadas = tres['HSA'].hour - tres['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if tres['HEN'] != time(00, 00, 00) and tres['HSA'] != time(00, 00, 00):
            minutosTrabajadas = tres['HSA'].minute - tres['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if tres['HALI'] != time(00, 00, 00) and tres['HALF'] != time(00, 00, 00):
            horasAlmuerzo = tres['HALF'].hour -tres['HALI'].hour
        else:
            horasAlmuerzo = 0
        if tres['HALI'] != time(00, 00, 00) and tres['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = tres['HALF'].minute -tres['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if tres['HSA'] == 'NA':
            minutosTotal = 0

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if tres['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = tres['HEN'].strftime(formato1)
    
        if tres['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = tres['HDYI'].strftime(formato1)
    
        if tres['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = tres['HDYF'].strftime(formato1)
    
        if tres['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = tres['HALI'].strftime(formato1)
    
        if tres['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = tres['HALF'].strftime(formato1)
    
        if tres['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = tres['HPAI'].strftime(formato1)
    
        if tres['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = tres['HPAF'].strftime(formato1)
    
        if tres['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = tres['HDCI'].strftime(formato1)
    
        if tres['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = tres['HDCF'].strftime(formato1)
    
        if tres['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = tres['HSA'].strftime(formato1)
        
        cont = 0
        for d in festivos:
            if tres['EN'].month ==  d.festivos.month and tres['EN'].year == d.festivos.year:
                if d.festivos.day ==  tres['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if tres['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if tres['EN'].day == 3:
            tres3= tres['EN'].strftime(formato2)
            detalles3 = [('3 '+ tres3, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles3 = [(3, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #CUATRO
        if cuatro['HEN'] != time(00, 00, 00) and cuatro['HSA'] != time(00, 00, 00):
            horasTrabajadas = cuatro['HSA'].hour - cuatro['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if cuatro['HEN'] != time(00, 00, 00) and cuatro['HSA'] != time(00, 00, 00):
            minutosTrabajadas = cuatro['HSA'].minute - cuatro['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if cuatro['HALI'] != time(00, 00, 00) and cuatro['HALF'] != time(00, 00, 00):
            horasAlmuerzo = cuatro['HALF'].hour -cuatro['HALI'].hour
        else:
            horasAlmuerzo = 0
        if cuatro['HALI'] != time(00, 00, 00) and cuatro['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = cuatro['HALF'].minute -cuatro['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """
        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if cuatro['HSA'] == 'NA':
            minutosTotal = 0

        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if cuatro['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = cuatro['HEN'].strftime(formato1)
    
        if cuatro['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = cuatro['HDYI'].strftime(formato1)
    
        if cuatro['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = cuatro['HDYF'].strftime(formato1)
    
        if cuatro['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = cuatro['HALI'].strftime(formato1)
    
        if cuatro['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = cuatro['HALF'].strftime(formato1)
    
        if cuatro['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = cuatro['HPAI'].strftime(formato1)
    
        if cuatro['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = cuatro['HPAF'].strftime(formato1)
    
        if cuatro['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = cuatro['HDCI'].strftime(formato1)
    
        if cuatro['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = cuatro['HDCF'].strftime(formato1)
    
        if cuatro['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = cuatro['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if cuatro['EN'].month ==  d.festivos.month and cuatro['EN'].year == d.festivos.year:
                if d.festivos.day ==  cuatro['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if cuatro['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if cuatro['EN'].day == 4:
            cuatro4= cuatro4['EN'].strftime(formato2)
            detalles4 = [('4 '+ cuatro4, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles4 = [(4, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #CINCO
        if cinco['HEN'] != time(00, 00, 00) and cinco['HSA'] != time(00, 00, 00):
            horasTrabajadas = cinco['HSA'].hour - cinco['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if cinco['HEN'] != time(00, 00, 00) and cinco['HSA'] != time(00, 00, 00):
            minutosTrabajadas = cinco['HSA'].minute - cinco['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if cinco['HALI'] != time(00, 00, 00) and cinco['HALF'] != time(00, 00, 00):
            horasAlmuerzo = cinco['HALF'].hour -cinco['HALI'].hour
        else:
            horasAlmuerzo = 0
        if cinco['HALI'] != time(00, 00, 00) and cinco['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = cinco['HALF'].minute -cinco['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """
        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if cinco['HSA'] == 'NA':
            minutosTotal = 0

        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante


        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if cinco['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = cinco['HEN'].strftime(formato1)
    
        if cinco['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = cinco['HDYI'].strftime(formato1)
    
        if cinco['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = cinco['HDYF'].strftime(formato1)
    
        if cinco['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = cinco['HALI'].strftime(formato1)
    
        if cinco['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = cinco['HALF'].strftime(formato1)
    
        if cinco['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = cinco['HPAI'].strftime(formato1)
    
        if cinco['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = cinco['HPAF'].strftime(formato1)
    
        if cinco['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = cinco['HDCI'].strftime(formato1)
    
        if cinco['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = cinco['HDCF'].strftime(formato1)
    
        if cinco['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = cinco['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if cinco['EN'].month ==  d.festivos.month and cinco['EN'].year == d.festivos.year:
                if d.festivos.day ==  cinco['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if cinco['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if cinco['EN'].day == 5:
            cinco5= cinco['EN'].strftime(formato2)
            detalles5 = [('5 '+ cinco5, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles5 = [(5, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #SEIS
        if seis['HEN'] != time(00, 00, 00) and seis['HSA'] != time(00, 00, 00):
            horasTrabajadas = seis['HSA'].hour - seis['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if seis['HEN'] != time(00, 00, 00) and seis['HSA'] != time(00, 00, 00):
            minutosTrabajadas = seis['HSA'].minute - seis['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if seis['HALI'] != time(00, 00, 00) and seis['HALF'] != time(00, 00, 00):
            horasAlmuerzo = seis['HALF'].hour -seis['HALI'].hour
        else:
            horasAlmuerzo = 0
        if seis['HALI'] != time(00, 00, 00) and seis['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = seis['HALF'].minute -seis['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if seis['HSA'] == 'NA':
            minutosTotal = 0

        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if seis['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = seis['HEN'].strftime(formato1)
    
        if seis['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = seis['HDYI'].strftime(formato1)
    
        if seis['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = seis['HDYF'].strftime(formato1)
    
        if seis['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = seis['HALI'].strftime(formato1)
    
        if seis['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = seis['HALF'].strftime(formato1)
    
        if seis['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = seis['HPAI'].strftime(formato1)
    
        if seis['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = seis['HPAF'].strftime(formato1)
    
        if seis['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = seis['HDCI'].strftime(formato1)
    
        if seis['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = seis['HDCF'].strftime(formato1)
    
        if seis['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = seis['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if seis['EN'].month ==  d.festivos.month and seis['EN'].year == d.festivos.year:
                if d.festivos.day ==  seis['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if seis['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if seis['EN'].day == 6:
            seis6= seis6['EN'].strftime(formato2)
            detalle6 = [('6 '+ seis6, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles6 = [(6 , 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #SIETE
        if siete['HEN'] != time(00, 00, 00) and siete['HSA'] != time(00, 00, 00):
            horasTrabajadas = siete['HSA'].hour - siete['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if siete['HEN'] != time(00, 00, 00) and siete['HSA'] != time(00, 00, 00):
            minutosTrabajadas = siete['HSA'].minute - siete['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if siete['HALI'] != time(00, 00, 00) and siete['HALF'] != time(00, 00, 00):
            horasAlmuerzo = siete['HALF'].hour -siete['HALI'].hour
        else:
            horasAlmuerzo = 0
        if siete['HALI'] != time(00, 00, 00) and siete['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = siete['HALF'].minute -siete['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if siete['HSA'] == 'NA':
            minutosTotal = 0

        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if siete['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = siete['HEN'].strftime(formato1)
    
        if siete['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = siete['HDYI'].strftime(formato1)
    
        if siete['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = siete['HDYF'].strftime(formato1)
    
        if siete['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = siete['HALI'].strftime(formato1)
    
        if siete['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = siete['HALF'].strftime(formato1)
    
        if siete['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = siete['HPAI'].strftime(formato1)
    
        if siete['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = siete['HPAF'].strftime(formato1)
    
        if siete['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = siete['HDCI'].strftime(formato1)
    
        if siete['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = siete['HDCF'].strftime(formato1)
    
        if siete['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = siete['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if siete['EN'].month ==  d.festivos.month and siete['EN'].year == d.festivos.year:
                if d.festivos.day ==  siete['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if siete['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
            
        if siete['EN'].day == 7:
            siete7= siete['EN'].strftime(formato2)
            detalles7 = [('7 '+ siete7, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles7 = [(7, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #OCHO
        if ocho['HEN'] != time(00, 00, 00) and ocho['HSA'] != time(00, 00, 00):
            horasTrabajadas = ocho['HSA'].hour - ocho['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if ocho['HEN'] != time(00, 00, 00) and ocho['HSA'] != time(00, 00, 00):
            minutosTrabajadas = ocho['HSA'].minute - ocho['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if ocho['HALI'] != time(00, 00, 00) and ocho['HALF'] != time(00, 00, 00):
            horasAlmuerzo = ocho['HALF'].hour -ocho['HALI'].hour
        else:
            horasAlmuerzo = 0
        if ocho['HALI'] != time(00, 00, 00) and ocho['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = ocho['HALF'].minute -ocho['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """
        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if ocho['HSA'] == 'NA':
            minutosTotal = 0
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if ocho['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = ocho['HEN'].strftime(formato1)
    
        if ocho['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = ocho['HDYI'].strftime(formato1)
    
        if ocho['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = ocho['HDYF'].strftime(formato1)
    
        if ocho['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = ocho['HALI'].strftime(formato1)
    
        if ocho['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = ocho['HALF'].strftime(formato1)
    
        if ocho['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = ocho['HPAI'].strftime(formato1)
    
        if ocho['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = ocho['HPAF'].strftime(formato1)
    
        if ocho['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = ocho['HDCI'].strftime(formato1)
    
        if ocho['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = ocho['HDCF'].strftime(formato1)
    
        if ocho['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = ocho['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if ocho['EN'].month ==  d.festivos.month and ocho['EN'].year == d.festivos.year:
                if d.festivos.day ==  ocho['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if ocho['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if ocho['EN'].day == 8:
            ocho8= ocho['EN'].strftime(formato2)
            detalles8 = [('8 '+ ocho8 , la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles8 = [(8, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #NUEVE
        if nueve['HEN'] != time(00, 00, 00) and nueve['HSA'] != time(00, 00, 00):
            horasTrabajadas = nueve['HSA'].hour - nueve['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if nueve['HEN'] != time(00, 00, 00) and nueve['HSA'] != time(00, 00, 00):
            minutosTrabajadas = nueve['HSA'].minute - nueve['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if nueve['HALI'] != time(00, 00, 00) and nueve['HALF'] != time(00, 00, 00):
            horasAlmuerzo = nueve['HALF'].hour -nueve['HALI'].hour
        else:
            horasAlmuerzo = 0
        if nueve['HALI'] != time(00, 00, 00) and nueve['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = nueve['HALF'].minute -nueve['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if nueve['HSA'] == 'NA':
            minutosTotal = 0

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if nueve['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = nueve['HEN'].strftime(formato1)
    
        if nueve['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = nueve['HDYI'].strftime(formato1)
    
        if nueve['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = nueve['HDYF'].strftime(formato1)
    
        if nueve['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = nueve['HALI'].strftime(formato1)
    
        if nueve['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = nueve['HALF'].strftime(formato1)
    
        if nueve['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = nueve['HPAI'].strftime(formato1)
    
        if nueve['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = nueve['HPAF'].strftime(formato1)
    
        if nueve['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = nueve['HDCI'].strftime(formato1)
    
        if nueve['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = nueve['HDCF'].strftime(formato1)
    
        if nueve['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = nueve['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if nueve['EN'].month ==  d.festivos.month and nueve['EN'].year == d.festivos.year:
                if d.festivos.day ==  nueve['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if nueve['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
            
        if nueve['EN'].day == 9:
            nueve9= nueve['EN'].strftime(formato2)
            detalles9 = [('9 '+ nueve9, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles9 = [(9,'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DIEZ
        if diez['HEN'] != time(00, 00, 00) and diez['HSA'] != time(00, 00, 00):
            horasTrabajadas = diez['HSA'].hour - diez['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if diez['HEN'] != time(00, 00, 00) and diez['HSA'] != time(00, 00, 00):
            minutosTrabajadas = diez['HSA'].minute - diez['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if diez['HALI'] != time(00, 00, 00) and diez['HALF'] != time(00, 00, 00):
            horasAlmuerzo = diez['HALF'].hour -diez['HALI'].hour
        else:
            horasAlmuerzo = 0
        if diez['HALF'] != time(00, 00, 00) and diez['HALI'] != time(00, 00, 00):
            minutosAlmuerzo = diez['HALF'].minute -diez['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """
        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if diez['HSA'] == 'NA':
            minutosTotal = 0

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if diez['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = diez['HEN'].strftime(formato1)
    
        if diez['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = diez['HDYI'].strftime(formato1)
    
        if diez['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = diez['HDYF'].strftime(formato1)
    
        if diez['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = diez['HALI'].strftime(formato1)
    
        if diez['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = diez['HALF'].strftime(formato1)
    
        if diez['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = diez['HPAI'].strftime(formato1)
    
        if diez['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = diez['HPAF'].strftime(formato1)
    
        if diez['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = diez['HDCI'].strftime(formato1)
    
        if diez['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = diez['HDCF'].strftime(formato1)
    
        if diez['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = diez['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if diez['EN'].month ==  d.festivos.month and diez['EN'].year == d.festivos.year:
                if d.festivos.day ==  diez['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if diez['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if diez['EN'].day == 10:
            diez10= diez['EN'].strftime(formato2)
            detalles10 = [('10 '+ diez10, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles10 = [(10, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #ONCE
        if once['HEN'] != time(00, 00, 00) and once['HSA'] != time(00, 00, 00):
            horasTrabajadas = once['HSA'].hour - once['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if once['HEN'] != time(00, 00, 00) and once['HSA'] != time(00, 00, 00):
            minutosTrabajadas = once['HSA'].minute - once['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if once['HALI'] != time(00, 00, 00) and once['HALF'] != time(00, 00, 00):
            horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasAlmuerzo = 0
        if once['HALF'] != time(00, 00, 00) and once['HALI'] != time(00, 00, 00):
            minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """
        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if once['HSA'] == 'NA':
            minutosTotal = 0

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if once['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = once['HEN'].strftime(formato1)
    
        if once['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = once['HDYI'].strftime(formato1)
    
        if once['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = once['HDYF'].strftime(formato1)
    
        if once['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = once['HALI'].strftime(formato1)
    
        if once['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = once['HALF'].strftime(formato1)
    
        if once['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = once['HPAI'].strftime(formato1)
    
        if once['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = once['HPAF'].strftime(formato1)
    
        if once['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = once['HDCI'].strftime(formato1)
    
        if once['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = once['HDCF'].strftime(formato1)
    
        if once['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = once['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if once['EN'].month ==  d.festivos.month and once['EN'].year == d.festivos.year:
                if d.festivos.day ==  once['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if once['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
            
        if once['EN'].day == 11:
            once11= once['EN'].strftime(formato2)
            detalles11 = [('11 '+once11, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles11 = [(11 , 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #DOCE
        if doce['HEN'] != time(00, 00, 00) and doce['HSA'] != time(00, 00, 00):
            horasTrabajadas = doce['HSA'].hour - doce['HEN'].hour
        else:
            horasTrabajadas = 0
        if doce['HEN'] != time(00, 00, 00) and doce['HSA'] != time(00, 00, 00):
            minutosTrabajadas = doce['HSA'].minute - doce['HEN'].minute
        else:
            minutosTrabajadas = 0
        if doce['HALI'] != time(00, 00, 00) and doce['HALF'] != time(00, 00, 00):
            horasAlmuerzo = doce['HALF'].hour -doce['HALI'].hour
        else:
            horasAlmuerzo = 0
        if doce['HALI'] != time(00, 00, 00) and doce['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = doce['HALF'].minute -doce['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if doce['HSA'] == 'NA':
            minutosTotal = 0

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        
        if doce['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = doce['HEN'].strftime(formato1)
    
        if doce['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = doce['HDYI'].strftime(formato1)
    
        if doce['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = doce['HDYF'].strftime(formato1)
    
        if doce['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = doce['HALI'].strftime(formato1)
    
        if doce['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = doce['HALF'].strftime(formato1)
    
        if doce['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = doce['HPAI'].strftime(formato1)
    
        if doce['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = doce['HPAF'].strftime(formato1)
    
        if doce['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = doce['HDCI'].strftime(formato1)
    
        if doce['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = doce['HDCF'].strftime(formato1)
    
        if doce['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = doce['HSA'].strftime(formato1)
            
        if doce['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
            
        cont = 0
        for d in festivos:
            if doce['EN'].month ==  d.festivos.month and doce['EN'].year == d.festivos.year:
                if d.festivos.day ==  doce['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
    
        if doce['EN'].day == 12:
            doce12= doce['EN'].strftime(formato2)
            detalles12 = [('12 '+doce12, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles12 = [(12, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #TRECE
        if trece['HEN'] != time(00, 00, 00) and trece['HSA'] != time(00, 00, 00):
            horasTrabajadas = trece['HSA'].hour - trece['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if trece['HEN'] != time(00, 00, 00) and trece['HSA'] != time(00, 00, 00):
            minutosTrabajadas = trece['HSA'].minute - trece['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if trece['HALI'] != time(00, 00, 00) and trece['HALF'] != time(00, 00, 00):
            horasAlmuerzo = trece['HALF'].hour -trece['HALI'].hour
        else:
            horasAlmuerzo = 0
        if trece['HALI'] != time(00, 00, 00) and trece['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = trece['HALF'].minute -trece['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if trece['HSA'] == 'NA':
            minutosTotal = 0

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if trece['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = trece['HEN'].strftime(formato1)
    
        if trece['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = trece['HDYI'].strftime(formato1)
    
        if trece['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = trece['HDYF'].strftime(formato1)
    
        if trece['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = trece['HALI'].strftime(formato1)
    
        if trece['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = trece['HALF'].strftime(formato1)
    
        if trece['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = trece['HPAI'].strftime(formato1)
    
        if trece['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = trece['HPAF'].strftime(formato1)
    
        if trece['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = trece['HDCI'].strftime(formato1)
    
        if trece['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = trece['HDCF'].strftime(formato1)
    
        if trece['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = trece['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if trece['EN'].month ==  d.festivos.month and trece['EN'].year == d.festivos.year:
                if d.festivos.day ==  trece['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if trece['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if trece['EN'].day == 13:
            trece13= trece['EN'].strftime(formato2)
            detalles13 = [('13 '+ trece13, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles13 = [(13, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #CATORCE
        if catorce['HEN'] != time(00, 00, 00) and catorce['HSA'] != time(00, 00, 00):
            horasTrabajadas = catorce['HSA'].hour - catorce['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if catorce['HEN'] != time(00, 00, 00) and catorce['HSA'] != time(00, 00, 00):
            minutosTrabajadas = catorce['HSA'].minute - catorce['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if catorce['HALI'] != time(00, 00, 00) and catorce['HALF'] != time(00, 00, 00):
            horasAlmuerzo = catorce['HALF'].hour -catorce['HALI'].hour
        else:
            horasAlmuerzo = 0
        if catorce['HALI'] != time(00, 00, 00) and catorce['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = catorce['HALF'].minute -catorce['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """
        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if catorce['HSA'] == 'NA':
            minutosTotal = 0

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if catorce['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = catorce['HEN'].strftime(formato1)
    
        if catorce['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = catorce['HDYI'].strftime(formato1)
    
        if catorce['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = catorce['HDYF'].strftime(formato1)
    
        if catorce['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = catorce['HALI'].strftime(formato1)
    
        if catorce['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = catorce['HALF'].strftime(formato1)
    
        if catorce['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = catorce['HPAI'].strftime(formato1)
    
        if catorce['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = catorce['HPAF'].strftime(formato1)
    
        if catorce['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = catorce['HDCI'].strftime(formato1)
    
        if catorce['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = catorce['HDCF'].strftime(formato1)
    
        if catorce['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = catorce['HSA'].strftime(formato1)
            
        if catorce['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
            
        cont = 0
        for d in festivos:
            if catorce['EN'].month ==  d.festivos.month and catorce['EN'].year == d.festivos.year:
                if d.festivos.day ==  catorce['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
    
        if catorce['EN'].day == 14:
            catorce14= catorce['EN'].strftime(formato2)
            detalles14 = [('14 '+ catorce14, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles14 = [(14, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #QUINCE
        if quince['HEN'] != time(00, 00, 00) and quince['HSA'] != time(00, 00, 00):
            horasTrabajadas = quince['HSA'].hour - quince['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if quince['HEN'] != time(00, 00, 00) and quince['HSA'] != time(00, 00, 00):
            minutosTrabajadas = quince['HSA'].minute - quince['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if quince['HALI'] != time(00, 00, 00) and quince['HALF'] != time(00, 00, 00):
            horasAlmuerzo = quince['HALF'].hour -quince['HALI'].hour
        else:
            horasAlmuerzo = 0
        if quince['HALI'] != time(00, 00, 00) and quince['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = quince['HALF'].minute -quince['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if quince['HSA'] == 'NA':
            minutosTotal = 0

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if quince['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = quince['HEN'].strftime(formato1)
    
        if quince['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = quince['HDYI'].strftime(formato1)
    
        if quince['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = quince['HDYF'].strftime(formato1)
    
        if quince['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = quince['HALI'].strftime(formato1)
    
        if quince['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = quince['HALF'].strftime(formato1)
    
        if quince['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = quince['HPAI'].strftime(formato1)
    
        if quince['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = quince['HPAF'].strftime(formato1)
    
        if quince['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = quince['HDCI'].strftime(formato1)
    
        if quince['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = quince['HDCF'].strftime(formato1)
    
        if quince['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = quince['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if quince['EN'].month ==  d.festivos.month and quince['EN'].year == d.festivos.year:
                if d.festivos.day ==  quince['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if quince['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if quince['EN'].day == 15:
            quince15= quince['EN'].strftime(formato2)
            detalles15 = [('15 '+quince15, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles15 = [(15, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DIECISEIS
        if dieciseis['HEN'] != time(00, 00, 00) and dieciseis['HSA'] != time(00, 00, 00):
            horasTrabajadas = dieciseis['HSA'].hour - dieciseis['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if dieciseis['HEN'] != time(00, 00, 00) and dieciseis['HSA'] != time(00, 00, 00):
            minutosTrabajadas = dieciseis['HSA'].minute - dieciseis['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if dieciseis['HALI'] != time(00, 00, 00) and dieciseis['HALF'] != time(00, 00, 00):
            horasAlmuerzo = dieciseis['HALF'].hour -dieciseis['HALI'].hour
        else:
            horasAlmuerzo = 0
        if dieciseis['HALI'] != time(00, 00, 00) and dieciseis['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = dieciseis['HALF'].minute -dieciseis['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """
        
        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if dieciseis['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if dieciseis['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = dieciseis['HEN'].strftime(formato1)
    
        if dieciseis['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = dieciseis['HDYI'].strftime(formato1)
    
        if dieciseis['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = dieciseis['HDYF'].strftime(formato1)
    
        if dieciseis['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = dieciseis['HALI'].strftime(formato1)
    
        if dieciseis['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = dieciseis['HALF'].strftime(formato1)
    
        if dieciseis['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = dieciseis['HPAI'].strftime(formato1)
    
        if dieciseis['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = dieciseis['HPAF'].strftime(formato1)
    
        if dieciseis['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = dieciseis['HDCI'].strftime(formato1)
    
        if dieciseis['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = dieciseis['HDCF'].strftime(formato1)
    
        if dieciseis['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = dieciseis['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if dieciseis['EN'].month ==  d.festivos.month and dieciseis['EN'].year == d.festivos.year:
                if d.festivos.day ==  dieciseis['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if dieciseis['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if dieciseis['EN'].day == 16:
            dieciseis16 = dieciseis['EN'].strftime(formato2)
            detalles16 = [('16 '+ dieciseis16, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles16 = [(16, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DIECISIETE
        if diecisiete['HEN'] != time(00, 00, 00) and diecisiete['HSA'] != time(00, 00, 00):
            horasTrabajadas = diecisiete['HSA'].hour - diecisiete['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if diecisiete['HEN'] != time(00, 00, 00) and diecisiete['HSA'] != time(00, 00, 00):
            minutosTrabajadas = diecisiete['HSA'].minute - diecisiete['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if diecisiete['HALI'] != time(00, 00, 00) and diecisiete['HALF'] != time(00, 00, 00):
            horasAlmuerzo = diecisiete['HALF'].hour -diecisiete['HALI'].hour
        else:
            horasAlmuerzo = 0
        if diecisiete['HALI'] != time(00, 00, 00) and diecisiete['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = diecisiete['HALF'].minute -diecisiete['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if diecisiete['HSA'] == 'NA':
            minutosTotal = 0

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if diecisiete['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = diecisiete['HEN'].strftime(formato1)
    
        if diecisiete['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = diecisiete['HDYI'].strftime(formato1)
    
        if diecisiete['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = diecisiete['HDYF'].strftime(formato1)
    
        if diecisiete['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = diecisiete['HALI'].strftime(formato1)
    
        if diecisiete['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = diecisiete['HALF'].strftime(formato1)
    
        if diecisiete['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = diecisiete['HPAI'].strftime(formato1)
    
        if diecisiete['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = diecisiete['HPAF'].strftime(formato1)
    
        if diecisiete['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = diecisiete['HDCI'].strftime(formato1)
    
        if diecisiete['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = diecisiete['HDCF'].strftime(formato1)
    
        if diecisiete['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = diecisiete['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if diecisiete['EN'].month ==  d.festivos.month and diecisiete['EN'].year == d.festivos.year:
                if d.festivos.day ==  diecisiete['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if diecisiete['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if diecisiete['EN'].day == 17:
            diecisiete17 = diecisiete['EN'].strftime(formato2)
            detalles17 = [('17 '+ diecisiete17, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles17 = [(17, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DIECIOCHO
        if dieciocho['HEN'] != time(00, 00, 00) and dieciocho['HSA'] != time(00, 00, 00):
            horasTrabajadas = dieciocho['HSA'].hour - dieciocho['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if dieciocho['HEN'] != time(00, 00, 00) and dieciocho['HSA'] != time(00, 00, 00):
            minutosTrabajadas = dieciocho['HSA'].minute - dieciocho['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if dieciocho['HALI'] != time(00, 00, 00) and dieciocho['HALF'] != time(00, 00, 00):
            horasAlmuerzo = dieciocho['HALF'].hour -dieciocho['HALI'].hour
        else:
            horasAlmuerzo = 0
        if dieciocho['HALI'] != time(00, 00, 00) and dieciocho['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = dieciocho['HALF'].minute -dieciocho['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if dieciocho['HSA'] == 'NA':
            minutosTotal = 0

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if dieciocho['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = dieciocho['HEN'].strftime(formato1)
    
        if dieciocho['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = dieciocho['HDYI'].strftime(formato1)
    
        if dieciocho['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = dieciocho['HDYF'].strftime(formato1)
    
        if dieciocho['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = dieciocho['HALI'].strftime(formato1)
    
        if dieciocho['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = dieciocho['HALF'].strftime(formato1)
    
        if dieciocho['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = dieciocho['HPAI'].strftime(formato1)
    
        if dieciocho['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = dieciocho['HPAF'].strftime(formato1)
    
        if dieciocho['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = dieciocho['HDCI'].strftime(formato1)
    
        if dieciocho['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = dieciocho['HDCF'].strftime(formato1)
    
        if dieciocho['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = dieciocho['HSA'].strftime(formato1)
            
        cont =0
        for d in festivos:
            if dieciocho['EN'].month ==  d.festivos.month and dieciocho['EN'].year == d.festivos.year:
                if d.festivos.day ==  dieciocho['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if dieciocho['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if dieciocho['EN'].day == 18:
            dieciocho18= dieciocho['EN'].strftime(formato2)
            detalles18 = [('18 '+ dieciocho18, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles18 = [(18,'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DIECINUEVE
        if diecinueve['HEN'] != time(00, 00, 00) and diecinueve['HSA'] != time(00, 00, 00):
            horasTrabajadas = diecinueve['HSA'].hour - diecinueve['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if diecinueve['HEN'] != time(00, 00, 00) and diecinueve['HSA'] != time(00, 00, 00):
            minutosTrabajadas = diecinueve['HSA'].minute - diecinueve['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if diecinueve['HALI'] != time(00, 00, 00) and diecinueve['HALF'] != time(00, 00, 00):
            horasAlmuerzo = diecinueve['HALF'].hour -diecinueve['HALI'].hour
        else:
            horasAlmuerzo = 0
        if diecinueve['HALI'] != time(00, 00, 00) and diecinueve['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = diecinueve['HALF'].minute -diecinueve['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if diecinueve['HSA'] == 'NA':
            minutosTotal = 0

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if diecinueve['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = diecinueve['HEN'].strftime(formato1)
    
        if diecinueve['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = diecinueve['HDYI'].strftime(formato1)
    
        if diecinueve['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = diecinueve['HDYF'].strftime(formato1)
    
        if diecinueve['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = diecinueve['HALI'].strftime(formato1)
    
        if diecinueve['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = diecinueve['HALF'].strftime(formato1)
    
        if diecinueve['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = diecinueve['HPAI'].strftime(formato1)
    
        if diecinueve['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = diecinueve['HPAF'].strftime(formato1)
    
        if diecinueve['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = diecinueve['HDCI'].strftime(formato1)
    
        if diecinueve['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = diecinueve['HDCF'].strftime(formato1)
    
        if diecinueve['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = diecinueve['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if diecinueve['EN'].month ==  d.festivos.month and diecinueve['EN'].year == d.festivos.year:
                if d.festivos.day ==  diecinueve['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if diecinueve['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if diecinueve['EN'].day == 19:
            diecinueve19 = diecinueve19['EN'].strftime(formato2)
            detalles19 = [('19 '+diecinueve19, la, la1, la2, la3, la4, la5, la6, la7, la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles19 = [(19, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTE
        if veinte['HEN'] != time(00, 00, 00) and veinte['HSA'] != time(00, 00, 00):
            horasTrabajadas = veinte['HSA'].hour - veinte['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veinte['HEN'] != time(00, 00, 00) and veinte['HSA'] != time(00, 00, 00):
            minutosTrabajadas = veinte['HSA'].minute - veinte['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veinte['HALI'] != time(00, 00, 00) and veinte['HALF'] != time(00, 00, 00):
            horasAlmuerzo = veinte['HALF'].hour -veinte['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veinte['HALI'] != time(00, 00, 00) and veinte['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = veinte['HALF'].minute -veinte['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if veinte['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veinte['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = veinte['HEN'].strftime(formato1)
    
        if veinte['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = veinte['HDYI'].strftime(formato1)
    
        if veinte['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = veinte['HDYF'].strftime(formato1)
    
        if veinte['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = veinte['HALI'].strftime(formato1)
    
        if veinte['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = veinte['HALF'].strftime(formato1)
    
        if veinte['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = veinte['HPAI'].strftime(formato1)
    
        if veinte['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = veinte['HPAF'].strftime(formato1)
    
        if veinte['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = veinte['HDCI'].strftime(formato1)
    
        if veinte['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = veinte['HDCF'].strftime(formato1)
    
        if veinte['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = veinte['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if veinte['EN'].month ==  d.festivos.month and veinte['EN'].year == d.festivos.year:
                if d.festivos.day ==  veinte['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if veinte['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if veinte['EN'].day == 20:
            veinte20= veinte['EN'].strftime(formato2)
            detalles20 = [('20 '+ veinte20, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles20 = [(20, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTIUNO
        if veintiuno['HEN'] != time(00, 00, 00) and veintiuno['HSA'] != time(00, 00, 00):
            horasTrabajadas = veintiuno['HSA'].hour - veintiuno['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintiuno['HEN'] != time(00, 00, 00) and veintiuno['HSA'] != time(00, 00, 00):
            minutosTrabajadas = veintiuno['HSA'].minute - veintiuno['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintiuno['HALI'] != time(00, 00, 00) and veintiuno['HALF'] != time(00, 00, 00):
            horasAlmuerzo = veintiuno['HALF'].hour -veintiuno['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintiuno['HALF'] != time(00, 00, 00) and veintiuno['HALI'] != time(00, 00, 00):
            minutosAlmuerzo = veintiuno['HALF'].minute -veintiuno['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if veintiuno['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintiuno['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = veintiuno['HEN'].strftime(formato1)
    
        if veintiuno['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = veintiuno['HDYI'].strftime(formato1)
    
        if veintiuno['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = veintiuno['HDYF'].strftime(formato1)
    
        if veintiuno['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = veintiuno['HALI'].strftime(formato1)
    
        if veintiuno['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = veintiuno['HALF'].strftime(formato1)
    
        if veintiuno['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = veintiuno['HPAI'].strftime(formato1)
    
        if veintiuno['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = veintiuno['HPAF'].strftime(formato1)
    
        if veintiuno['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = veintiuno['HDCI'].strftime(formato1)
    
        if veintiuno['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = veintiuno['HDCF'].strftime(formato1)
    
        if veintiuno['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = veintiuno['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if veintiuno['EN'].month ==  d.festivos.month and veintiuno['EN'].year == d.festivos.year:
                if d.festivos.day ==  veintiuno['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if veintiuno['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if veintiuno['EN'].day == 21:
            veintiuno21= veintiuno['EN'].strftime(formato2)
            detalles21 = [('21 '+ veintiuno21, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles21 = [(21, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #VEINTIDOS
        if veintidos['HEN'] != time(00, 00, 00) and veintidos['HSA'] != time(00, 00, 00):
            horasTrabajadas = veintidos['HSA'].hour - veintidos['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintidos['HEN'] != time(00, 00, 00) and veintidos['HSA'] != time(00, 00, 00):
            minutosTrabajadas = veintidos['HSA'].minute - veintidos['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintidos['HALI'] != time(00, 00, 00) and veintidos['HALF'] != time(00, 00, 00):
            horasAlmuerzo = veintidos['HALF'].hour -veintidos['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintidos['HALF'] != time(00, 00, 00) and veintidos['HALI'] != time(00, 00, 00):
            minutosAlmuerzo = veintidos['HALF'].minute -veintidos['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if veintidos['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintidos['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = veintidos['HEN'].strftime(formato1)
    
        if veintidos['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = veintidos['HDYI'].strftime(formato1)
    
        if veintidos['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = veintidos['HDYF'].strftime(formato1)
    
        if veintidos['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = veintidos['HALI'].strftime(formato1)
    
        if veintidos['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = veintidos['HALF'].strftime(formato1)
    
        if veintidos['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = veintidos['HPAI'].strftime(formato1)
    
        if veintidos['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = veintidos['HPAF'].strftime(formato1)
    
        if veintidos['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = veintidos['HDCI'].strftime(formato1)
    
        if veintidos['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = veintidos['HDCF'].strftime(formato1)
    
        if veintidos['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = veintidos['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if veintidos['EN'].month ==  d.festivos.month and veintidos['EN'].year == d.festivos.year:
                if d.festivos.day ==  veintidos['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
        
        if veintidos['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if veintidos['EN'].day == 22:
            veintidos22= veintidos['EN'].strftime(formato2)
            detalles22 = [('22 '+veintidos22, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles22 = [(22 , 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #VEINTITRES
        if veintitres['HEN'] != time(00, 00, 00) and veintitres['HSA'] != time(00, 00, 00):
            horasTrabajadas = veintitres['HSA'].hour - veintitres['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintitres['HEN'] != time(00, 00, 00) and veintitres['HSA'] != time(00, 00, 00):
            minutosTrabajadas = veintitres['HSA'].minute - veintitres['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintitres['HALI'] != time(00, 00, 00) and veintitres['HALF'] != time(00, 00, 00):
            horasAlmuerzo = veintitres['HALF'].hour -veintitres['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintitres['HALI'] != time(00, 00, 00) and veintitres['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = veintitres['HALF'].minute -veintitres['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if veintitres['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintitres['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = veintitres['HEN'].strftime(formato1)
    
        if veintitres['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = veintitres['HDYI'].strftime(formato1)
    
        if veintitres['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = veintitres['HDYF'].strftime(formato1)
    
        if veintitres['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = veintitres['HALI'].strftime(formato1)
    
        if veintitres['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = veintitres['HALF'].strftime(formato1)
    
        if veintitres['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = veintitres['HPAI'].strftime(formato1)
    
        if veintitres['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = veintitres['HPAF'].strftime(formato1)
    
        if veintitres['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = veintitres['HDCI'].strftime(formato1)
    
        if veintitres['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = veintitres['HDCF'].strftime(formato1)
    
        if veintitres['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = veintitres['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if veintitres['EN'].month ==  d.festivos.month and veintitres['EN'].year == d.festivos.year:
                if d.festivos.day ==  veintitres['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if veintitres['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if veintitres['EN'].day == 23:
            veintitres23= veintitres['EN'].strftime(formato2)
            detalles23 = [('23 '+veintitres23, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles23 = [(23, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTICUATRO
        if veinticuatro['HEN'] != time(00, 00, 00) and veinticuatro['HSA'] != time(00, 00, 00):
            horasTrabajadas = veinticuatro['HSA'].hour - veinticuatro['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veinticuatro['HEN'] != time(00, 00, 00) and veinticuatro['HSA'] != time(00, 00, 00):
            minutosTrabajadas = veinticuatro['HSA'].minute - veinticuatro['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veinticuatro['HALI'] != time(00, 00, 00) and veinticuatro['HALF'] != time(00, 00, 00):
            horasAlmuerzo = veinticuatro['HALF'].hour -veinticuatro['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veinticuatro['HALI'] != time(00, 00, 00) and veinticuatro['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = veinticuatro['HALF'].minute -veinticuatro['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if veinticuatro['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veinticuatro['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = veinticuatro['HEN'].strftime(formato1)
    
        if veinticuatro['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = veinticuatro['HDYI'].strftime(formato1)
    
        if veinticuatro['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = veinticuatro['HDYF'].strftime(formato1)
    
        if veinticuatro['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = veinticuatro['HALI'].strftime(formato1)
    
        if veinticuatro['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = veinticuatro['HALF'].strftime(formato1)
    
        if veinticuatro['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = veinticuatro['HPAI'].strftime(formato1)
    
        if veinticuatro['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = veinticuatro['HPAF'].strftime(formato1)
    
        if veinticuatro['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = veinticuatro['HDCI'].strftime(formato1)
    
        if veinticuatro['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = veinticuatro['HDCF'].strftime(formato1)
    
        if veinticuatro['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = veinticuatro['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if veinticuatro['EN'].month ==  d.festivos.month and veinticuatro['EN'].year == d.festivos.year:
                if d.festivos.day ==  veinticuatro['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if veinticuatro['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if veinticuatro['EN'].day == 24:
            veinticuatro24= veinticuatro['EN'].strftime(formato2)
            detalles24 = [('24 '+veinticuatro24, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles24 = [(24,'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #VEINTICINCO
        if veinticinco['HEN'] != time(00, 00, 00) and veinticinco['HSA'] != time(00, 00, 00):
            horasTrabajadas = veinticinco['HSA'].hour - veinticinco['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veinticinco['HEN'] != time(00, 00, 00) and veinticinco['HSA'] != time(00, 00, 00):
            minutosTrabajadas = veinticinco['HSA'].minute - veinticinco['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veinticinco['HALI'] != time(00, 00, 00) and veinticinco['HALF'] != time(00, 00, 00):
            horasAlmuerzo = veinticinco['HALF'].hour -veinticinco['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veinticinco['HALI'] != time(00, 00, 00) and veinticinco['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = veinticinco['HALF'].minute -veinticinco['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if veinticinco['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veinticinco['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = veinticinco['HEN'].strftime(formato1)
    
        if veinticinco['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = veinticinco['HDYI'].strftime(formato1)
    
        if veinticinco['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = veinticinco['HDYF'].strftime(formato1)
    
        if veinticinco['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = veinticinco['HALI'].strftime(formato1)
    
        if veinticinco['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = veinticinco['HALF'].strftime(formato1)
    
        if veinticinco['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = veinticinco['HPAI'].strftime(formato1)
    
        if veinticinco['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = veinticinco['HPAF'].strftime(formato1)
    
        if veinticinco['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = veinticinco['HDCI'].strftime(formato1)
    
        if veinticinco['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = veinticinco['HDCF'].strftime(formato1)
    
        if veinticinco['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = veinticinco['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if veinticinco['EN'].month ==  d.festivos.month and veinticinco['EN'].year == d.festivos.year:
                if d.festivos.day == veinticinco['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if veinticinco['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
    
        if veinticinco['EN'].day == 25:
            veinticinco25= veinticinco['EN'].strftime(formato2)
            detalles25 = [('25 '+veinticinco25, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles25 = [(25, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTISEIS
        if veintiseis['HEN'] != time(00, 00, 00) and veintiseis['HSA'] != time(00, 00, 00):
            horasTrabajadas = veintiseis['HSA'].hour - veintiseis['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintiseis['HEN'] != time(00, 00, 00) and veintiseis['HSA'] != time(00, 00, 00):
            minutosTrabajadas = veintiseis['HSA'].minute - veintiseis['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintiseis['HALI'] != time(00, 00, 00) and veintiseis['HALF'] != time(00, 00, 00):
            horasAlmuerzo = veintiseis['HALF'].hour -veintiseis['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintiseis['HALI'] != time(00, 00, 00) and veintiseis['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = veintiseis['HALF'].minute -veintiseis['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if veintiseis['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintiseis['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = veintiseis['HEN'].strftime(formato1)
    
        if veintiseis['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = veintiseis['HDYI'].strftime(formato1)
    
        if veintiseis['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = veintiseis['HDYF'].strftime(formato1)
    
        if veintiseis['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = veintiseis['HALI'].strftime(formato1)
    
        if veintiseis['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = veintiseis['HALF'].strftime(formato1)
    
        if veintiseis['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = veintiseis['HPAI'].strftime(formato1)
    
        if veintiseis['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = veintiseis['HPAF'].strftime(formato1)
    
        if veintiseis['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = veintiseis['HDCI'].strftime(formato1)
    
        if veintiseis['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = veintiseis['HDCF'].strftime(formato1)
    
        if veintiseis['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = veintiseis['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if veintiseis['EN'].month ==  d.festivos.month and veintiseis['EN'].year == d.festivos.year:
                if d.festivos.day ==  veintiseis['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if veintiseis['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
        
        if veintiseis['EN'].day == 26:
            veintiseis26= veintiseis['EN'].strftime(formato2)
            detalles26 = [('26 '+veintiseis26, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles26 = [(26, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTISIETE
        if veintisiete['HEN'] != time(00, 00, 00) and veintisiete['HSA'] != time(00, 00, 00):
            horasTrabajadas = veintisiete['HSA'].hour - veintisiete['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintisiete['HEN'] != time(00, 00, 00) and veintisiete['HSA'] != time(00, 00, 00):
            minutosTrabajadas = veintisiete['HSA'].minute - veintisiete['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintisiete['HALI'] != time(00, 00, 00) and veintisiete['HALF'] != time(00, 00, 00):
            horasAlmuerzo = veintisiete['HALF'].hour -veintisiete['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintisiete['HALI'] != time(00, 00, 00) and veintisiete['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = veintisiete['HALF'].minute -veintisiete['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if veintisiete['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintisiete['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = veintisiete['HEN'].strftime(formato1)

        if veintisiete['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = veintisiete['HDYI'].strftime(formato1)

        if veintisiete['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = veintisiete['HDYF'].strftime(formato1)

        if veintisiete['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = veintisiete['HALI'].strftime(formato1)

        if veintisiete['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = veintisiete['HALF'].strftime(formato1)

        if veintisiete['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = veintisiete['HPAI'].strftime(formato1)

        if veintisiete['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = veintisiete['HPAF'].strftime(formato1)

        if veintisiete['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = veintisiete['HDCI'].strftime(formato1)

        if veintisiete['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = veintisiete['HDCF'].strftime(formato1)

        if veintisiete['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = veintisiete['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if veintisiete['EN'].month ==  d.festivos.month and veintisiete['EN'].year == d.festivos.year:
                if d.festivos.day ==  veintisiete['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if veintisiete['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60  

        if veintisiete['EN'].day == 27:
            veintisiete27= veintisiete['EN'].strftime(formato2)
            detalles27 = [('27 '+veintisiete27, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles27 = [(27, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTIOCHO
        if veintiocho['HEN'] != time(00, 00, 00) and veintiocho['HSA'] != time(00, 00, 00):
            horasTrabajadas = veintiocho['HSA'].hour - veintiocho['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintiocho['HEN'] != time(00, 00, 00) and veintiocho['HSA'] != time(00, 00, 00):
            minutosTrabajadas = veintiocho['HSA'].minute - veintiocho['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintiocho['HALI'] != time(00, 00, 00) and veintiocho['HALF'] != time(00, 00, 00):
            horasAlmuerzo = veintiocho['HALF'].hour -veintiocho['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintiocho['HALI'] != time(00, 00, 00) and veintiocho['HALF'] != time(00, 00, 00):
            minutosAlmuerzo = veintiocho['HALF'].minute -veintiocho['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if veintiocho['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        
        if veintiocho['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = veintiocho['HEN'].strftime(formato1)

        if veintiocho['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = veintiocho['HDYI'].strftime(formato1)

        if veintiocho['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = veintiocho['HDYF'].strftime(formato1)

        if veintiocho['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  =veintiocho['HALI'].strftime(formato1)

        if veintiocho['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = veintiocho['HALF'].strftime(formato1)

        if veintiocho['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = veintiocho['HPAI'].strftime(formato1)

        if veintiocho['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  =veintiocho['HPAF'].strftime(formato1)

        if veintiocho['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  =veintiocho['HDCI'].strftime(formato1)

        if veintiocho['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = veintiocho['HDCF'].strftime(formato1)

        if veintiocho['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = veintiocho['HSA'].strftime(formato1)
             
        cont = 0
        for d in festivos:
            if veintiocho['EN'].month ==  d.festivos.month and veintiocho['EN'].year == d.festivos.year:
                if d.festivos.day ==  veintiocho['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if veintiocho['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60

        if veintiocho['EN'].day == 28:
            veintiocho28= veintiocho['EN'].strftime(formato2)
            detalles28 = [('28 '+veintiocho28, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles28 = [(28, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTINUEVE
        if veintinueve['HEN'] != time(00, 00, 00) and veintinueve['HSA'] != time(00, 00, 00):
            horasTrabajadas = veintinueve['HSA'].hour - veintinueve['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintinueve['HEN'] != time(00, 00, 00) and veintinueve['HSA'] != time(00, 00, 00):
            minutosTrabajadas = veintinueve['HSA'].minute - veintinueve['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintinueve['HALI'] != time(00, 00, 00) and veintinueve['HALF'] != time(00, 00, 00):
            horasAlmuerzo = veintinueve['HALF'].hour -veintinueve['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintinueve['HALF'] != time(00, 00, 00) and veintinueve['HALI'] != time(00, 00, 00):
            minutosAlmuerzo = veintinueve['HALF'].minute -veintinueve['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        """
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        """
        #HORAS
        #if horasAlmuerzo < 0:
        #    horasAlmuerzo = -horasAlmuerzo

        #if horasTrabajadas < 0:
        #    horasTrabajadas = -horasTrabajadas
        """
        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if veintinueve['HSA'] == 'NA':
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintinueve['HDYI'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = veintinueve['HDYI'].strftime(formato1)

        if veintinueve['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = veintinueve['HEN'].strftime(formato1)

        if veintinueve['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = veintinueve['HDYI'].strftime(formato1)

        if veintinueve['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = veintinueve['HDYF'].strftime(formato1)

        if veintinueve['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = veintinueve['HALI'].strftime(formato1)

        if veintinueve['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = veintinueve['HALF'].strftime(formato1)

        if veintinueve['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = veintinueve['HPAI'].strftime(formato1)

        if veintinueve['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = veintinueve['HPAF'].strftime(formato1)

        if veintinueve['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = veintinueve['HDCI'].strftime(formato1)

        if veintinueve['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = veintinueve['HDCF'].strftime(formato1)

        if veintinueve['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = veintinueve['HSA'].strftime(formato1)
        
        cont = 0
        for d in festivos:
            if veintinueve['EN'].month ==  d.festivos.month and veintinueve['EN'].year == d.festivos.year:
                if d.festivos.day ==  veintinueve['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
            
        if veintinueve['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60    

        if veintinueve['EN'].day == 29:
            veintinueve29= veintinueve['EN'].strftime(formato2)
            detalles29 = [('29 '+veintinueve29, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles29 = [(29,'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]



        #TREINTA
        if treinta['HEN'] != time(00, 00, 00)and treinta['HSA'] != time(00, 00, 00):
            horasTrabajadas = treinta['HSA'].hour - treinta['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if treinta['HEN'] != time(00, 00, 00) and treinta['HSA'] != time(00, 00, 00):
            minutosTrabajadas = treinta['HSA'].minute - treinta['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if treinta['HALI'] != time(00, 00, 00) and treinta['HALF'] != time(00, 00, 00):
            horasAlmuerzo = treinta['HALF'].hour -treinta['HALI'].hour
        else:
            horasAlmuerzo = 0
        if treinta['HALF'] != time(00, 00, 00) and treinta['HALI'] != time(00, 00, 00):
            minutosAlmuerzo = treinta['HALF'].minute -treinta['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas"""

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1

        """#HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """
        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if treinta['HSA'] == time(00, 00, 00):
            minutosTotal = 0
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if treinta['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = treinta['HEN'].strftime(formato1)

        if treinta['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = treinta['HDYI'].strftime(formato1)

        if treinta['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = treinta['HDYF'].strftime(formato1)

        if treinta['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = treinta['HALI'].strftime(formato1)

        if treinta['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = treinta['HALF'].strftime(formato1)

        if treinta['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = treinta['HPAI'].strftime(formato1)

        if treinta['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = treinta['HPAF'].strftime(formato1)

        if treinta['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = treinta['HDCI'].strftime(formato1)

        if treinta['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = treinta['HDCF'].strftime(formato1)

        if treinta['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = treinta['HSA'].strftime(formato1)
            
        cont = 0
        for d in festivos:
            if treinta['EN'].month ==  d.festivos.month and treinta['EN'].year == d.festivos.year:
                if d.festivos.day ==  treinta['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
                        
        if treinta['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60    

        if treinta['EN'].day == 30:
            treinta30 = treinta['EN'].strftime(formato2)
            detalles30 = [('30 '+treinta30, la, la1, la2, la3, la4, la5, la6, la7,la8, la9, "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles30 = [(30,'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #TREINTAUNO
        if treintauno['HEN'] != time(00, 00, 00) and treintauno['HSA'] != time(00, 00, 00):
            horasTrabajadas = treintauno['HSA'].hour - treintauno['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if treintauno['HEN'] != time(00, 00, 00) and treintauno['HSA'] != time(00, 00, 00):
            minutosTrabajadas = treintauno['HSA'].minute - treintauno['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if treintauno['HALI'] != time(00, 00, 00) and treintauno['HALF'] != time(00, 00, 00):
            horasAlmuerzo = treintauno['HALF'].hour -treintauno['HALI'].hour
        else:
            horasAlmuerzo = 0
        if treintauno['HALF'] != time(00, 00, 00) and treintauno['HALI'] != time(00, 00, 00):
            minutosAlmuerzo = treintauno['HALF'].minute -treintauno['HALI'].minute
        else:
            minutosAlmuerzo = 0

        """#MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        """
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1

        """#HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas
        """

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #SI la hora de salida no esta registrada, no me muestre ningun resultado, ni haga operaciones
        if treintauno['HSA'] == 'NA':
            minutosTotal = 0
        print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        #print(totalMes, totalMesMinutos)
        if treintauno['HEN'] == time(00, 00, 00):
            la = 'NA'
        else:
            la = treintauno['HEN'].strftime(formato1)

        if treintauno['HDYI'] == time(00, 00, 00):
            la1 = 'NA'
        else:
            la1 = treintauno['HDYI'].strftime(formato1)

        if treintauno['HDYF'] == time(00, 00, 00):
            la2 = 'NA'
        else:
            la2 = treintauno['HDYF'].strftime(formato1)

        if treintauno['HALI'] == time(00, 00, 00):
            la3 = 'NA'
        else:
            la3  = treintauno['HALI'].strftime(formato1)

        if treintauno['HALF'] == time(00, 00, 00):
            la4 = 'NA'
        else:
            la4 = treintauno['HALF'].strftime(formato1)

        if treintauno['HPAI'] == time(00, 00, 00):
            la5 = 'NA'
        else:
            la5 = treintauno['HPAI'].strftime(formato1)

        if treintauno['HPAF'] == time(00, 00, 00):
            la6 = 'NA'
        else:
            la6  = treintauno['HPAF'].strftime(formato1)

        if treintauno['HDCI'] == time(00, 00, 00):
            la7 = 'NA'
        else:
            la7  = treintauno['HDCI'].strftime(formato1)

        if treintauno['HDCF'] == time(00, 00, 00):
            la8 = 'NA'
        else:
            la8 = treintauno['HDCF'].strftime(formato1)

        if treintauno['HSA'] == time(00, 00, 00):
            la9 = 'NA'
        else:
            la9 = treintauno['HSA'].strftime(formato1)
        
        cont = 0
        for d in festivos:
            if treintauno['EN'].month ==  d.festivos.month and treintauno['EN'].year == d.festivos.year:
                if d.festivos.day ==  treintauno['EN'].day:
                    cont +=1
                    if cont != 1:
                        pass
                    else:
                        hora_domi_fes = horaTotal + hora_domi_fes
                        min_domi_fes = minutosTotal + min_domi_fes
        
        if treintauno['EN'].strftime(formato2) == 'Sun':
            hora_domi_fes = horaTotal + hora_domi_fes
            min_domi_fes = minutosTotal + min_domi_fes
            
        if min_domi_fes >= 60:
            hora_domi_fes += 1
            min_domi_fes -=60
            
        if treintauno['EN'].day == 31:
            treintauno31= treintauno['EN'].strftime(formato2)
            detalles31 = [('31 '+treintauno31, la, la1, la2, la3, la4, la5, la6, la7, la8, la9, "Horas: "+ str(horaTotal) + " Minutos "+ str(minutosTotal))]
        else:
            detalles31 = [(31, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        totalHoras = [('Total'," ", " ", " ", " "," ", " ", " ", " ","","","Horas: "+ str(totalMes) + " Min: "+ str(totalMesMinutos))]
        total_dominicales_festivos = [('Dominicales y festivos'," ", " ", " ", " "," ", " ", " ", " ","","", "Horas: "+ str(hora_domi_fes) + " Min: "+ str(min_domi_fes))]

        #Establecemos el tamaño de cada una de las columnas de la tabla
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden = Table([encabezados] + detalles1 + detalles2 + detalles3 + detalles4 + detalles5 + detalles6 +  detalles7 + detalles8 + detalles9 + detalles10 + detalles11 + detalles12 + detalles13 +  detalles14 + detalles15 + detalles16 + detalles17 + detalles18 + detalles19 + detalles20 + detalles21 + detalles22 + detalles23 + detalles24 + detalles25 + detalles26 + detalles27 + detalles28 + detalles29 + detalles30 + detalles31+ totalHoras + total_dominicales_festivos, colWidths=[ 1.5* cm, 2.15 * cm, 2.15 * cm, 2.6 * cm, 2.15* cm, 2.6 * cm, 2.8 * cm, 3.4 * cm,2.15* cm, 2.4 * cm, 2.15 * cm, 3.3 * cm, 2.5 * cm])
        #detalle_orden.setStyle([('TEXTCOLOR',(0,1),(0,-1), colors.blue), ('TEXTCOLOR', (1,1), (2,-1),colors.green)])
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(0,0),'LEFT'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -3), 0, colors.black),
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (0, -38), 4.5)
            ]
        ))
        #print("FORMATO2", catorce[i.accion_jornada].strftime(formato2), veinte[i.accion_jornada].strftime(formato2), veintiuno[i.accion_jornada].strftime(formato2), uno[i.accion_jornada].strftime(formato2))
        
        for d in festivos:
            if uno['EN'].month ==  d.festivos.month and uno['EN'].year == d.festivos.year:
                #print("FESTIVOS",d.festivos.day, treintauno['EN'].day)
                #print("MES", d.festivos.month, treintauno['EN'].month)
                #print("AÑO", d.festivos.year, treintauno['EN'].year)
                if d.festivos.day ==  uno['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,1),(11,1),colors.gray)])
            if dos['EN'].month ==  d.festivos.month and dos['EN'].year == d.festivos.year:
                if d.festivos.day ==  dos['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,2),(11,2),colors.gray)])
            if tres['EN'].month ==  d.festivos.month and tres['EN'].year == d.festivos.year:
                if d.festivos.day == tres['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,3),(11,3),colors.gray)])
            if cuatro['EN'].month ==  d.festivos.month and cuatro['EN'].year == d.festivos.year:
                if d.festivos.day == cuatro['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,4),(11,4),colors.gray)])
            if cinco['EN'].month ==  d.festivos.month and cinco['EN'].year == d.festivos.year:
                if d.festivos.day ==  cinco['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,5),(11,5),colors.gray)])
            if seis['EN'].month ==  d.festivos.month and seis['EN'].year == d.festivos.year:
                if d.festivos.day ==  seis['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,6),(11,6),colors.gray)])        
            if siete['EN'].month ==  d.festivos.month and siete['EN'].year == d.festivos.year:
                if d.festivos.day ==  siete['EN'].day:
                     detalle_orden.setStyle([('BACKGROUND',(0,7),(11,7),colors.gray)])
            if ocho['EN'].month ==  d.festivos.month and ocho['EN'].year == d.festivos.year:
                if d.festivos.day == ocho['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,8),(11,8),colors.gray)])
            if nueve['EN'].month ==  d.festivos.month and nueve['EN'].year == d.festivos.year:
                if d.festivos.day == nueve['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,9),(11,9),colors.gray)])
            if diez['EN'].month ==  d.festivos.month and diez['EN'].year == d.festivos.year:
                if d.festivos.day == diez['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,10),(11,10),colors.gray)])
            if once['EN'].month ==  d.festivos.month and once['EN'].year == d.festivos.year:
                if d.festivos.day == once['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,11),(11,11),colors.gray)])
            if doce['EN'].month ==  d.festivos.month and doce['EN'].year == d.festivos.year:
                if d.festivos.day == doce['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,12),(11,12),colors.gray)])
            if trece['EN'].month ==  d.festivos.month and trece['EN'].year == d.festivos.year:
                if d.festivos.day == trece['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,13),(11,13),colors.gray)])
            if catorce['EN'].month ==  d.festivos.month and catorce['EN'].year == d.festivos.year:
                if d.festivos.day == catorce['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,14),(11,14),colors.gray)])        
            if quince['EN'].month ==  d.festivos.month and quince['EN'].year == d.festivos.year:
                if d.festivos.day ==  quince['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,15),(11,15),colors.gray)])
            if dieciseis['EN'].month ==  d.festivos.month and dieciseis['EN'].year == d.festivos.year:
                if d.festivos.day == dieciseis['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,16),(11,16),colors.gray)])
            if diecisiete['EN'].month ==  d.festivos.month and diecisiete['EN'].year == d.festivos.year:
                if d.festivos.day == diecisiete['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,17),(11,17),colors.gray)])
            if dieciocho['EN'].month ==  d.festivos.month and dieciocho['EN'].year == d.festivos.year:
                if d.festivos.day ==  dieciocho['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,18),(11,18),colors.gray)])
            if diecinueve['EN'].month ==  d.festivos.month and diecinueve['EN'].year == d.festivos.year:
                if d.festivos.day ==  diecinueve['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,19),(11,19),colors.gray)])        
            if veinte['EN'].month ==  d.festivos.month and veinte['EN'].year == d.festivos.year:
                if d.festivos.day ==  veinte['EN'].day:
                     detalle_orden.setStyle([('BACKGROUND',(0,20),(11,20),colors.gray)])
            if veintiuno['EN'].month ==  d.festivos.month and veintiuno['EN'].year == d.festivos.year:
                if d.festivos.day == veintiuno['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,21),(11,21),colors.gray)])
            if veintidos['EN'].month ==  d.festivos.month and veintidos['EN'].year == d.festivos.year:
                if d.festivos.day == veintidos['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,22),(11,22),colors.gray)])
            if veintitres['EN'].month ==  d.festivos.month and veintitres['EN'].year == d.festivos.year:
                if d.festivos.day == veintitres['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,23),(11,23),colors.gray)])
            if veinticuatro['EN'].month ==  d.festivos.month and veinticuatro['EN'].year == d.festivos.year:
                if d.festivos.day == veinticuatro['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,24),(11,24),colors.gray)])
            if veinticinco['EN'].month ==  d.festivos.month and veinticinco['EN'].year == d.festivos.year:
                if d.festivos.day == veinticinco['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,25),(11,25),colors.gray)])
            if veintiseis['EN'].month ==  d.festivos.month and veintiseis['EN'].year == d.festivos.year:
                if d.festivos.day == veintiseis['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,26),(11,26),colors.gray)])
            if veintisiete['EN'].month ==  d.festivos.month and veintisiete['EN'].year == d.festivos.year:
                if d.festivos.day == veintisiete['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,27),(11,27),colors.gray)])        
            if veintiocho['EN'].month ==  d.festivos.month and veintiocho['EN'].year == d.festivos.year:
                if d.festivos.day == veintiocho['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,28),(11,28),colors.gray)])
            if veintinueve['EN'].month ==  d.festivos.month and veintinueve['EN'].year == d.festivos.year:
                if d.festivos.day == veintinueve['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,29),(11,29),colors.gray)])
            if treinta['EN'].month ==  d.festivos.month and treinta['EN'].year == d.festivos.year:
                if d.festivos.day == treinta['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,30),(11,30),colors.gray)])
            if treintauno['EN'].month ==  d.festivos.month and treintauno['EN'].year == d.festivos.year:
                if d.festivos.day == treintauno['EN'].day:
                    detalle_orden.setStyle([('BACKGROUND',(0,31),(11,31),colors.gray)])
        
        if uno['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,1),(11,1),colors.gray)])
        if dos['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,2),(11,2),colors.gray)])
        if tres['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,3),(11,3),colors.gray)])
        if cuatro['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,4),(11,4),colors.gray)])
        if cinco['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,5),(11,5),colors.gray)])
        if seis['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,6),(11,6),colors.gray)])
        if siete['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,7),(11,7),colors.gray)])
        if ocho['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,8),(11,8),colors.gray)])    
        if nueve['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,9),(11,9),colors.gray)])    
        if diez['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,10),(11,10),colors.gray)])    
        if once['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,11),(11,11),colors.gray)])    
        if doce['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,12),(11,12),colors.gray)])    
        if trece['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,13),(11,13),colors.gray)])      
        if catorce['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,14),(11,14),colors.gray)])
        if quince['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,15),(11,15),colors.gray)])    
        if dieciseis['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,16),(11,16),colors.gray)])    
        if diecisiete['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,17),(11,17),colors.gray)])    
        if dieciocho['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,18),(11,18),colors.gray)])      
        if diecinueve['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,19),(11,19),colors.gray)])    
        if veinte['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,20),(11,20),colors.gray)])    
        if veintiuno['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,21),(11,21),colors.gray)])    
        if veintidos['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,22),(11,22),colors.gray)])
        if veintitres['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,23),(11,23),colors.gray)])    
        if veinticuatro['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,24),(11,24),colors.gray)])      
        if veinticinco['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,25),(11,25),colors.gray)])    
        if veintiseis['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,26),(11,26),colors.gray)])    
        if veintisiete['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,27),(11,27),colors.gray)])    
        if veintiocho['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,28),(11,28),colors.gray)])
        if veintinueve['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,29),(11,29),colors.gray)])
        if treinta['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,30),(11,30),colors.gray)])
        if treintauno['EN'].strftime(formato2) == 'Sun':
            detalle_orden.setStyle([('BACKGROUND',(0,31),(11,31),colors.gray)])    
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 23,25)

    def get(self, request, *args, **kwargs):
        #f = request.GET['cedula']
        #print("F con F",value)
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.setPageSize((950,750))
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        """if 'cedula' in request.GET and 'mes' in request.GET:
            cedula = request.GET['cedula']
            mes = request.GET['mes']
            print( "Mes" ,mes)
            if not cedula and not mes:
                errors.append('Colaborador no encontrado.')
            else:
                Colaborador = Historial_IO.objects.filter(id_trabajadores__cedula=cedula)
                Mes = Historial_IO.objects.filter(fecha__month=mes)
               return response
            """
        return response


"""
def report(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment; filename=report.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)

	#Cabecera del archivo

	c.setLineWidth(.3)
	c.setFont('Helvetica',22)
	c.drawString(30, 750, 'Siete')
	c.setFont('Helvetica', 12)
	c.drawString(30, 735, 'Colinas')
	c.setFont('Helvetica-Bold', 12)
	c.drawString(480, 750, '09/01/2018')
	c.line(460, 747, 560, 747)

	#Tabla Estudiante

	students=[
		{'#':'1', 'name':'Miguel Rodriguez', 'b1':'3.4', 'b2':'2.2', 'b3': '4.5', 'Total':'3.36'},
		{'#':'2', 'name':'Felipe Andrade', 'b1':'4.3', 'b2':'2.6', 'b3':'4.6', 'Total':'3.83'},
		{'#':'3', 'name':'Carlos Florez', 'b1':'2.1', 'b2':'4.3', 'b3': '4.9', 'Total':'3.76'},
		{'#':'4', 'name':'Raul Cardona', 'b1':'5.0', 'b2':'4.7', 'b3':'4.5', 'Total':'4.7'},
		{'#':'5', 'name':'Humberto Rangel', 'b1':'3.3', 'b2':'4.9', 'b3':'4.9', 'Total':'4.36'}

		]

	#Cabecera de la tabla
	styles = getSampleStyleSheet()
	styleBH = styles["Normal"]
	styleBH.aligment = TA_CENTER
	styleBH.fontSize = 10

	numero = Paragraph(''' # ''', styleBH)
	alumno = Paragraph(''' Alumno ''', styleBH)
	b1 = Paragraph('''BIM1''', styleBH)
	b2 = Paragraph('''BIM2''', styleBH)
	b3 = Paragraph('''BIM3''', styleBH)
	Total = Paragraph('''Promedio''', styleBH)

	#tabla
	styles = getSampleStyleSheet()
	styleN = styles["BodyText"]
	styleBH.aligment = TA_CENTER
	styleBH.fontSize = 7

	width, height = A4
	high = 650

	data = []
	data.append([numero, alumno, b1,b2,b3,Total])

	for student in students:
		this_student = [student['#'], student['name'], student['b1'], student['b2'], student['b3'], student['Total']]
		data.append(this_student)
		high = high-18

		#Tamano de la Tabla
		table = Table(data, colWidths = [1.8*cm, 9.5*cm, 1.9*cm, 1.9*cm, 2.0*cm])
		table.setStyle(TableStyle([
			#estilos de la Tabla
			('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
			('BOX', (0,0), (-1,-1), 0.25, colors.black),
		]))
	table.wrapOn(c, width, height)
	table.drawOn(c, 30, high)
	c.showPage()

	c.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response #HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
"""

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
        existe_colaborador.values('fechaNacimiento')
        if not q:
            errors.append('Por favor introduce un termino de búsqueda.')
            print(errors)
        else:
            trabajadores = Trabajadores.objects.filter(CodigoBarras=q)

            #modelo=Historial_IO.objects.all()
           #print(trabajadores.values()[0])
            if trabajadores.count() > 0:
                try:
                    id = trabajadores.get().id
                except:
                    quit()
                #print(id)
            else:
                if not existe_colaborador.count() != 0:
                    errors.append('Por favor registre primero un Colaborador.')
                else:
                    errors.append('Colaborador no encontrado.')
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


            fecha= date.today().day
            fecha_trabajadores = Historial_IO.objects.all()

            #print(cp)
            #params = urllib.urlencode(cp)
            #print(params)
            context = {
                'form': form,
                'trabajadores': trabajadores,
                'query': q,
                'errors':errors,
            }
            lis = []
            for g in fecha_trabajadores:
                for n in trabajadores:
                    if g.fecha.day == fecha:
                        if g.id_trabajadores.cedula == n.cedula:
                            print(g.accion_jornada, n.cedula)
                            lis.append(g.accion_jornada)
            #print(lis, "Sigeee")
            if request.method == 'POST':
                if form.is_valid():
                    existe_sa= Historial_IO.objects.all()
                    instance = form.save(commit=False)
                    accion_jornada = instance.accion_jornada

                    print(lis, "Despues")
                    if 'SA' in lis:
                        errors.append("Usted ya registro SALIDA, no podrá ingresar mas datos.")
                        instance = form.save(commit=False)
                    else:
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
                        mensaje_exitoso.append('Se ha registrado con éxito !')
                        success=True

                        #return HttpResponseRedirect('',mensaje_exitoso)
                        return redirect('registrarJornada')
                        #return render(request,'registrarJornada/registrarJornada.html', {'mensaje': mensaje_exitoso})
                        # print(form)
                else:
                    print('no entra')
                    print(form.errors)
                    errors.append('La acción ya se encuentra registrada en este día.')
            return render(request, 'registrarJornada/registrarJornada.html',context)

    return render(request, 'registrarJornada/registrarJornada.html', {'errors': errors})
