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
        print(self.request.GET)
        q = Historial_IO.objects.filter(id_trabajadores__cedula=self.request.GET.get('cedula'))
        cedula = self.request.GET.get('cedula')
        hoy = str(date.today().day)
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
            fq = i.fecha.day
            a['nombre'] = i.id_trabajadores.nombres
            a['cedula'] = i.id_trabajadores.cedula
            if fq == 1:
                uno[i.accion_jornada] = i.fecha
                uno[i.accion_jornada_hora] = i.hora
            elif fq == 2:
                dos[i.accion_jornada] = i.fecha
                dos[i.accion_jornada_hora] = i.hora
            elif fq == 3:
                tres[i.accion_jornada] = i.fecha
                tres[i.accion_jornada_hora] = i.hora
            elif fq == 4:
                cuatro[i.accion_jornada] = i.fecha
                cuatro[i.accion_jornada_hora] = i.hora
            elif fq==5:
                cinco[i.accion_jornada] = i.fecha
                cinco[i.accion_jornada_hora] = i.hora
            elif fq == 6:
                seis[i.accion_jornada] = i.fecha
                seis[i.accion_jornada_hora] = i.hora
            elif fq == 7:
                siete[i.accion_jornada] = i.fecha
                siete[i.accion_jornada_hora] = i.hora
            elif fq==8:
                ocho[i.accion_jornada] = i.fecha
                ocho[i.accion_jornada_hora] = i.hora
            elif fq==9:
                nueve[i.accion_jornada] = i.fecha
                nueve[i.accion_jornada_hora] = i.hora
            elif fq == 10:
                diez[i.accion_jornada] = i.fecha
                diez[i.accion_jornada_hora] = i.hora
            elif fq == 11:
                once[i.accion_jornada] = i.fecha
                once[i.accion_jornada_hora] = i.hora
            elif fq==12:
                doce[i.accion_jornada] = i.fecha
                doce[i.accion_jornada_hora] = i.hora
            elif fq==13:
                trece[i.accion_jornada] = i.fecha
                trece[i.accion_jornada_hora] = i.hora
            elif fq==14:
                catorce[i.accion_jornada] = i.fecha
                catorce[i.accion_jornada_hora] = i.hora
            elif fq == 15:
                quince[i.accion_jornada] = i.fecha
                quince[i.accion_jornada_hora] = i.hora
            elif fq == 16:
                dieciseis[i.accion_jornada] = i.fecha
                dieciseis[i.accion_jornada_hora] = i.hora
            elif fq == 17:
                diecisiete[i.accion_jornada] = i.fecha
                diecisiete[i.accion_jornada_hora] = i.hora
            elif fq == 18:
                dieciocho[i.accion_jornada] = i.fecha
                dieciocho[i.accion_jornada_hora] = i.hora
            elif fq==19:
                diecinueve[i.accion_jornada] = i.fecha
                diecinueve[i.accion_jornada_hora] = i.hora
            elif fq == 20:
                veinte[i.accion_jornada] = i.fecha
                veinte[i.accion_jornada_hora] = i.hora
            elif fq == 21:
                veintiuno[i.accion_jornada] = i.fecha
                veintiuno[i.accion_jornada_hora] = i.hora
            elif fq==22:
                veintidos[i.accion_jornada] = i.fecha
                veintidos[i.accion_jornada_hora] = i.hora
            elif fq==23:
                veintitres[i.accion_jornada] = i.fecha
                veintitres[i.accion_jornada_hora] = i.hora
            elif fq == 24:
                veinticuatro[i.accion_jornada] = i.fecha
                veinticuatro[i.accion_jornada_hora] = i.hora
            elif fq == 25:
                veinticinco[i.accion_jornada] = i.fecha
                veinticinco[i.accion_jornada_hora] = i.hora
            elif fq==26:
                veintiseis[i.accion_jornada] = i.fecha
                veintiseis[i.accion_jornada_hora] = i.hora
            elif fq==27:
                veintisiete[i.accion_jornada] = i.fecha
                veintisiete[i.accion_jornada_hora] = i.hora
            elif fq==28:
                veintiocho[i.accion_jornada] = i.fecha
                veintiocho[i.accion_jornada_hora] = i.hora
            elif fq==29:
                veintinueve[i.accion_jornada] = i.fecha
                veintinueve[i.accion_jornada_hora] = i.hora
            elif fq==30:
                treinta[i.accion_jornada] = i.fecha
                treinta[i.accion_jornada_hora] = i.hora
            elif fq==31:
                treintauno[i.accion_jornada] = i.fecha
                treintauno[i.accion_jornada_hora] = i.hora
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
        # a.update(j)  //Combinar dos  diccionarios
        #print(self.z)
        #self.b.append(a)
        #print(self.b)
        # print(m)
        #print(self.b)
        a={}
        j={}
        print(self.b)
        return self.b


