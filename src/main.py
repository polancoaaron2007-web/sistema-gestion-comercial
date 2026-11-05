"""Punto de entrada del sistema. Ejecutar: python -m src.main"""
from .archivos import ErrorDatos
from .productos import menu_productos
from .ventas import menu_ventas
from .inventario import menu_inventario
from .reportes import menu_reportes

def main():
    opciones = {'1': menu_productos, '2': menu_ventas,
                '3': menu_inventario, '4': menu_reportes}
    while True:
        print('\n====== SISTEMA DE GESTIÓN COMERCIAL ======')
        print('1. Productos\n2. Ventas\n3. Inventario\n4. Reportes\n5. Salir')
        opcion = input('Selecciona una opción: ').strip()
        if opcion == '5': print('Hasta pronto.'); return
        if opcion not in opciones: print('Opción inválida.'); continue
        try:
            opciones[opcion]()
        except (ValueError, ErrorDatos, KeyError, TypeError) as exc:
            print('No se pudo completar la operación:', exc)

if __name__ == '__main__':
    try: main()
    except (EOFError, KeyboardInterrupt): print('\nSalida controlada.')
