import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from src import archivos, productos, ventas, inventario, reportes

class SistemaTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.parche = patch.object(archivos, 'DATOS', Path(self.temp.name))
        self.parche.start()
        self.addCleanup(self.parche.stop)
        productos.crear_producto('P1', 'Teclado', 'Accesorios', '125', 5, 2)
        productos.crear_producto('P2', 'Mouse', 'Accesorios', '75', 2, 2)

    def test_registro_y_duplicado(self):
        self.assertEqual(len(productos.obtener_productos()), 2)
        with self.assertRaises(ValueError):
            productos.crear_producto('p1', 'Otro', 'Accesorios', 10, 1, 1)

    def test_cantidades_invalidas(self):
        with self.assertRaises(ValueError):
            productos.crear_producto('P3', 'Error', 'Test', 2, -1, 1)
        with self.assertRaises(ValueError):
            productos.crear_producto('P3', 'Error', 'Test', 2, 'abc', 1)

    def test_stock_insuficiente_no_modifica(self):
        with self.assertRaises(ValueError): ventas.registrar_venta([('P1', 6)])
        self.assertEqual(productos.obtener_productos()[0]['cantidad'], 5)
        self.assertEqual(archivos.leer_datos('ventas.json'), [])

    def test_producto_inexistente(self):
        self.assertIsNone(productos.buscar_producto(productos.obtener_productos(), 'Z999'))
        with self.assertRaises(ValueError): ventas.registrar_venta([('Z999', 1)])

    def test_iva_y_movimientos(self):
        v = ventas.registrar_venta([('P1', 2)], fecha='2026-11-01T10:00:00')
        self.assertEqual((v['subtotal'], v['iva'], v['total']), ('250.00', '30.00', '280.00'))
        self.assertEqual(productos.obtener_productos()[0]['cantidad'], 3)
        self.assertEqual(archivos.leer_datos('movimientos.json')[0]['tipo'], 'SALIDA')

    def test_entrada_y_alertas(self):
        self.assertEqual(inventario.registrar_entrada('P2', 3, 'Reposición'), 5)
        self.assertEqual(archivos.leer_datos('movimientos.json')[0]['tipo'], 'ENTRADA')

    def test_reportes_y_matriz(self):
        ventas.registrar_venta([('P1', 2), ('P2', 1)], fecha='2026-11-01T10:00:00')
        r = reportes.generar_reporte()
        self.assertEqual(r['ingresos'], 364)
        self.assertEqual(r['mas_vendido'], ('P1', 2))
        self.assertEqual(r['matriz'], [[3, 325.0, 39.0, 364.0]])
        self.assertEqual(r['promedios_mensuales']['2026-11'], 364)

    def test_archivo_invalido(self):
        (Path(self.temp.name) / 'ventas.json').write_text('{mal json', encoding='utf-8')
        with self.assertRaises(archivos.ErrorDatos): archivos.leer_datos('ventas.json')

if __name__ == '__main__': unittest.main()
