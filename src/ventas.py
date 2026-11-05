"""Registro de ventas, IVA, comprobantes y descuento de existencias."""
from datetime import datetime
from decimal import Decimal
from .archivos import leer_datos, guardar_datos
from .productos import obtener_productos, buscar_producto
from .inventario import movimiento
from .estructuras import dinero, entero_positivo, pedir_texto, pedir_entero

IVA = Decimal('0.12')

def calcular_totales(detalle):
    subtotal = sum((dinero(x['precio']) * int(x['cantidad']) for x in detalle), Decimal('0'))
    subtotal = dinero(subtotal)
    impuesto = dinero(subtotal * IVA)
    return subtotal, impuesto, dinero(subtotal + impuesto)

def registrar_venta(items, fecha=None):
    """items: [(codigo, cantidad), ...]. Precios de catálogo SIN IVA."""
    if not items: raise ValueError('La venta necesita al menos un producto.')
    productos = obtener_productos()
    cantidades = {}
    for codigo, cantidad in items:
        p = buscar_producto(productos, codigo)
        if not p or not p['activo']: raise ValueError(f'Producto no disponible: {codigo}')
        cantidad = entero_positivo(cantidad)
        cantidades[p['codigo']] = cantidades.get(p['codigo'], 0) + cantidad
    detalle = []
    for codigo, cantidad in cantidades.items():
        p = buscar_producto(productos, codigo)
        if cantidad > p['cantidad']: raise ValueError(f'Stock insuficiente para {codigo}. Disponible: {p["cantidad"]}')
        detalle.append({'codigo': codigo, 'nombre': p['nombre'], 'precio': str(dinero(p['precio'])),
                        'cantidad': cantidad, 'subtotal': str(dinero(dinero(p['precio']) * cantidad))})
    subtotal, iva, total = calcular_totales(detalle)
    ventas = leer_datos('ventas.json')
    movimientos = leer_datos('movimientos.json')
    numero = max([int(v['numero']) for v in ventas] + [0]) + 1
    fecha = fecha or datetime.now().isoformat(timespec='seconds')
    venta = {'numero': numero, 'fecha': fecha, 'detalle': detalle,
             'subtotal': str(subtotal), 'iva': str(iva), 'total': str(total)}
    for linea in detalle:
        buscar_producto(productos, linea['codigo'])['cantidad'] -= linea['cantidad']
        movimientos.append(movimiento(linea['codigo'], 'SALIDA', linea['cantidad'],
                                      f'Venta número {numero}', fecha))
    # Se preparan todos los datos antes de escribir. Con archivos JSON no hay
    # transacciones reales entre tres archivos: consultar manual técnico.
    guardar_datos('ventas.json', ventas + [venta])
    guardar_datos('movimientos.json', movimientos)
    guardar_datos('productos.json', productos)
    return venta

def mostrar_comprobante(v):
    print(f"\nVENTA N.º {v['numero']} | {v['fecha']}")
    for x in v['detalle']:
        print(f"{x['codigo']} {x['nombre']} x{x['cantidad']} = Q{x['subtotal']}")
    print(f"Subtotal: Q{v['subtotal']} | IVA 12%: Q{v['iva']} | TOTAL: Q{v['total']}")

def venta_interactiva():
    items = []
    while True:
        codigo = pedir_texto('Código del producto: ')
        cantidad = pedir_entero('Unidades: ', positivo=True)
        items.append((codigo, cantidad))
        if input('¿Agregar otro producto? (s/n): ').strip().lower() != 's': break
    venta = registrar_venta(items)
    mostrar_comprobante(venta)

def menu_ventas():
    while True:
        print('\n--- VENTAS ---\n1. Registrar venta\n2. Ver historial\n0. Volver')
        op = input('Opción: ').strip()
        if op == '0': return
        if op == '1': venta_interactiva()
        elif op == '2':
            ventas = leer_datos('ventas.json')
            if not ventas: print('No hay ventas.')
            for v in ventas: mostrar_comprobante(v)
        else: print('Opción inválida.')
