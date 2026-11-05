# Sistema de Gestión Comercial
Proyecto académico de Algoritmos, segundo semestre de Ingeniería en Sistemas.

## Requisitos
Python 3.10 o superior. No requiere instalar paquetes ni conexión a internet.

## Ejecutar
1. Descargar el ZIP del repositorio (Code > Download ZIP) o clonar con Git.
2. Abrir una terminal en la carpeta `sistema-gestion-comercial` (donde está este README).
3. Ejecutar `python -m src.main` (Windows también puede usar `py -m src.main`).
4. Elegir una opción del menú. Para salir, elegir 5.

## Datos incluidos
`datos/productos.json`, `datos/ventas.json` y `datos/movimientos.json` contienen ejemplos coherentes para probar el sistema. **Se modifican al usar el programa**. Para restaurarlos, volver a extraer el ZIP o usar `git restore datos/`.

## Módulos
- Productos: registrar, buscar, listar, modificar, desactivar y reactivar.
- Ventas: varios productos, validación de stock, IVA 12 %, comprobante y salidas.
- Inventario: entradas, existencias, alertas e historial.
- Reportes: productos, stock bajo, ventas, ingresos, más vendido, valor del inventario, promedios mensuales y matriz de ventas.

## Criterios
Los precios del catálogo se ingresan **sin IVA**; se agrega 12 % en cada venta. El valor del inventario se calcula a precio de venta, no a costo de adquisición. El promedio mensual es el promedio del importe total de las ventas registradas en cada mes. Se usa `Decimal` para dinero.

## Pruebas
Ejecutar `python -m unittest discover -s tests -v` desde la raíz. Las pruebas usan carpetas temporales y no modifican los datos de ejemplo.

## Documentación
Consultar `docs/analisis/`, `docs/diagramas/`, `docs/manual-tecnico.md`, `docs/manual-usuario.md` y `docs/pruebas.md`.

## GitHub
El repositorio debe ser creado y publicado por el equipo. Commits, issues, rama, pull request, release y capturas de ejecución deben realizarse realmente; no se simulan. Ver `docs/guia-github.md`.

## Limitación
JSON es adecuado para un proyecto educativo de uso local y un usuario a la vez. Una falla de escritura entre archivos podría dejar datos parcialmente actualizados; para producción se recomendaría una base de datos con transacciones.
