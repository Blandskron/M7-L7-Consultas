from django.shortcuts import render
from .models import Cliente
import datetime

def todos_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'consulta_orm/todos_clientes.html', {'clientes': clientes})

def clientes_activos(request):
    clientes = Cliente.objects.filter(activo=True)
    return render(request, 'consulta_orm/clientes_activos.html', {'clientes': clientes})

def clientes_rango_fechas(request):
    inicio = datetime.date(1980, 1, 1)
    final = datetime.date(2000, 12, 31)
    clientes = Cliente.objects.filter(fecha_nacimiento__range=(inicio, final))
    return render(request, 'consulta_orm/clientes_rango_fechas.html', {'clientes': clientes})
