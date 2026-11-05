"""Operaciones del catálogo de productos."""
from .archivos import leer_datos, guardar_datos
from .estructuras import dinero, entero_no_negativo, pedir_texto, pedir_entero, pedir_precio

ARCHIVO = 'productos.json'

def obtener_productos():
    return leer_datos(ARCHIVO)

def buscar_producto(productos, codigo):
    return next((p for p in productos if p['codigo'].upper() == codigo.upper()), None)

def crear_producto(codigo, nombre, categoria, precio, cantidad, stock_minimo, productos=None):
    productos = obtener_productos() if productos is None else productos
    if not all(isinstance(x, str) and x.strip() for x in (codigo, nombre, categoria)):
        raise ValueError('Código, nombre y categoría son obligatorios.')
    if buscar_producto(productos, codigo.strip()):
        raise ValueError('Ya existe ese código.')
    producto = {'codigo': codigo.strip().upper(), 'nombre': nombre.strip(),
                'categoria': categoria.strip(), 'precio': str(dinero(precio)),
                'cantidad': entero_no_negativo(cantidad),
                'stock_minimo': entero_no_negativo(stock_minimo), 'activo': True}
    productos.append(producto)
    guardar_datos(ARCHIVO, productos)
    return producto

def mostrar_producto(p):
    print(f"{p['codigo']} | {p['nombre']} | {p['categoria']} | Q{dinero(p['precio']):.2f} | "
          f"Existencias: {p['cantidad']} | Mínimo: {p['stock_minimo']} | "
          f"{'Activo' if p['activo'] else 'Inactivo'}")

def registrar_producto():
    print('\n--- REGISTRO DE PRODUCTO ---')
    codigo = pedir_texto('Código: ')
    if buscar_producto(obtener_productos(), codigo):
        print('Error: el código ya está registrado.'); return
    nombre = pedir_texto('Nombre: ')
    categoria = pedir_texto('Categoría: ')
    precio = pedir_precio('Precio de venta sin IVA (Q): ')
    cantidad = pedir_entero('Existencias iniciales: ')
    minimo = pedir_entero('Stock mínimo: ')
    crear_producto(codigo, nombre, categoria, precio, cantidad, minimo)
    print('Producto registrado correctamente.')

def consultar_producto():
    p = buscar_producto(obtener_productos(), pedir_texto('Código a buscar: '))
    mostrar_producto(p) if p else print('Producto inexistente.')

def listar_productos():
    productos = obtener_productos()
    if not productos: print('No hay productos registrados.')
    for p in productos: mostrar_producto(p)

def modificar_producto():
    productos = obtener_productos()
    p = buscar_producto(productos, pedir_texto('Código a modificar: '))
    if not p: print('Producto inexistente.'); return
    print('1. Nombre  2. Categoría  3. Precio  4. Stock mínimo  5. Reactivar')
    op = input('Campo: ').strip()
    if op == '1': p['nombre'] = pedir_texto('Nuevo nombre: ')
    elif op == '2': p['categoria'] = pedir_texto('Nueva categoría: ')
    elif op == '3': p['precio'] = str(pedir_precio('Nuevo precio (Q): '))
    elif op == '4': p['stock_minimo'] = pedir_entero('Nuevo stock mínimo: ')
    elif op == '5': p['activo'] = True
    else: print('Opción inválida.'); return
    guardar_datos(ARCHIVO, productos)
    print('Producto actualizado.')

def desactivar_producto():
    productos = obtener_productos()
    p = buscar_producto(productos, pedir_texto('Código a desactivar: '))
    if not p: print('Producto inexistente.'); return
    if not p['activo']: print('El producto ya está inactivo.'); return
    p['activo'] = False
    guardar_datos(ARCHIVO, productos)
    print('Producto desactivado. Se conserva su historial.')

def menu_productos():
    opciones = {'1': registrar_producto, '2': consultar_producto,
                '3': listar_productos, '4': modificar_producto, '5': desactivar_producto}
    while True:
        print('\n--- PRODUCTOS ---\n1. Registrar\n2. Consultar por código\n3. Listar\n4. Modificar\n5. Desactivar\n0. Volver')
        op = input('Opción: ').strip()
        if op == '0': return
        if op in opciones: opciones[op]()
        else: print('Opción inválida.')
