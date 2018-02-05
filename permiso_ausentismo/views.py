import json

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle

from CRT import settings
from main.models import Trabajadores
from permiso_ausentismo.forms import PermisoAusentismoForms
from permiso_ausentismo.models import PermisoAusentismo


def ListarPermisoAusentismo(request):
    listar_permisos = PermisoAusentismo.objects.all()
    trabajador = ''
    cedula = request.GET.get('cedula')
    mes = request.GET.get('mes')
    if Trabajadores.objects.all().exists():
        hay_trabajador = 1
    else:
        hay_trabajador = 0
    # print(cedula)
    # print(mes)

    if cedula:
        listar_permisos = PermisoAusentismo.objects.filter(idTrabajador__cedula=cedula).order_by('mes_evento')
        trabajador = Trabajadores.objects.filter(cedula=cedula)


    if mes and mes != '--':

        listar_permisos = PermisoAusentismo.objects.filter(mes_evento=mes).order_by('mes_evento')


    if mes and mes != '--' and cedula:
        listar_permisos = PermisoAusentismo.objects.filter(mes_evento=mes, idTrabajador__cedula=cedula).order_by('mes_evento')



    #print(listar_permisos.values())
    #print(listar_permisos[1].get_mes_evento_display())
    paginator = Paginator(listar_permisos, 5)

    page = request.GET.get('page')
    listar_permisos = paginator.get_page(page)


    if request.POST.get('imprimir'):
        reponse = HttpResponse(content_type='applicacion/pdf')
        # print(request.GET)
        reponse['Content-Disposition'] = 'filename=reporte.pdf'
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)

        # CABECERA DEL ARCHIVO
        archivo_imagen = settings.STATIC_ROOT + '/img/index.jpg'
        c.drawImage(archivo_imagen, 20, 750, 120, 80, preserveAspectRatio=True)
        c.setFont("Helvetica", 20)
        # Dibujamos una cadena en la ubicación X,Y especificada
        c.drawString(150, 800, u"Siete Colinas S.A.S")
        c.line(150, 795, 345, 795)
        c.setFont("Helvetica", 10)
        c.drawString(150, 780, u"REPORTE PERMISO DE AUSENTISMO")
        c.setFont("Helvetica", 15)
        c.drawString(430, 810, u"Colaborador:")
        c.setFont("Helvetica", 14)
        c.drawString(380, 794, str(trabajador.first()))
        c.setFont("Helvetica", 15)
        c.drawString(447, 773, u"Cedula:")
        c.setFont("Helvetica", 14)
        c.drawString(435, 756, cedula)

        #CABECERA DE LA TABLA
        styles = getSampleStyleSheet()
        styleBH = styles['Normal']
        styleBH.aligment = TA_CENTER
        styleBH.fontSize = 10

        mes = Paragraph('''Mes''',styleBH)
        periodo_inicial = Paragraph('''Periodo inicial''', styleBH)
        periodo_final = Paragraph('''Periodo final''', styleBH)
        total_dias_incapacidad = Paragraph('''Total días''', styleBH)
        codigo_diagnostico = Paragraph('''Código de diagnostico''',styleBH)
        tipo_evento = Paragraph('''Tipo de evento''', styleBH)
        observaciones = Paragraph('''Observaciones''',styleBH)

        data = []
        data.append([mes,periodo_inicial,periodo_final,total_dias_incapacidad,tipo_evento,codigo_diagnostico,observaciones])

        #TABLA
        styleN = styles['BodyText']
        styleN.aligment= TA_CENTER
        styleN.fontSize = 7

        high = 700
        cont = 0
        for x in listar_permisos.object_list.values():
            x['mes_evento'] = listar_permisos[cont].get_mes_evento_display()
            x['totalDiasIncapacidad'] = str(x['totalDiasIncapacidad'])
            print(x['totalDiasIncapacidad'])
            if x['totalDiasIncapacidad'] == '0':
                x['totalDiasIncapacidad'] = 1
            x['tipo_evento'] = listar_permisos[cont].get_tipo_evento_display()
            #print(x['observaciones'])

            if x['observaciones'] == None:
                x['observaciones'] = 'Sin registro'
            if x['codigoDiagnostico'] == None or x['codigoDiagnostico'] == '':
                x['codigoDiagnostico'] = 'No aplica'
            if x['tipo_evento'][0:3] == 'A.C':
                x['tipo_evento'] = 'A.C'
            if x['tipo_evento'][0:3] == 'O.E':
                x['tipo_evento'] = 'O.E'
            if x['tipo_evento'][0:3] == 'A.T':
                x['tipo_evento'] = 'A.T'
            if x['tipo_evento'][0:3] == 'E.L':
                x['tipo_evento'] = 'E.L'

            permiso=[
                x["mes_evento"],
                x["periodoIncapacidadInicial"],
                x["periodoIncapacidadFinal"],
                x["totalDiasIncapacidad"],
                x["tipo_evento"],
                x["codigoDiagnostico"],
                Paragraph(x["observaciones"],styles['Normal']),
            ]
            cont = cont + 1
            data.append(permiso)
            high = high - 18

        #TABLA
        width, height =A4
        table = Table(data,colWidths=[2.1 * cm,2.7 * cm,2.7 * cm,2.9 * cm,1.8 * cm,2.9 * cm,4.8 * cm,4.0 * cm,])
        table.setStyle(TableStyle([#Estilos de la tabla
            ('INNERGRID',(0,0),(-1,-1),0.25,colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            #('GRID',(6,1),(6,-1),2,colors.orange),
            ('ALIGN', (3, 0), (5, -1), 'CENTER'),
        ]))

        table.wrapOn(c,width,height)
        table.drawOn(c,20,high)

        c.showPage()
        c.save()
        pdf = buffer.getvalue()
        buffer.close()
        reponse.write(pdf)
        return reponse

    """
    if request.method == 'POST':
        if request.is_ajax():
            #report(request)
            return render(request, 'Trabajadores/trabajadores.html', context)
    """

    context = {
        'listar_permisos': listar_permisos,
        'trabajador': trabajador,
        'cedula':cedula,
        'mes':mes,
        'hay_trabajador':hay_trabajador,
    }
    return render(request, 'permiso_ausentismo/permiso_ausentismo.html', context)


def CrearPermisoAusentismo(request):
    form = PermisoAusentismoForms(request.POST or None)
    # --------------- Prueba de carga de datos xlsx ------------------- #
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if request.is_ajax():
            # Always use get on request.POST. Correct way of querying a QueryDict.
            import openpyxl
            codigo = request.POST.get('codigo')
            documento = openpyxl.load_workbook('CIE/CIE10%s.xlsx' % codigo)
            lista = documento.get_sheet_names()
            sheet = documento.get_sheet_by_name(lista[0])
            a = []
            codigos = dict()

            # d,e=codigo.split('-')
            # password = request.POST.get('password')
            for filas in sheet.rows:
                for columnas in filas:
                    a.append(columnas.value)
                codigos[a[0]] = a[1]
                a = []
            """
            for filas in sheet[d:e]:
                for columna in filas:
                    a.append(columna.value)
                codigos[a[0]] = a[1]
                # print(a[0],a[1])
                a = []
            """
            # print(codigos)
            codigos.pop('Código')
            # print(codigos)
            data = {"codigo": codigo, "codigos": codigos}
            # codigos.clear()
            # print(codigos)
            documento.close()

            # Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(data)
        if form.is_valid():

            if form.cleaned_data['observaciones'] == None:
                print('awdad')
                form.initial={'observaciones':'Sin observaciones.'}
            instance = form.save(commit=False)
            instance.save()
            return redirect('listado_permiso_ausentismo')
        else:
            errors = form.errors
            # print(errors)
    return render(request, 'permiso_ausentismo/form_permiso_ausentismo.html', context)


"""
def DetallePermisoAusentismo(request,pk):
    permiso_ausentismo = PermisoAusentismo.objects.filter(idPermisoAusentismo=pk)
    context = {
        'object':permiso_ausentismo,
    }
    return render(request,'permiso_ausentismo/detalle_permiso_ausentismo.html',context)
"""


class DetallePermisoAusentismo(DetailView):
    model = PermisoAusentismo
    template_name = 'permiso_ausentismo/detalle_permiso_ausentismo.html'


def prueba_ajax(request):
    if request.method == 'POST':
        # POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            # Always use get on request.POST. Correct way of querying a QueryDict.
            import openpyxl
            codigo = request.POST.get('codigo')

            documento = openpyxl.load_workbook('CIE10.xlsx')
            lista = documento.get_sheet_names()
            sheet = documento.get_sheet_by_name(lista[0])
            a = []
            codigos = dict()

            d, e = codigo.split('-')
            # password = request.POST.get('password')


            for filas in sheet[d:e]:
                for columna in filas:
                    a.append(columna.value)
                codigos[a[0]] = a[1]
                # print(a[0],a[1])
                a = []

            # print(codigos)
            codigos.pop('Código')
            print(codigos)
            data = {"codigo": codigo, "codigos": codigos}
            codigos.clear()
            documento.close()
            # Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(data)
            # Get goes here
    return render(request, 'permiso_ausentismo/tabs.html')


class EliminarPermisoAusentismo(DeleteView):
    model = PermisoAusentismo
    template_name = 'permiso_ausentismo/eliminar_permiso_ausentismo.html'
    success_url = reverse_lazy('listado_permiso_ausentismo')


def EditarPermisoAusentismo(request, pk):
    id = get_object_or_404(PermisoAusentismo, pk=pk)
    if request.method == 'POST':
        form = PermisoAusentismoForms(request.POST, instance=id)
        if request.is_ajax():
            # Always use get on request.POST. Correct way of querying a QueryDict.
            import openpyxl
            codigo = request.POST.get('codigo')
            documento = openpyxl.load_workbook('CIE/CIE10%s.xlsx' % codigo)
            lista = documento.get_sheet_names()
            sheet = documento.get_sheet_by_name(lista[0])
            a = []
            codigos = dict()

            # d,e=codigo.split('-')
            # password = request.POST.get('password')
            for filas in sheet.rows:
                for columnas in filas:
                    a.append(columnas.value)
                codigos[a[0]] = a[1]
                a = []
            """
            for filas in sheet[d:e]:
                for columna in filas:
                    a.append(columna.value)
                codigos[a[0]] = a[1]
                # print(a[0],a[1])
                a = []
            """
            # print(codigos)
            codigos.pop('Código')
            # print(codigos)
            data = {"codigo": codigo, "codigos": codigos}
            # codigos.clear()
            # print(codigos)
            documento.close()

            # Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(data)

        if form.is_valid():
            print(form.cleaned_data['observaciones'])
            if form.cleaned_data['observaciones'] == None:

                form.initial={'observaciones':'Sin observaciones.'}
            instance = form.save(commit=False)
            instance.save()
            return redirect('listado_permiso_ausentismo')
        else:
            print(form.errors)
    else:
        form = PermisoAusentismoForms(request.POST or None, instance=id)

    return render(request, 'permiso_ausentismo/form_permiso_ausentismo.html', {'form':form})