class ReportePersonasPDF(View):
    def cabecera(self,pdf):
        objetos = Trabajadores.objects.all()
        #r = self.request.GET['cedula']
        #print("R con R cigaRRO",r)
        a = {}
        b= []
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.STATIC_ROOT+'/img/index.jpg'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 490, 120, 80,preserveAspectRatio=True)
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 25)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(280, 520, u"Siete Colinas S.A.S")
        pdf.line(280, 510, 520, 510)
        pdf.setFont("Helvetica", 14)
        pdf.drawString(280, 492, u"REPORTE DE REGISTRO JORNADA")
        pdf.setFont("Helvetica", 10)
        pdf.drawString(620, 500, u"Colaborador:")
        pdf.setFont("Helvetica", 10)
        for i in objetos:
            a['nombree'] = i.nombres
        b.append(a)
        pdf.drawString(680,500, 'Jose Antonio Piccaso')
        print(a)

    def tabla(self,pdf,y):
        #print("cedula del nn", f)
        cont = 0
        cont1 = 0
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('día', 'hora Entrada', 'hora Desayuno', 'Hora Fin desayuno', 'hora Almuerzo', 'hora Fin Almuerzo', 'hora Pausas Activas', 'hora Fin pausas activas', 'hora Descanso', 'hora Fin Descanso', 'hora Salida', 'Horas Trabajadas', 'horas Descansadas')
        #Creamos una lista de tuplas que van a contener a las personas
        q = Historial_IO.objects.filter(id_trabajadores__cedula=self.request.GET.get('cedula'))
        #fq = i.fecha.day
        #a['nombre'] = i.id_trabajadores.nombres
        """if fq == 4:
            a[i.accion_jornada] = i.fecha
        elif fq==5:
            j[i.accion_jornada] = i.fecha
        elif fq==8:
            ocho[i.accion_jornada] = i.fecha
            ocho[i.accion_jornada_hora] = i.hora
        elif fq==9:
            nueve[i.accion_jornada] = i.fecha
            nueve[i.accion_jornada_hora] = i.hora
        """
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

        self.b= []
        for i in q:
            fq = i.fecha.day
            #print(fq)
            a['nombre'] = i.id_trabajadores.nombres
            if fq==8:
                ocho[i.accion_jornada] = i.fecha
                ocho[i.accion_jornada_hora] = i.hora
                #detalles = [(i.fecha, i.accion_jornada_hora)]
            elif fq==9:
                nueve[i.accion_jornada] = i.fecha
                nueve[i.accion_jornada_hora] = i.hora
            elif fq==10:
                diez[i.accion_jornada] = i.fecha
                diez[i.accion_jornada_hora] = i.hora
            elif fq==11:
                once[i.accion_jornada] = i.fecha
                once[i.accion_jornada_hora] = i.hora


        self.b.append(a)
        self.b.append(ocho)
        self.b.append(nueve)
        self.b.append(diez)
        self.b.append(once)


        #print("sss", once)

        #if ocho
        #for g, u in ocho.items():
        #    print(g,u)

        if ocho['EN'].day == 8:
            detalles = [(8, ocho['HEN'], ocho['HDYI'], 'vacio', ocho['HALI'] ) ]
        if nueve['EN'].day == 9:
            detalles2 = [(9, nueve['HEN'], nueve['HDYI'], nueve['HDYF'], nueve['HEN'], 'NA' )]
        #else:
        #    detalles2 = [(9, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]
        if diez['EN'].day == 10:
            detalles10 = [(10, diez['HEN'], diez['HDYI'], diez['HDYF'], diez['HEN'], 'NA' )]

        if once['HSA'] != 'NA':
            horasTrabajadas = once['HSA'].hour - once['HEN'].hour
            #horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasTrabajadas = 0
        if once['HSA'] != 'NA':
            minutosTrabajadas = once['HSA'].minute - once['HEN'].minute
            #minutosAlmuerzo = once['HALF'].minute -once['HALI'].minute
        else:
            minutosTrabajadas = 0

        if once['HALI'] != 'NA':
            horasAlmuerzo = once['HALF'].hour -once['HALI'].hour
        else:
            horasAlmuerzo = 0
        if once['HALF'] != 'NA':
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

        print(horasTrabajadas, minutosTrabajadas)
        print(horasAlmuerzo, minutosAlmuerzo)
        print(horaTotal, horasTrabajadas, horasAlmuerzo)
        #minutosTrabajadas = once['HSA'].minute - once['HEN'].minute
        #print(once['HSA'].minute, once['HEN'].minute)
        #print(minutosTotal, minutosTrabajadas, minutosAlmuerzo)
        #print(horaTotal)
        #Me llene el registro cuando todos los campos ya esten llenos hasta la salida
        if once['EN'].day == 11 :
            detalles11 = [(11, once['HEN'], once['HDYI'], once['HDYF'], once['HALI'], once['HALF'], once['HPAI'], once['HPAF'], once['HDCI'],once['HDCF'], once['HSA'], "Horas: "+ str(horaTotal) + " Minutos "+ str(minutosTotal), 'Horas Descansadas'   )]
        #try:
        #    detalles11 = [(11, once['HEN'], once['HDYI'], once['HDYF'], once['HALI'], once['HALF'], once['HPAI'], once['HPAF'], once['HDCI'],once['HDCF'], once['HSA'], "Horas: "+ str(horasTrabajadas) + " Minutos "+ str(minutosTrabajadas), 'Horas Descansadas'   )]
        #except:
        #    detalles11 = [(11, once['HEN'], once['HDYI'], once['HDYF'], once['HALI'], once['HALF'], once['HPAI'], once['HPAF'], once['HDCI'],once['HDCF'], once['HSA'], 'NA', 'Horas Descansadas'   )]

        #detalles2 = [(9 , 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden = Table([encabezados] + detalles+ detalles2 + detalles10 + detalles11, colWidths=[ 1.5* cm, 2.15 * cm, 2.15 * cm, 2.15 * cm])
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'LEFT'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 5),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 10,250)

    def get(self, request, *args, **kwargs):
        #f = request.GET['cedula']
        #print("F con F",value)
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.setPageSize( landscape(letter) )
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
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
