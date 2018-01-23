import json

from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from main.models import Trabajadores
from permiso_ausentismo.forms import PermisoAusentismoForms
from permiso_ausentismo.models import PermisoAusentismo


def ListarPermisoAusentismo(request):
    listar_permisos = PermisoAusentismo.objects.all()
    trabajador = ''
    cedula = request.GET.get('cedula')
    mes = request.GET.get('mes')
    # print(cedula)
    # print(mes)
    if cedula:
        listar_permisos = PermisoAusentismo.objects.filter(idTrabajador__cedula=cedula)
        trabajador = Trabajadores.objects.filter(cedula=cedula)

    if mes and mes != '--':
        listar_permisos = PermisoAusentismo.objects.filter(mes_evento=mes)

    if mes and mes != '--' and cedula:
        listar_permisos = PermisoAusentismo.objects.filter(mes_evento=mes, idTrabajador__cedula=cedula)


    context = {
        'listar_permisos': listar_permisos,
        'trabajador': trabajador,
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
    pk = PermisoAusentismo.objects.get(idPermisoAusentismo=pk)
    form = ''
    if request.method == 'GET':
        form = PermisoAusentismoForms(instance=pk)

    context = {
        'form': form,
    }
    if form:
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
                instance = form.save(commit=False)
                instance.save()
                return redirect('listado_permiso_ausentismo')
            else:
                errors = form.errors
                # print(errors)
        return render(request, 'permiso_ausentismo/form_permiso_ausentismo.html', context)
    return render(request, 'permiso_ausentismo/form_permiso_ausentismo.html', context)


def report(request):
    reponse = HttpResponse(content_type='applicacion/pdf')
    print(request.GET)
    reponse['Content-Disposition'] = 'attacment; filename=reporte.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    # CABECERA DEL ARCHIVO
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30, 750, '1195250')
    c.setFont('Helvetica', 12)
    c.drawString(30, 735, 'FICHA')
    c.setFont('Helvetica-Bold', 12)
    c.drawString(480, 750, '26/05/2017')
    c.line(460, 747, 560, 747)

    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    reponse.write(pdf)
    return reponse
