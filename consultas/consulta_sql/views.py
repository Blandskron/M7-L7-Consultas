from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseBadRequest

def todas_facturas(request):
    query = "SELECT * FROM consulta_sql_factura"
    with connection.cursor() as cursor:
        cursor.execute(query)
        columnas = [col[0] for col in cursor.description]
        facturas = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    return render(request, 'consulta_sql/todas_facturas.html', {'facturas': facturas})

def facturas_pagadas(request):
    query = "SELECT * FROM consulta_sql_factura WHERE pagada = TRUE"
    with connection.cursor() as cursor:
        cursor.execute(query)
        columnas = [col[0] for col in cursor.description]
        facturas = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    return render(request, 'consulta_sql/facturas_pagadas.html', {'facturas': facturas})


def facturas_por_cliente(request, cliente_id):
    # Validación de cliente_id ya no es necesaria porque <int:cliente_id> asegura que sea un número
    query = "SELECT * FROM consulta_sql_factura WHERE cliente_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, [cliente_id])
        columnas = [col[0] for col in cursor.description]
        facturas = [dict(zip(columnas, row)) for row in cursor.fetchall()]

    return render(request, 'consulta_sql/facturas_por_cliente.html', {'facturas': facturas})

