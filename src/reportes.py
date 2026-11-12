
"""Reportes calculados exclusivamente desde archivos JSON."""

from collections import defaultdict
from datetime import datetime
from decimal import Decimal

from .archivos import leer_datos
from .productos import obtener_productos, mostrar_producto
from .estructuras import dinero, matriz_ventas


def generar_reporte():
    productos = obtener_productos()
    ventas = leer_datos('ventas.json')

    unidades = defaultdict(int)
    periodos = defaultdict(list)

    # Recorrer las ventas registradas
    for v in ventas:
        periodo = datetime.fromisoformat(v['fecha']).strftime('%Y-%m')
        periodos[periodo].append(dinero(v['total']))

        for d in v['detalle']:
            unidades[d['codigo']] += int(d['cantidad'])

    # Identificar todos los productos con mayor cantidad vendida
    maximo = max(unidades.values(), default=0)

    mas_vendidos = [
        (codigo, cantidad)
        for codigo, cantidad in unidades.items()
        if cantidad == maximo
    ]

    # Calcular los reportes desde los datos almacenados
    return {
        'productos': productos,

        'bajo_stock': [
            p for p in productos
            if p['activo'] and p['cantidad'] <= p['stock_minimo']
        ],

        'ventas': ventas,

        'ingresos': sum(
            (dinero(v['total']) for v in ventas),
            Decimal('0')
        ),

        'mas_vendido': mas_vendidos,

        'valor_inventario': sum(
            (dinero(p['precio']) * p['cantidad'] for p in productos),
            Decimal('0')
        ),

        'promedios_mensuales': {
            mes: dinero(sum(totales) / len(totales))
            for mes, totales in sorted(periodos.items())
        },

        'matriz': matriz_ventas(ventas)
    }


def menu_reportes():
    while True:
        print('\n========== REPORTES Y ESTADÍSTICAS ==========')
        print('1. Listado general de productos')
        print('2. Productos con bajo stock')
        print('3. Historial de ventas')
        print('4. Total de ingresos')
        print('5. Productos más vendidos')
        print('6. Valor total del inventario')
        print('7. Promedios mensuales')
        print('8. Matriz de ventas')
        print('0. Volver al menú principal')

        op = input('\nSeleccione una opción: ').strip()

        if op == '0':
            return

        if op not in ('1', '2', '3', '4', '5', '6', '7', '8'):
            print('\nOpción inválida. Intente nuevamente.')
            continue

        r = generar_reporte()

        # REPORTE 1: LISTADO GENERAL DE PRODUCTOS
        if op == '1':
            print('\n========== LISTADO DE PRODUCTOS ==========')

            if not r['productos']:
                print('No hay productos registrados.')
            else:
                for p in r['productos']:
                    mostrar_producto(p)

        # REPORTE 2: PRODUCTOS CON BAJO STOCK
        elif op == '2':
            print('\n========== PRODUCTOS CON BAJO STOCK ==========')

            if not r['bajo_stock']:
                print('No hay productos con existencias bajas.')
            else:
                for p in r['bajo_stock']:
                    mostrar_producto(p)

        # REPORTE 3: HISTORIAL DE VENTAS
        elif op == '3':
            print('\n========== HISTORIAL DE VENTAS ==========')

            if not r['ventas']:
                print('No hay ventas registradas.')
            else:
                from .ventas import mostrar_comprobante

                for v in r['ventas']:
                    mostrar_comprobante(v)

        # REPORTE 4: TOTAL DE INGRESOS
        elif op == '4':
            print('\n========== TOTAL DE INGRESOS ==========')
            print(f"Ingresos totales (IVA incluido): Q{r['ingresos']:.2f}")

        # REPORTE 5: PRODUCTOS MÁS VENDIDOS
        elif op == '5':
            print('\n========== PRODUCTOS MÁS VENDIDOS ==========')

            if not r['mas_vendido']:
                print('No hay ventas registradas.')
            else:
                for codigo, cantidad in r['mas_vendido']:
                    producto = next(
                        (p for p in r['productos']
                         if p['codigo'] == codigo),
                        None
                    )

                    nombre = (
                        producto['nombre']
                        if producto
                        else 'Producto no encontrado'
                    )

                    print(f'\nCódigo: {codigo}')
                    print(f'Producto: {nombre}')
                    print(f'Unidades vendidas: {cantidad}')

                if len(r['mas_vendido']) > 1:
                    print(
                        f"\nHay {len(r['mas_vendido'])} productos "
                        "empatados como los más vendidos."
                    )

            print('===========================================')

        # REPORTE 6: VALOR DEL INVENTARIO
        elif op == '6':
            print('\n========== VALOR DEL INVENTARIO ==========')
            print(
                f"Valor total a precio de venta sin IVA: "
                f"Q{r['valor_inventario']:.2f}"
            )

        # REPORTE 7: PROMEDIOS MENSUALES
        elif op == '7':
            print('\n========== PROMEDIOS MENSUALES ==========')

            if not r['promedios_mensuales']:
                print('No hay ventas registradas.')
            else:
                for mes, promedio in r['promedios_mensuales'].items():
                    print(f'Mes: {mes} | Promedio por venta: Q{promedio:.2f}')

        # REPORTE 8: MATRIZ DE VENTAS
        elif op == '8':
            print('\n========== MATRIZ DE VENTAS ==========')
            print('Columnas: Unidades | Subtotal | IVA | Total')

            if not r['matriz']:
                print('No hay ventas registradas.')
            else:
                for fila in r['matriz']:
                    print(fila)

        print('\nReporte generado correctamente.')
