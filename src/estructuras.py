"""Validaciones reutilizables y matriz para el análisis de ventas."""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

DOS = Decimal('0.01')

def dinero(valor):
    try:
        numero = Decimal(str(valor))
    except (InvalidOperation, ValueError):
        raise ValueError('El precio debe ser numérico.')
    if not numero.is_finite() or numero < 0:
        raise ValueError('El precio debe ser finito y no negativo.')
    return numero.quantize(DOS, rounding=ROUND_HALF_UP)

def entero_no_negativo(valor):
    if isinstance(valor, bool) or not str(valor).isdigit():
        raise ValueError('La cantidad debe ser un entero no negativo.')
    return int(valor)

def entero_positivo(valor):
    numero = entero_no_negativo(valor)
    if numero == 0:
        raise ValueError('La cantidad debe ser mayor que cero.')
    return numero

def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print('Error: el texto no puede estar vacío.')

def pedir_entero(mensaje, positivo=False):
    while True:
        try:
            valor = input(mensaje).strip()
            return entero_positivo(valor) if positivo else entero_no_negativo(valor)
        except ValueError as exc:
            print('Error:', exc)

def pedir_precio(mensaje):
    while True:
        try:
            return dinero(input(mensaje).strip())
        except ValueError as exc:
            print('Error:', exc)

def matriz_ventas(ventas):
    """Cada fila: [unidades, subtotal, iva, total]."""
    return [[sum(int(x['cantidad']) for x in v['detalle']),
             float(dinero(v['subtotal'])), float(dinero(v['iva'])),
             float(dinero(v['total']))] for v in ventas]
