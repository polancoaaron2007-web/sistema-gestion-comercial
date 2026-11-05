"""Entradas de inventario e historial de movimientos."""
from datetime import datetime
from .archivos import leer_datos, guardar_datos
from .productos import obtener_productos, buscar_producto, mostrar_producto
from .estructuras import entero_positivo, pedir_texto, pedir_entero

ARCHIVO = 'movimientos.json'

def movimiento(codigo, tipo, cantidad, descripcion, fecha=None):
    return {'fecha': fecha or datetime.now().isoformat(timespec='seconds'),
            'codigo': codigo, 'tipo': tipo, 'cantidad': entero_positivo(cantidad),
            'descripcion': descripcion}

def registrar_entrada(codigo, cantidad, descripcion):
    productos = obtener_productos()
    p = buscar_producto(productos, codigo)
    if not p: raise ValueError('El producto no existe.')
    if not p['activo']: raise ValueError('No se puede ingresar a un producto inactivo.')
    cantidad = entero_positivo(cantidad)
    movimientos = leer_datos(ARCHIVO)
    p['cantidad'] += cantidad
    movimientos.append(movimiento(p['codigo'], 'ENTRADA', cantidad, descripcion))
    # El movimiento se guarda primero; si falla, no se cambia el catálogo.
    guardar_datos(ARCHIVO, movimientos)
    guardar_datos('productos.json', productos)
    return p['cantidad']

def consultar_existencias():
    for p in obtener_productos(): mostrar_producto(p)

def entrada_interactiva():
    codigo = pedir_texto('Código: ')
    cantidad = pedir_entero('Cantidad de entrada: ', positivo=True)
    descripcion = pedir_texto('Descripción del movimiento: ')
    print('Existencias actualizadas:', registrar_entrada(codigo, cantidad, descripcion))

def alertas():
    productos = obtener_productos()

    encontrados = [
        p for p in productos
        if p['cantidad'] <= p['stock_minimo']
    ]

    if not encontrados:
        print('No hay productos con existencias bajas.')
        return

    print('\n--- PRODUCTOS CON STOCK BAJO ---')

    for p in encontrados:
        mostrar_producto(p)

def historial():
    movimientos = leer_datos(ARCHIVO)
    if not movimientos: print('Sin movimientos.')
    for m in movimientos:
        print(f"{m['fecha']} | {m['codigo']} | {m['tipo']} | {m['cantidad']} | {m['descripcion']}")

def menu_inventario():
    opciones = {'1': consultar_existencias, '2': entrada_interactiva,
                '3': alertas, '4': historial}
    while True:
        print('\n--- INVENTARIO ---\n1. Consultar existencias\n2. Registrar entrada\n3. Alertas stock mínimo\n4. Historial movimientos\n0. Volver')
        op = input('Opción: ').strip()
        if op == '0': return
        if op in opciones: opciones[op]()
        else: print('Opción inválida.')
