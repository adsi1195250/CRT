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
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape

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
"""
class CrearTrabajador(CreateView):
    model = Trabajadores
    template_name = 'Trabajadores/trabajador_modal.html'
    form_class = trabajadoresForms
    success_url = reverse_lazy('listado_trabajadores')
"""
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
                    #print("Month" ,p.fecha.month)
               
                ja = False
                if int(qames) in lis:
                    ja = True
                else:
                    ja = False
                    errors['error'] = ('El Colaborador no tiene registro en este fecha.')        

                lis_nombres = []
                existe = []
                
                for m in existe_colaborador:
                    existe.append(m)
                
                for k in q:
                    lis_nombres.append(k.id_trabajadores.nombres)
                
                if q.count() <=0:
                    errors['error'] =('Colaborador no encontrado.')
                
                #print("no ha nada", q.count())
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
                for i in q:
                    mes1 = i
                    for mes in filtroMes:
                        if mes == mes1:
                            fq = i.fecha.day
                            #fqmes = i.fecha.month
                            #print("Mes",mes.fecha.month)
                            a['nombre'] = i.id_trabajadores.nombres
                            a['cedula'] = i.id_trabajadores.cedula
                            a['mes'] = mes.fecha.month
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

                #print("Here",fq)
                #if fq == 5:
                #   j[i.accion_jornada] = i.hora

                #print("None",i)
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
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.STATIC_ROOT+'/img/index.jpg'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 640, 120, 80,preserveAspectRatio=True)
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 25)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(300, 670, u"Siete Colinas S.A.S")
        pdf.line(300, 662, 545, 662)
        pdf.setFont("Helvetica", 14)
        pdf.drawString(300, 645 , u"REPORTE DE REGISTRO JORNADA")
        pdf.setFont("Helvetica", 18)
        pdf.drawString(740, 700, u"Colaborador:")
        pdf.setFont("Helvetica", 15)
        #print(filtroMes)
        for jh in q:
            jnombre = jh.id_trabajadores.nombres
            jcedula = jh.id_trabajadores.cedula
        pdf.drawString(700,674, jnombre)
        pdf.setFont("Helvetica", 14)
        pdf.drawString(760, 650, u"Cedula:")
        pdf.setFont("Helvetica", 15)
        pdf.drawString(742,630, jcedula)

    def tabla(self,pdf,y):

        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Día', 'Entrada', 'Desayuno', 'Fin desayuno', 'Almuerzo', 'Fin Almuerzo', 'Pausas Activas', 'Fin pausas activas', 'Descanso', 'Fin Descanso', 'Salida', 'Horas Trabajadas')
        #Creamos una lista de tuplas que van a contener a las personas
        q = Historial_IO.objects.filter(id_trabajadores__cedula=self.request.GET.get('cedula'))
        filtroMes = Historial_IO.objects.filter(fecha__month=self.request.GET.get('mes'))
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

        uno['EN'] = date(12, 1, 2)
        uno['HEN'] = 'NA'
        uno['HDYI'] = 'NA'
        uno['HDYF'] = 'NA'
        uno['HALI'] = 'NA'
        uno['HALF'] = 'NA'
        uno['HPAI'] = 'NA'
        uno['HPAF'] = 'NA'
        uno['HDCI'] = 'NA'
        uno['HDCF'] = 'NA'
        uno['HSA'] = 'NA'

        dos['EN'] = date(12, 1, 1)
        dos['HEN'] = 'NA'
        dos['HDYI'] = 'NA'
        dos['HDYF'] = 'NA'
        dos['HALI'] = 'NA'
        dos['HALF'] = 'NA'
        dos['HPAI'] = 'NA'
        dos['HPAF'] = 'NA'
        dos['HDCI'] = 'NA'
        dos['HDCF'] = 'NA'
        dos['HSA'] = 'NA'


        tres['EN'] = date(12, 1, 1)
        tres['HEN'] = 'NA'
        tres['HDYI'] = 'NA'
        tres['HDYF'] = 'NA'
        tres['HALI'] = 'NA'
        tres['HALF'] = 'NA'
        tres['HPAI'] = 'NA'
        tres['HPAF'] = 'NA'
        tres['HDCI'] = 'NA'
        tres['HDCF'] = 'NA'
        tres['HSA'] = 'NA'

        cuatro['EN'] = date(12, 1, 1)
        cuatro['HEN'] = 'NA'
        cuatro['HDYI'] = 'NA'
        cuatro['HDYF'] = 'NA'
        cuatro['HALI'] = 'NA'
        cuatro['HALF'] = 'NA'
        cuatro['HPAI'] = 'NA'
        cuatro['HPAF'] = 'NA'
        cuatro['HDCI'] = 'NA'
        cuatro['HDCF'] = 'NA'
        cuatro['HSA'] = 'NA'


        cinco['EN'] = date(12, 1, 1)
        cinco['HEN'] = 'NA'
        cinco['HDYI'] = 'NA'
        cinco['HDYF'] = 'NA'
        cinco['HALI'] = 'NA'
        cinco['HALF'] = 'NA'
        cinco['HPAI'] = 'NA'
        cinco['HPAF'] = 'NA'
        cinco['HDCI'] = 'NA'
        cinco['HDCF'] = 'NA'
        cinco['HSA'] = 'NA'

        seis['EN'] = date(12, 1, 1)
        seis['HEN'] = 'NA'
        seis['HDYI'] = 'NA'
        seis['HDYF'] = 'NA'
        seis['HALI'] = 'NA'
        seis['HALF'] = 'NA'
        seis['HPAI'] = 'NA'
        seis['HPAF'] = 'NA'
        seis['HDCI'] = 'NA'
        seis['HDCF'] = 'NA'
        seis['HSA'] = 'NA'

        siete['EN'] = date(12, 1, 1)
        siete['HEN'] = 'NA'
        siete['HDYI'] = 'NA'
        siete['HDYF'] = 'NA'
        siete['HALI'] = 'NA'
        siete['HALF'] = 'NA'
        siete['HPAI'] = 'NA'
        siete['HPAF'] = 'NA'
        siete['HDCI'] = 'NA'
        siete['HDCF'] = 'NA'
        siete['HSA'] = 'NA'

        ocho['EN'] = date(12, 1, 1)
        ocho['HEN'] = 'NA'
        ocho['HDYI'] = 'NA'
        ocho['HDYF'] = 'NA'
        ocho['HALI'] = 'NA'
        ocho['HALF'] = 'NA'
        ocho['HPAI'] = 'NA'
        ocho['HPAF'] = 'NA'
        ocho['HDCI'] = 'NA'
        ocho['HDCF'] = 'NA'
        ocho['HSA'] = 'NA'

        nueve['EN'] = date(12, 1, 1)
        nueve['HEN'] = 'NA'
        nueve['HDYI'] = 'NA'
        nueve['HDYF'] = 'NA'
        nueve['HALI'] = 'NA'
        nueve['HALF'] = 'NA'
        nueve['HPAI'] = 'NA'
        nueve['HPAF'] = 'NA'
        nueve['HDCI'] = 'NA'
        nueve['HDCF'] = 'NA'
        nueve['HSA'] = 'NA'

        diez['EN'] = date(12, 1, 1)
        diez['HEN'] = 'NA'
        diez['HDYI'] = 'NA'
        diez['HDYF'] = 'NA'
        diez['HALI'] = 'NA'
        diez['HALF'] = 'NA'
        diez['HPAI'] = 'NA'
        diez['HPAF'] = 'NA'
        diez['HDCI'] = 'NA'
        diez['HDCF'] = 'NA'
        diez['HSA'] = 'NA'

        once['EN'] = date(12, 1, 1)
        once['HEN'] = 'NA'
        once['HDYI'] = 'NA'
        once['HDYF'] = 'NA'
        once['HALI'] = 'NA'
        once['HALF'] = 'NA'
        once['HPAI'] = 'NA'
        once['HPAF'] = 'NA'
        once['HDCI'] = 'NA'
        once['HDCF'] = 'NA'
        once['HSA'] = 'NA'

        doce['EN'] = date(12, 1, 1)
        doce['HEN'] = 'NA'
        doce['HDYI'] = 'NA'
        doce['HDYF'] = 'NA'
        doce['HALI'] = 'NA'
        doce['HALF'] = 'NA'
        doce['HPAI'] = 'NA'
        doce['HPAF'] = 'NA'
        doce['HDCI'] = 'NA'
        doce['HDCF'] = 'NA'
        doce['HSA'] = 'NA'

        trece['EN'] = date(12, 1, 1)
        trece['HEN'] = 'NA'
        trece['HDYI'] = 'NA'
        trece['HDYF'] = 'NA'
        trece['HALI'] = 'NA'
        trece['HALF'] = 'NA'
        trece['HPAI'] = 'NA'
        trece['HPAF'] = 'NA'
        trece['HDCI'] = 'NA'
        trece['HDCF'] = 'NA'
        trece['HSA'] = 'NA'


        catorce['EN'] = date(12, 1, 1)
        catorce['HEN'] = 'NA'
        catorce['HDYI'] = 'NA'
        catorce['HDYF'] = 'NA'
        catorce['HALI'] = 'NA'
        catorce['HALF'] = 'NA'
        catorce['HPAI'] = 'NA'
        catorce['HPAF'] = 'NA'
        catorce['HDCI'] = 'NA'
        catorce['HDCF'] = 'NA'
        catorce['HSA'] = 'NA'

        quince['EN'] = date(12, 1, 1)
        quince['HEN'] = 'NA'
        quince['HDYI'] = 'NA'
        quince['HDYF'] = 'NA'
        quince['HALI'] = 'NA'
        quince['HALF'] = 'NA'
        quince['HPAI'] = 'NA'
        quince['HPAF'] = 'NA'
        quince['HDCI'] = 'NA'
        quince['HDCF'] = 'NA'
        quince['HSA'] = 'NA'


        dieciseis['EN'] = date(12, 1, 1)
        dieciseis['HEN'] = 'NA'
        dieciseis['HDYI'] = 'NA'
        dieciseis['HDYF'] = 'NA'
        dieciseis['HALI'] = 'NA'
        dieciseis['HALF'] = 'NA'
        dieciseis['HPAI'] = 'NA'
        dieciseis['HPAF'] = 'NA'
        dieciseis['HDCI'] = 'NA'
        dieciseis['HDCF'] = 'NA'
        dieciseis['HSA'] = 'NA'

        diecisiete['EN'] = date(12, 1, 1)
        diecisiete['HEN'] = 'NA'
        diecisiete['HDYI'] = 'NA'
        diecisiete['HDYF'] = 'NA'
        diecisiete['HALI'] = 'NA'
        diecisiete['HALF'] = 'NA'
        diecisiete['HPAI'] = 'NA'
        diecisiete['HPAF'] = 'NA'
        diecisiete['HDCI'] = 'NA'
        diecisiete['HDCF'] = 'NA'
        diecisiete['HSA'] = 'NA'

        dieciocho['EN'] = date(12, 1, 1)
        dieciocho['HEN'] = 'NA'
        dieciocho['HDYI'] = 'NA'
        dieciocho['HDYF'] = 'NA'
        dieciocho['HALI'] = 'NA'
        dieciocho['HALF'] = 'NA'
        dieciocho['HPAI'] = 'NA'
        dieciocho['HPAF'] = 'NA'
        dieciocho['HDCI'] = 'NA'
        dieciocho['HDCF'] = 'NA'
        dieciocho['HSA'] = 'NA'

        diecinueve['EN'] = date(12, 1, 1)
        diecinueve['HEN'] = 'NA'
        diecinueve['HDYI'] = 'NA'
        diecinueve['HDYF'] = 'NA'
        diecinueve['HALI'] = 'NA'
        diecinueve['HALF'] = 'NA'
        diecinueve['HPAI'] = 'NA'
        diecinueve['HPAF'] = 'NA'
        diecinueve['HDCI'] = 'NA'
        diecinueve['HDCF'] = 'NA'
        diecinueve['HSA'] = 'NA'

        veinte['EN'] = date(12, 1, 1)
        veinte['HEN'] = 'NA'
        veinte['HDYI'] = 'NA'
        veinte['HDYF'] = 'NA'
        veinte['HALI'] = 'NA'
        veinte['HALF'] = 'NA'
        veinte['HPAI'] = 'NA'
        veinte['HPAF'] = 'NA'
        veinte['HDCI'] = 'NA'
        veinte['HDCF'] = 'NA'
        veinte['HSA'] = 'NA'

        veintiuno['EN'] = date(12, 1, 1)
        veintiuno['HEN'] = 'NA'
        veintiuno['HDYI'] = 'NA'
        veintiuno['HDYF'] = 'NA'
        veintiuno['HALI'] = 'NA'
        veintiuno['HALF'] = 'NA'
        veintiuno['HPAI'] = 'NA'
        veintiuno['HPAF'] = 'NA'
        veintiuno['HDCI'] = 'NA'
        veintiuno['HDCF'] = 'NA'
        veintiuno['HSA'] = 'NA'

        veintidos['EN'] = date(12, 1, 1)
        veintidos['HEN'] = 'NA'
        veintidos['HDYI'] = 'NA'
        veintidos['HDYF'] = 'NA'
        veintidos['HALI'] = 'NA'
        veintidos['HALF'] = 'NA'
        veintidos['HPAI'] = 'NA'
        veintidos['HPAF'] = 'NA'
        veintidos['HDCI'] = 'NA'
        veintidos['HDCF'] = 'NA'
        veintidos['HSA'] = 'NA'

        veintitres['EN'] = date(12, 1, 1)
        veintitres['HEN'] = 'NA'
        veintitres['HDYI'] = 'NA'
        veintitres['HDYF'] = 'NA'
        veintitres['HALI'] = 'NA'
        veintitres['HALF'] = 'NA'
        veintitres['HPAI'] = 'NA'
        veintitres['HPAF'] = 'NA'
        veintitres['HDCI'] = 'NA'
        veintitres['HDCF'] = 'NA'
        veintitres['HSA'] = 'NA'

        veinticuatro['EN'] = date(12, 1, 1)
        veinticuatro['HEN'] = 'NA'
        veinticuatro['HDYI'] = 'NA'
        veinticuatro['HDYF'] = 'NA'
        veinticuatro['HALI'] = 'NA'
        veinticuatro['HALF'] = 'NA'
        veinticuatro['HPAI'] = 'NA'
        veinticuatro['HPAF'] = 'NA'
        veinticuatro['HDCI'] = 'NA'
        veinticuatro['HDCF'] = 'NA'
        veinticuatro['HSA'] = 'NA'


        veinticinco['EN'] = date(12, 1, 1)
        veinticinco['HEN'] = 'NA'
        veinticinco['HDYI'] = 'NA'
        veinticinco['HDYF'] = 'NA'
        veinticinco['HALI'] = 'NA'
        veinticinco['HALF'] = 'NA'
        veinticinco['HPAI'] = 'NA'
        veinticinco['HPAF'] = 'NA'
        veinticinco['HDCI'] = 'NA'
        veinticinco['HDCF'] = 'NA'
        veinticinco['HSA'] = 'NA'

        veintiseis['EN'] = date(12, 1, 1)
        veintiseis['HEN'] = 'NA'
        veintiseis['HDYI'] = 'NA'
        veintiseis['HDYF'] = 'NA'
        veintiseis['HALI'] = 'NA'
        veintiseis['HALF'] = 'NA'
        veintiseis['HPAI'] = 'NA'
        veintiseis['HPAF'] = 'NA'
        veintiseis['HDCI'] = 'NA'
        veintiseis['HDCF'] = 'NA'
        veintiseis['HSA'] = 'NA'

        veintisiete['EN'] = date(12, 1, 1)
        veintisiete['HEN'] = 'NA'
        veintisiete['HDYI'] = 'NA'
        veintisiete['HDYF'] = 'NA'
        veintisiete['HALI'] = 'NA'
        veintisiete['HALF'] = 'NA'
        veintisiete['HPAI'] = 'NA'
        veintisiete['HPAF'] = 'NA'
        veintisiete['HDCI'] = 'NA'
        veintisiete['HDCF'] = 'NA'
        veintisiete['HSA'] = 'NA'

        veintiocho['EN'] = date(12, 1, 1)
        veintiocho['HEN'] = 'NA'
        veintiocho['HDYI'] = 'NA'
        veintiocho['HDYF'] = 'NA'
        veintiocho['HALI'] = 'NA'
        veintiocho['HALF'] = 'NA'
        veintiocho['HPAI'] = 'NA'
        veintiocho['HPAF'] = 'NA'
        veintiocho['HDCI'] = 'NA'
        veintiocho['HDCF'] = 'NA'
        veintiocho['HSA'] = 'NA'

        veintinueve['EN'] = date(12, 1, 1)
        veintinueve['HEN'] = 'NA'
        veintinueve['HDYI'] = 'NA'
        veintinueve['HDYF'] = 'NA'
        veintinueve['HALI'] = 'NA'
        veintinueve['HALF'] = 'NA'
        veintinueve['HPAI'] = 'NA'
        veintinueve['HPAF'] = 'NA'
        veintinueve['HDCI'] = 'NA'
        veintinueve['HDCF'] = 'NA'
        veintinueve['HSA'] = 'NA'

        treinta['EN'] = date(12, 1, 1)
        treinta['HEN'] = 'NA'
        treinta['HDYI'] = 'NA'
        treinta['HDYF'] = 'NA'
        treinta['HALI'] = 'NA'
        treinta['HALF'] = 'NA'
        treinta['HPAI'] = 'NA'
        treinta['HPAF'] = 'NA'
        treinta['HDCI'] = 'NA'
        treinta['HDCF'] = 'NA'
        treinta['HSA'] = 'NA'

        treintauno['EN'] = date(12, 1, 1)
        treintauno['HEN'] = 'NA'
        treintauno['HDYI'] = 'NA'
        treintauno['HDYF'] = 'NA'
        treintauno['HALI'] = 'NA'
        treintauno['HALF'] = 'NA'
        treintauno['HPAI'] = 'NA'
        treintauno['HPAF'] = 'NA'
        treintauno['HDCI'] = 'NA'
        treintauno['HDCF'] = 'NA'
        treintauno['HSA'] = 'NA'

        self.b= []
        #print(filtroMes)
        for i in q:
            mes1 = i
            for mes in filtroMes:
                if mes == mes1:
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

        #TOTAL MES
        totalMes = 0
        totalMesMinutos = 0

        #UNO
        if uno['HEN'] != 'NA' and uno['HSA'] != 'NA':
            horasTrabajadas = uno['HSA'].hour - uno['HEN'].hour
        else:
            horasTrabajadas = 0
        if uno['HEN'] != 'NA' and uno['HSA'] != 'NA':
            minutosTrabajadas = uno['HSA'].minute - uno['HEN'].minute
        else:
            minutosTrabajadas = 0
        if uno['HALI'] != 'NA' and uno['HALF'] != 'NA':
            horasAlmuerzo = uno['HALF'].hour -uno['HALI'].hour
        else:
            horasAlmuerzo = 0
        if uno['HALI'] != 'NA' and uno['HALF'] != 'NA':
            minutosAlmuerzo = uno['HALF'].minute -uno['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if uno['EN'].day == 1:
            detalles1 = [(1, uno['HEN'], uno['HDYI'], uno['HDYF'], uno['HALI'], uno['HALF'], uno['HPAI'], uno['HPAF'], uno['HDCI'],uno['HDCF'], uno['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles1 = [(1 , 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DOS
        if dos['HEN'] != 'NA' and dos['HSA'] != 'NA':
            horasTrabajadas = dos['HSA'].hour - dos['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if dos['HEN'] != 'NA' and dos['HSA'] != 'NA':
            minutosTrabajadas = dos['HSA'].minute - dos['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if dos['HALI'] != 'NA' and dos['HALF'] != 'NA':
            horasAlmuerzo = dos['HALF'].hour -dos['HALI'].hour
        else:
            horasAlmuerzo = 0
        if dos['HALI'] != 'NA' and dos['HALF'] != 'NA':
            minutosAlmuerzo = dos['HALF'].minute -dos['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)     

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos

        if dos['EN'].day == 2:
            detalles2 = [(2, dos['HEN'], dos['HDYI'], dos['HDYF'], dos['HALI'], dos['HALF'], dos['HPAI'], dos['HPAF'], dos['HDCI'],dos['HDCF'], dos['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles2 = [(2 , 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #TRES
        if tres['HEN'] != 'NA' and tres['HSA'] != 'NA':
            horasTrabajadas = tres['HSA'].hour - tres['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if tres['HEN'] != 'NA' and tres['HSA'] != 'NA':
            minutosTrabajadas = tres['HSA'].minute - tres['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if tres['HALI'] != 'NA' and tres['HALF'] != 'NA':
            horasAlmuerzo = tres['HALF'].hour -tres['HALI'].hour
        else:
            horasAlmuerzo = 0
        if tres['HALI'] != 'NA' and tres['HALF'] != 'NA':
            minutosAlmuerzo = tres['HALF'].minute -tres['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)     

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if tres['EN'].day == 3:
            detalles3 = [(3, tres['HEN'], tres['HDYI'], tres['HDYF'], tres['HALI'], tres['HALF'], tres['HPAI'], tres['HPAF'], tres['HDCI'],tres['HDCF'], tres['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles3 = [(3, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #CUATRO
        if cuatro['HEN'] != 'NA' and cuatro['HSA'] != 'NA':
            horasTrabajadas = cuatro['HSA'].hour - cuatro['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if cuatro['HEN'] != 'NA' and cuatro['HSA'] != 'NA':
            minutosTrabajadas = cuatro['HSA'].minute - cuatro['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if cuatro['HALI'] != 'NA' and cuatro['HALF'] != 'NA':
            horasAlmuerzo = cuatro['HALF'].hour -cuatro['HALI'].hour
        else:
            horasAlmuerzo = 0
        if cuatro['HALI'] != 'NA' and cuatro['HALF'] != 'NA':
            minutosAlmuerzo = cuatro['HALF'].minute -cuatro['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if cuatro['EN'].day == 4:
            detalles4 = [(4, cuatro['HEN'], cuatro['HDYI'], cuatro['HDYF'], cuatro['HALI'], cuatro['HALF'], cuatro['HPAI'], cuatro['HPAF'], cuatro['HDCI'], cuatro['HDCF'], cuatro['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles4 = [(4, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #CINCO
        if cinco['HEN'] != 'NA' and cinco['HSA'] != 'NA':
            horasTrabajadas = cinco['HSA'].hour - cinco['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if cinco['HEN'] != 'NA' and cinco['HSA'] != 'NA':
            minutosTrabajadas = cinco['HSA'].minute - cinco['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if cinco['HALI'] != 'NA' and cinco['HALF'] != 'NA':
            horasAlmuerzo = cinco['HALF'].hour -cinco['HALI'].hour
        else:
            horasAlmuerzo = 0
        if cinco['HALI'] != 'NA' and cinco['HALF'] != 'NA':
            minutosAlmuerzo = cinco['HALF'].minute -cinco['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if cinco['EN'].day == 5:
            detalles5 = [(5, cinco['HEN'], cinco['HDYI'], cinco['HDYF'], cinco['HALI'], cinco['HALF'], cinco['HPAI'], cinco['HPAF'], cinco['HDCI'],cinco['HDCF'], cinco['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles5 = [(5, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #SEIS
        if seis['HEN'] != 'NA' and seis['HSA'] != 'NA':
            horasTrabajadas = seis['HSA'].hour - seis['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if seis['HEN'] != 'NA' and seis['HSA'] != 'NA':
            minutosTrabajadas = seis['HSA'].minute - seis['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if seis['HALI'] != 'NA' and seis['HALF'] != 'NA':
            horasAlmuerzo = seis['HALF'].hour -seis['HALI'].hour
        else:
            horasAlmuerzo = 0
        if seis['HALI'] != 'NA' and seis['HALF'] != 'NA':
            minutosAlmuerzo = seis['HALF'].minute -seis['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if seis['EN'].day == 6:
            detalles6 = [(6, seis['HEN'], seis['HDYI'], seis['HDYF'], seis['HALI'], seis['HALF'], seis['HPAI'], seis['HPAF'], seis['HDCI'],seis['HDCF'], seis['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles6 = [(6 , 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #SIETE
        if siete['HEN'] != 'NA' and siete['HSA'] != 'NA':
            horasTrabajadas = siete['HSA'].hour - siete['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if siete['HEN'] != 'NA' and siete['HSA'] != 'NA':
            minutosTrabajadas = siete['HSA'].minute - siete['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if siete['HALI'] != 'NA' and siete['HALF'] != 'NA':
            horasAlmuerzo = siete['HALF'].hour -siete['HALI'].hour
        else:
            horasAlmuerzo = 0
        if siete['HALI'] != 'NA' and siete['HALF'] != 'NA':
            minutosAlmuerzo = siete['HALF'].minute -siete['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante   

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if siete['EN'].day == 7:
            detalles7 = [(7, siete['HEN'], siete['HDYI'], siete['HDYF'], siete['HALI'], siete['HALF'], siete['HPAI'], siete['HPAF'], siete['HDCI'],siete['HDCF'], siete['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles7 = [(7, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #OCHO
        if ocho['HEN'] != 'NA' and ocho['HSA'] != 'NA':
            horasTrabajadas = ocho['HSA'].hour - ocho['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if ocho['HEN'] != 'NA' and ocho['HSA'] != 'NA':
            minutosTrabajadas = ocho['HSA'].minute - ocho['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if ocho['HALI'] != 'NA' and ocho['HALF'] != 'NA':
            horasAlmuerzo = ocho['HALF'].hour -ocho['HALI'].hour
        else:
            horasAlmuerzo = 0
        if ocho['HALI'] != 'NA' and ocho['HALF'] != 'NA':
            minutosAlmuerzo = ocho['HALF'].minute -ocho['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante    

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if ocho['EN'].day == 8:
            detalles8 = [(8, ocho['HEN'], ocho['HDYI'], ocho['HDYF'], ocho['HALI'], ocho['HALF'], ocho['HPAI'], ocho['HPAF'], ocho['HDCI'], ocho['HDCF'], ocho['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles8 = [(8, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #NUEVE
        if nueve['HEN'] != 'NA' and nueve['HSA'] != 'NA':
            horasTrabajadas = nueve['HSA'].hour - nueve['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if nueve['HEN'] != 'NA' and nueve['HSA'] != 'NA':
            minutosTrabajadas = nueve['HSA'].minute - nueve['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if nueve['HALI'] != 'NA' and nueve['HALF'] != 'NA':
            horasAlmuerzo = nueve['HALF'].hour -nueve['HALI'].hour
        else:
            horasAlmuerzo = 0
        if nueve['HALI'] != 'NA' and nueve['HALF'] != 'NA':
            minutosAlmuerzo = nueve['HALF'].minute -nueve['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)                 

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if nueve['EN'].day == 9:
            detalles9 = [(9, nueve['HEN'], nueve['HDYI'], nueve['HDYF'], nueve['HALI'], nueve['HALF'], nueve['HPAI'], nueve['HPAF'], nueve['HDCI'],nueve['HDCF'], nueve['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles9 = [(9,'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DIEZ
        if diez['HEN'] != 'NA' and diez['HSA'] != 'NA':
            horasTrabajadas = diez['HSA'].hour - diez['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if diez['HEN'] != 'NA' and diez['HSA'] != 'NA':
            minutosTrabajadas = diez['HSA'].minute - diez['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if diez['HALI'] != 'NA':
            horasAlmuerzo = diez['HALF'].hour -diez['HALI'].hour
        else:
            horasAlmuerzo = 0
        if diez['HALF'] != 'NA':
            minutosAlmuerzo = diez['HALF'].minute -diez['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if diez['EN'].day == 10:
            detalles10 = [(10, diez['HEN'], diez['HDYI'], diez['HDYF'], diez['HALI'], diez['HALF'], diez['HPAI'], diez['HPAF'], diez['HDCI'], diez['HDCF'], diez['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles10 = [(10, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #ONCE
        if once['HEN'] != 'NA' and once['HSA'] != 'NA':
            horasTrabajadas = once['HSA'].hour - once['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if once['HEN'] != 'NA' and once['HSA'] != 'NA':
            minutosTrabajadas = once['HSA'].minute - once['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if once['HALI'] != 'NA' and once['HALF'] != 'NA':
            horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasAlmuerzo = 0
        if once['HALF'] != 'NA' and once['HALI'] != 'NA':
            minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if once['EN'].day == 11:
            detalles11 = [(11, once['HEN'], once['HDYI'], once['HDYF'], once['HALI'], once['HALF'], once['HPAI'], once['HPAF'], once['HDCI'],once['HDCF'], once['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles11 = [(11 , 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #DOCE
        if doce['HEN'] != 'NA' and doce['HSA'] != 'NA':
            horasTrabajadas = doce['HSA'].hour - doce['HEN'].hour
        else:
            horasTrabajadas = 0
        if doce['HEN'] != 'NA' and doce['HSA'] != 'NA':
            minutosTrabajadas = doce['HSA'].minute - doce['HEN'].minute
        else:
            minutosTrabajadas = 0
        if doce['HALI'] != 'NA' and doce['HALF'] != 'NA':
            horasAlmuerzo = doce['HALF'].hour -doce['HALI'].hour
        else:
            horasAlmuerzo = 0
        if doce['HALI'] != 'NA' and doce['HALF'] != 'NA':
            minutosAlmuerzo = doce['HALF'].minute -doce['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if doce['EN'].day == 12:
            detalles12 = [(12, doce['HEN'], doce['HDYI'], doce['HDYF'], doce['HALI'], doce['HALF'], doce['HPAI'], doce['HPAF'], doce['HDCI'],doce['HDCF'], doce['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles12 = [(12, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #TRECE
        if trece['HEN'] != 'NA' and trece['HSA'] != 'NA':
            horasTrabajadas = trece['HSA'].hour - trece['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if trece['HEN'] != 'NA' and trece['HSA'] != 'NA':
            minutosTrabajadas = trece['HSA'].minute - trece['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if trece['HALI'] != 'NA' and trece['HALF'] != 'NA':
            horasAlmuerzo = trece['HALF'].hour -trece['HALI'].hour
        else:
            horasAlmuerzo = 0
        if trece['HALI'] != 'NA' and trece['HALF'] != 'NA':
            minutosAlmuerzo = trece['HALF'].minute -trece['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)             

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if trece['EN'].day == 13:
            detalles13 = [(13, trece['HEN'], trece['HDYI'], trece['HDYF'], trece['HALI'], trece['HALF'], trece['HPAI'], trece['HPAF'], trece['HDCI'],trece['HDCF'], trece['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles13 = [(13, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #CATORCE
        if catorce['HEN'] != 'NA' and catorce['HSA'] != 'NA':
            horasTrabajadas = catorce['HSA'].hour - catorce['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if catorce['HEN'] != 'NA' and catorce['HSA'] != 'NA':
            minutosTrabajadas = catorce['HSA'].minute - catorce['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if catorce['HALI'] != 'NA' and catorce['HALF'] != 'NA':
            horasAlmuerzo = catorce['HALF'].hour -catorce['HALI'].hour
        else:
            horasAlmuerzo = 0
        if catorce['HALI'] != 'NA' and catorce['HALF'] != 'NA':
            minutosAlmuerzo = catorce['HALF'].minute -catorce['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)     

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if catorce['EN'].day == 14:
            detalles14 = [(14, catorce['HEN'], catorce['HDYI'], catorce['HDYF'], catorce['HALI'], catorce['HALF'], catorce['HPAI'], catorce['HPAF'], catorce['HDCI'],catorce['HDCF'], catorce['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles14 = [(14, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #QUINCE
        if quince['HEN'] != 'NA' and quince['HSA'] != 'NA':
            horasTrabajadas = quince['HSA'].hour - quince['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if quince['HEN'] != 'NA' and quince['HSA'] != 'NA':
            minutosTrabajadas = quince['HSA'].minute - quince['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if quince['HALI'] != 'NA' and quince['HALF'] != 'NA':
            horasAlmuerzo = quince['HALF'].hour -quince['HALI'].hour
        else:
            horasAlmuerzo = 0
        if quince['HALI'] != 'NA' and quince['HALF'] != 'NA':
            minutosAlmuerzo = quince['HALF'].minute -quince['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)     

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if quince['EN'].day == 15:
            detalles15 = [(15, quince['HEN'], quince['HDYI'], quince['HDYF'], quince['HALI'], quince['HALF'], quince['HPAI'], quince['HPAF'], quince['HDCI'], quince['HDCF'], quince['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles15 = [(15, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DIECISEIS
        if dieciseis['HEN'] != 'NA' and dieciseis['HSA'] != 'NA':
            horasTrabajadas = dieciseis['HSA'].hour - dieciseis['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if dieciseis['HEN'] != 'NA' and dieciseis['HSA'] != 'NA':
            minutosTrabajadas = dieciseis['HSA'].minute - dieciseis['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if dieciseis['HALI'] != 'NA' and dieciseis['HALF'] != 'NA':
            horasAlmuerzo = dieciseis['HALF'].hour -dieciseis['HALI'].hour
        else:
            horasAlmuerzo = 0
        if dieciseis['HALI'] != 'NA' and dieciseis['HALF'] != 'NA':
            minutosAlmuerzo = dieciseis['HALF'].minute -dieciseis['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if dieciseis['EN'].day == 16:
            detalles16 = [(16, dieciseis['HEN'], dieciseis['HDYI'], dieciseis['HDYF'], dieciseis['HALI'], dieciseis['HALF'], dieciseis['HPAI'], dieciseis['HPAF'], dieciseis['HDCI'],dieciseis['HDCF'], dieciseis['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles16 = [(16, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DIECISIETE
        if diecisiete['HEN'] != 'NA' and diecisiete['HSA'] != 'NA':
            horasTrabajadas = diecisiete['HSA'].hour - diecisiete['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if diecisiete['HEN'] != 'NA' and diecisiete['HSA'] != 'NA':
            minutosTrabajadas = diecisiete['HSA'].minute - diecisiete['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if diecisiete['HALI'] != 'NA' and diecisiete['HALF'] != 'NA':
            horasAlmuerzo = diecisiete['HALF'].hour -diecisiete['HALI'].hour
        else:
            horasAlmuerzo = 0
        if diecisiete['HALI'] != 'NA' and diecisiete['HALF'] != 'NA':
            minutosAlmuerzo = diecisiete['HALF'].minute -diecisiete['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)       

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if diecisiete['EN'].day == 17:
            detalles17 = [(17, diecisiete['HEN'], diecisiete['HDYI'], diecisiete['HDYF'], diecisiete['HALI'], diecisiete['HALF'], diecisiete['HPAI'], diecisiete['HPAF'], diecisiete['HDCI'],diecisiete['HDCF'], diecisiete['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles17 = [(17, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DIECIOCHO
        if dieciocho['HEN'] != 'NA' and dieciocho['HSA'] != 'NA':
            horasTrabajadas = dieciocho['HSA'].hour - dieciocho['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if dieciocho['HEN'] != 'NA' and dieciocho['HSA'] != 'NA':
            minutosTrabajadas = dieciocho['HSA'].minute - dieciocho['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if dieciocho['HALI'] != 'NA' and dieciocho['HALF'] != 'NA':
            horasAlmuerzo = dieciocho['HALF'].hour -dieciocho['HALI'].hour
        else:
            horasAlmuerzo = 0
        if dieciocho['HALI'] != 'NA' and dieciocho['HALF'] != 'NA':
            minutosAlmuerzo = dieciocho['HALF'].minute -dieciocho['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if dieciocho['EN'].day == 18:
            detalles18 = [(18, dieciocho['HEN'], dieciocho['HDYI'], dieciocho['HDYF'], dieciocho['HALI'], dieciocho['HALF'], dieciocho['HPAI'], dieciocho['HPAF'], dieciocho['HDCI'],dieciocho['HDCF'], dieciocho['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles18 = [(18,'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #DIECINUEVE
        if diecinueve['HEN'] != 'NA' and diecinueve['HSA'] != 'NA':
            horasTrabajadas = diecinueve['HSA'].hour - diecinueve['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if diecinueve['HEN'] != 'NA' and diecinueve['HSA'] != 'NA':
            minutosTrabajadas = diecinueve['HSA'].minute - diecinueve['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if diecinueve['HALI'] != 'NA' and diecinueve['HALF'] != 'NA':
            horasAlmuerzo = diecinueve['HALF'].hour -diecinueve['HALI'].hour
        else:
            horasAlmuerzo = 0
        if diecinueve['HALI'] != 'NA' and diecinueve['HALF'] != 'NA':
            minutosAlmuerzo = diecinueve['HALF'].minute -diecinueve['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if diecinueve['EN'].day == 19:
            detalles19 = [(19, diecinueve['HEN'], diecinueve['HDYI'], diecinueve['HDYF'], diecinueve['HALI'], diecinueve['HALF'], diecinueve['HPAI'], diecinueve['HPAF'], diecinueve['HDCI'], diecinueve['HDCF'], diecinueve['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles19 = [(19, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTE
        if veinte['HEN'] != 'NA' and veinte['HSA'] != 'NA':
            horasTrabajadas = veinte['HSA'].hour - veinte['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veinte['HEN'] != 'NA' and veinte['HSA'] != 'NA':
            minutosTrabajadas = veinte['HSA'].minute - veinte['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veinte['HALI'] != 'NA' and veinte['HALF'] != 'NA':
            horasAlmuerzo = veinte['HALF'].hour -veinte['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veinte['HALI'] != 'NA' and veinte['HALF'] != 'NA':
            minutosAlmuerzo = veinte['HALF'].minute -veinte['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veinte['EN'].day == 20:
            detalles20 = [(20, veinte['HEN'], veinte['HDYI'], veinte['HDYF'], veinte['HALI'], veinte['HALF'], veinte['HPAI'], veinte['HPAF'], veinte['HDCI'],veinte['HDCF'], veinte['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles20 = [(20, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTIUNO
        if veintiuno['HEN'] != 'NA' and veintiuno['HSA'] != 'NA':
            horasTrabajadas = veintiuno['HSA'].hour - veintiuno['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintiuno['HEN'] != 'NA' and veintiuno['HSA'] != 'NA':
            minutosTrabajadas = veintiuno['HSA'].minute - veintiuno['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintiuno['HALI'] != 'NA' and veintiuno['HALF'] != 'NA':
            horasAlmuerzo = veintiuno['HALF'].hour -veintiuno['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintiuno['HALF'] != 'NA' and veintiuno['HALI']:
            minutosAlmuerzo = veintiuno['HALF'].minute -veintiuno['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintiuno['EN'].day == 21:
            detalles21 = [(21, veintiuno['HEN'], veintiuno['HDYI'], veintiuno['HDYF'], veintiuno['HALI'], veintiuno['HALF'], veintiuno['HPAI'], veintiuno['HPAF'], veintiuno['HDCI'], veintiuno['HDCF'], veintiuno['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles21 = [(21, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #VEINTIDOS
        if veintidos['HEN'] != 'NA' and veintidos['HSA'] != 'NA':
            horasTrabajadas = veintidos['HSA'].hour - veintidos['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintidos['HEN'] != 'NA' and veintidos['HSA'] != 'NA':
            minutosTrabajadas = veintidos['HSA'].minute - veintidos['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintidos['HALI'] != 'NA' and veintidos['HALF'] != 'NA':
            horasAlmuerzo = veintidos['HALF'].hour -veintidos['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintidos['HALF'] != 'NA' and veintidos['HALI'] != 'NA':
            minutosAlmuerzo = veintidos['HALF'].minute -veintidos['HALI'].minute
        else:
            minutosAlmuerzo = 0
        
        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas
        
        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        hora_restante = 0
        print("Min total",minutosTotal, minutosTrabajadas, minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal
            minutosTotal = 60 - minutosTotal
            hora_restante = 1
        print(hora_restante)    

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo) - (hora_restante)
        if horaTotal < 0:
            horaTotal = -horaTotal
        
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
        if veintidos['EN'].day == 22:
            detalles22 = [(22, veintidos['HEN'], veintidos['HDYI'], veintidos['HDYF'], veintidos['HALI'], veintidos['HALF'], veintidos['HPAI'], veintidos['HPAF'], veintidos['HDCI'],veintidos['HDCF'], veintidos['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles22 = [(22 , 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #VEINTITRES
        if veintitres['HEN'] != 'NA' and veintitres['HSA'] != 'NA':
            horasTrabajadas = veintitres['HSA'].hour - veintitres['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintitres['HEN'] != 'NA' and veintitres['HSA'] != 'NA':
            minutosTrabajadas = veintitres['HSA'].minute - veintitres['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintitres['HALI'] != 'NA' and veintitres['HALF'] != 'NA':
            horasAlmuerzo = veintitres['HALF'].hour -veintitres['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintitres['HALI'] != 'NA' and veintitres['HALF'] != 'NA':
            minutosAlmuerzo = veintitres['HALF'].minute -veintitres['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintitres['EN'].day == 23:
            detalles23 = [(23, veintitres['HEN'], veintitres['HDYI'], veintitres['HDYF'], veintitres['HALI'], veintitres['HALF'], veintitres['HPAI'], veintitres['HPAF'], veintitres['HDCI'], veintitres['HDCF'], veintitres['HSA'], "Horas: "+ str(horaTotal) + " Min "+ str(minutosTotal))]
        else:
            detalles23 = [(23, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTICUATRO
        if veinticuatro['HEN'] != 'NA' and veinticuatro['HSA'] != 'NA':
            horasTrabajadas = veinticuatro['HSA'].hour - veinticuatro['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veinticuatro['HEN'] != 'NA' and veinticuatro['HSA'] != 'NA':
            minutosTrabajadas = veinticuatro['HSA'].minute - veinticuatro['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veinticuatro['HALI'] != 'NA' and veinticuatro['HALF'] != 'NA':
            horasAlmuerzo = veinticuatro['HALF'].hour -veinticuatro['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veinticuatro['HALI'] != 'NA' and veinticuatro['HALF'] != 'NA':
            minutosAlmuerzo = veinticuatro['HALF'].minute -veinticuatro['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)        

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veinticuatro['EN'].day == 24:
            detalles24 = [(24, veinticuatro['HEN'], veinticuatro['HDYI'], veinticuatro['HDYF'], veinticuatro['HALI'], veinticuatro['HALF'], veinticuatro['HPAI'], veinticuatro['HPAF'], veinticuatro['HDCI'],veinticuatro['HDCF'], veinticuatro['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles24 = [(24,'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        #VEINTICINCO
        if veinticinco['HEN'] != 'NA' and veinticinco['HSA'] != 'NA':
            horasTrabajadas = veinticinco['HSA'].hour - veinticinco['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veinticinco['HEN'] != 'NA' and veinticinco['HSA'] != 'NA':
            minutosTrabajadas = veinticinco['HSA'].minute - veinticinco['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veinticinco['HALI'] != 'NA' and veinticinco['HALF'] != 'NA':
            horasAlmuerzo = veinticinco['HALF'].hour -veinticinco['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veinticinco['HALI'] != 'NA' and veinticinco['HALF'] != 'NA':
            minutosAlmuerzo = veinticinco['HALF'].minute -veinticinco['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veinticinco['EN'].day == 25:
            detalles25 = [(25, veinticinco['HEN'], veinticinco['HDYI'], veinticinco['HDYF'], veinticinco['HALI'], veinticinco['HALF'], veinticinco['HPAI'], veinticinco['HPAF'], veinticinco['HDCI'],veinticinco['HDCF'], veinticinco['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles25 = [(25, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTISEIS
        if veintiseis['HEN'] != 'NA' and veintiseis['HSA'] != 'NA':
            horasTrabajadas = veintiseis['HSA'].hour - veintiseis['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintiseis['HEN'] != 'NA' and veintiseis['HSA'] != 'NA':
            minutosTrabajadas = veintiseis['HSA'].minute - veintiseis['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintiseis['HALI'] != 'NA' and veintiseis['HALF'] != 'NA':
            horasAlmuerzo = veintiseis['HALF'].hour -veintiseis['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintiseis['HALI'] != 'NA' and veintiseis['HALF'] != 'NA':
            minutosAlmuerzo = veintiseis['HALF'].minute -veintiseis['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintiseis['EN'].day == 26:
            detalles26 = [(26, veintiseis['HEN'], veintiseis['HDYI'], veintiseis['HDYF'], veintiseis['HALI'], veintiseis['HALF'], veintiseis['HPAI'], veintiseis['HPAF'], veintiseis['HDCI'],veintiseis['HDCF'], veintiseis['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles26 = [(26, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTISIETE
        if veintisiete['HEN'] != 'NA' and veintisiete['HSA'] != 'NA':
            horasTrabajadas = veintisiete['HSA'].hour - veintisiete['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintisiete['HEN'] != 'NA' and veintisiete['HSA'] != 'NA':
            minutosTrabajadas = veintisiete['HSA'].minute - veintisiete['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintisiete['HALI'] != 'NA' and veintisiete['HALF'] != 'NA':
            horasAlmuerzo = veintisiete['HALF'].hour -veintisiete['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintisiete['HALI'] != 'NA' and veintisiete['HALF'] != 'NA':
            minutosAlmuerzo = veintisiete['HALF'].minute -veintisiete['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal
            
        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)         

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintisiete['EN'].day == 27:
            detalles27 = [(27, veintisiete['HEN'], veintisiete['HDYI'], veintisiete['HDYF'], veintisiete['HALI'], veintisiete['HALF'], veintisiete['HPAI'], veintisiete['HPAF'], veintisiete['HDCI'], veintisiete['HDCF'], veintisiete['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles27 = [(27, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTIOCHO
        if veintiocho['HEN'] != 'NA' and veintiocho['HSA'] != 'NA':
            horasTrabajadas = veintiocho['HSA'].hour - veintiocho['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintiocho['HEN'] != 'NA' and veintiocho['HSA'] != 'NA':
            minutosTrabajadas = veintiocho['HSA'].minute - veintiocho['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintiocho['HALI'] != 'NA' and veintiocho['HALF'] != 'NA':
            horasAlmuerzo = veintiocho['HALF'].hour -veintiocho['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintiocho['HALI'] != 'NA' and veintiocho['HALF'] != 'NA':
            minutosAlmuerzo = veintiocho['HALF'].minute -veintiocho['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintiocho['EN'].day == 28:
            detalles28 = [(28, veintiocho['HEN'], veintiocho['HDYI'], veintiocho['HDYF'], veintiocho['HALI'], veintiocho['HALF'], veintiocho['HPAI'], veintiocho['HPAF'], veintiocho['HDCI'],veintiocho['HDCF'], veintiocho['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles28 = [(28, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #VEINTINUEVE
        if veintinueve['HEN'] != 'NA' and veintinueve['HSA'] != 'NA':
            horasTrabajadas = veintinueve['HSA'].hour - veintinueve['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if veintinueve['HEN'] != 'NA' and veintinueve['HSA'] != 'NA':
            minutosTrabajadas = veintinueve['HSA'].minute - veintinueve['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if veintinueve['HALI'] != 'NA' and veintinueve['HALF'] != 'NA':
            horasAlmuerzo = veintinueve['HALF'].hour -veintinueve['HALI'].hour
        else:
            horasAlmuerzo = 0
        if veintinueve['HALF'] != 'NA' and veintinueve['HALI']:
            minutosAlmuerzo = veintinueve['HALF'].minute -veintinueve['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if veintinueve['EN'].day == 29:
            detalles29 = [(29, veintinueve['HEN'], veintinueve['HDYI'], veintinueve['HDYF'], veintinueve['HALI'], veintinueve['HALF'], veintinueve['HPAI'], veintinueve['HPAF'], veintinueve['HDCI'], veintinueve['HDCF'], veintinueve['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles29 = [(29,'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]



        #TREINTA
        if treinta['HEN'] != 'NA' and treinta['HSA'] != 'NA':
            horasTrabajadas = treinta['HSA'].hour - treinta['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if treinta['HEN'] != 'NA' and treinta['HSA'] != 'NA':
            minutosTrabajadas = treinta['HSA'].minute - treinta['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if treinta['HALI'] != 'NA' and treinta['HALF'] != 'NA':
            horasAlmuerzo = treinta['HALF'].hour -treinta['HALI'].hour
        else:
            horasAlmuerzo = 0
        if treinta['HALF'] != 'NA' and treinta['HALI'] != 'NA':
            minutosAlmuerzo = treinta['HALF'].minute -treinta['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal

        #print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        #print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        if treinta['EN'].day == 30:
            detalles30 = [(30, treinta['HEN'], treinta['HDYI'], treinta['HDYF'], treinta['HALI'], treinta['HALF'], treinta['HPAI'], treinta['HPAF'], treinta['HDCI'],treinta['HDCF'], treinta['HSA'], "Horas: "+ str(horaTotal) + " Min: "+ str(minutosTotal))]
        else:
            detalles30 = [(30,'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]


        #TREINTAUNO
        if treintauno['HEN'] != 'NA' and treintauno['HSA'] != 'NA':
            horasTrabajadas = treintauno['HSA'].hour - treintauno['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if treintauno['HEN'] != 'NA' and treintauno['HSA'] != 'NA':
            minutosTrabajadas = treintauno['HSA'].minute - treintauno['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if treintauno['HALI'] != 'NA' and treintauno['HALF'] != 'NA':
            horasAlmuerzo = treintauno['HALF'].hour -treintauno['HALI'].hour
        else:
            horasAlmuerzo = 0
        if treintauno['HALF'] != 'NA' and treintauno['HALI'] != 'NA':
            minutosAlmuerzo = treintauno['HALF'].minute -treintauno['HALI'].minute
        else:
            minutosAlmuerzo = 0

        #MINUTOS
        if minutosAlmuerzo < 0:
            minutosAlmuerzo = -minutosAlmuerzo

        if minutosTrabajadas < 0:
            minutosTrabajadas = -minutosTrabajadas

        minutosTotal =  (minutosTrabajadas) - (minutosAlmuerzo)
        if minutosTotal < 0:
            minutosTotal = -minutosTotal

        #HORAS
        if horasAlmuerzo < 0:
            horasAlmuerzo = -horasAlmuerzo

        if horasTrabajadas < 0:
            horasTrabajadas = -horasTrabajadas

        horaTotal =  (horasTrabajadas) - (horasAlmuerzo)
        if horaTotal < 0:
            horaTotal = -horaTotal


        print("Antes" ,totalMesMinutos, totalMes)
        restante = 0
        if totalMesMinutos >= 60:
           restante = totalMesMinutos - 60
           totalMes +=1
           totalMesMinutos = restante
        print("Resultado",totalMesMinutos, totalMes)

        totalMes = horaTotal + totalMes
        totalMesMinutos = minutosTotal + totalMesMinutos
        print(totalMes, totalMesMinutos)
        if treintauno['EN'].day == 31:
            detalles31 = [(31, treintauno['HEN'], treintauno['HDYI'], treintauno['HDYF'], treintauno['HALI'], treintauno['HALF'], treintauno['HPAI'], treintauno['HPAF'], treintauno['HDCI'],treintauno['HDCF'], treintauno['HSA'], "Horas: "+ str(horaTotal) + " Minutos "+ str(minutosTotal))]
        else:
            detalles31 = [(31, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]

        totalHoras = [('Total'," ", " ", " ", " "," ", " ", " ", " ","","","Horas: "+ str(totalMes) + " Min: "+ str(totalMesMinutos))]

        #Establecemos el tamaño de cada una de las columnas de la tabla
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden = Table([encabezados] + detalles1 + detalles2 + detalles3 + detalles4 + detalles5 + detalles6 +  detalles7 + detalles8 + detalles9 + detalles10 + detalles11 + detalles12 + detalles13 +  detalles14 + detalles15 + detalles16 + detalles17 + detalles18 + detalles19 + detalles20 + detalles21 + detalles22 + detalles23 + detalles24 + detalles25 + detalles26 + detalles27 + detalles28 + detalles29 + detalles30 + detalles31+ totalHoras, colWidths=[ 1.5* cm, 2.15 * cm, 2.15 * cm, 2.6 * cm, 2.15* cm, 2.6 * cm, 2.8 * cm, 3.4 * cm,2.15* cm, 2.4 * cm, 2.15 * cm, 3.5 * cm,])
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(0,0),'LEFT'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -2), 0, colors.black),
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (0, -38), 4.5)
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60,30)

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
        pdf.setPageSize((950,750) )
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        if 'cedula' in request.GET and 'mes' in request.GET:
            cedula = request.GET['cedula']
            mes = request.GET['mes']
            #print( "Mes" ,mes)
            if not cedula and not mes:
                errors.append('Colaborador no encontrado.')
            else:
                Colaborador = Historial_IO.objects.filter(id_trabajadores__cedula=cedula)
                Mes = Historial_IO.objects.filter(fecha__month=mes)
                return response
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
            errors.append('Por favor introduce un termino de busqueda.')
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
                    print(form.errors)
                    errors.append('La acción ya se encuntra registrada en este día.')

            return render(request, 'registrarJornada/registrarJornada.html',context)

    return render(request, 'registrarJornada/registrarJornada.html', {'errors': errors})
