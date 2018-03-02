import openpyxl

documento = openpyxl.load_workbook('CIE10.xlsx')
lista=documento.get_sheet_names()
sheet = documento.get_sheet_by_name(lista[0])
a = []
codigos= dict()
for filas in sheet['B1':'C12422']:
    for columna in filas:
        a.append(columna.value)
    codigos[a[0]]=a[1]
    # print(a[0],a[1])
    a=[]










