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
    for v in ventas:
        periodo = datetime.fromisoformat(v['fecha']).strftime('%Y-%m')
        periodos[periodo].append(dinero(v['total']))
        for d in v['detalle']:
            unidades[d['codigo']] += int(d['cantidad'])
    mayor = max(unidades, key=unidades.get) if unidades else None
    return {'productos': productos,
            'bajo_stock': [p for p in productos if p['activo'] and p['cantidad'] <= p['stock_minimo']],
            'ventas': ventas,
            'ingresos': sum((dinero(v['total']) for v in ventas), Decimal('0')),
            'mas_vendido': (mayor, unidades[mayor]) if mayor else None,
            'valor_inventario': sum((dinero(p['precio']) * p['cantidad'] for p in productos), Decimal('0')),
            'promedios_mensuales': {mes: dinero(sum(totales) / len(totales))
                                    for mes, totales in sorted(periodos.items())},
            'matriz': matriz_ventas(ventas)}

def menu_reportes():
    while True:
        print('\n--- REPORTES ---\n1. Productos\n2. Bajo stock\n3. Historial ventas\n4. Ingresos\n5. Más vendido\n6. Valor inventario\n7. Promedios mensuales\n8. Matriz ventas\n0. Volver')
        op = input('Opción: ').strip()
        if op == '0': return
        if op not in '12345678' or len(op) != 1: print('Opción inválida.'); continue
        r = generar_reporte()
        if op in ('1','2'):
            for p in r['productos' if op == '1' else 'bajo_stock']: mostrar_producto(p)
        elif op == '3':
            from .ventas import mostrar_comprobante
            for v in r['ventas']: mostrar_comprobante(v)
        elif op == '4': print(f"Ingresos totales (IVA incluido): Q{r['ingresos']:.2f}")
        elif op == '5': print('Más vendido (código, unidades):', r['mas_vendido'] or 'Sin ventas')
        elif op == '6': print(f"Valor inventario a precio de venta sin IVA: Q{r['valor_inventario']:.2f}")
        elif op == '7':
            if not r['promedios_mensuales']: print('Sin ventas.')
            for mes, promedio in r['promedios_mensuales'].items(): print(mes, f'Q{promedio:.2f} por venta')
        elif op == '8':
            print('Matriz [unidades, subtotal, IVA, total]:')
            for fila in r['matriz']: print(fila)
