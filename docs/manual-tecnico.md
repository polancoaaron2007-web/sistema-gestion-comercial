# Manual técnico
## Arquitectura
Aplicación de consola con biblioteca estándar de Python 3.10+. Entrada `src/main.py`, ejecutado como módulo con `python -m src.main`. Cada módulo contiene funciones y un submenú.

## Archivos
`src/productos.py` CRUD básico; `src/ventas.py` venta e IVA; `src/inventario.py` movimientos; `src/reportes.py` agregaciones; `src/archivos.py` lectura y escritura JSON; `src/estructuras.py` validación, Decimal y matriz; `src/main.py` menú y manejo de errores.

## Datos
Todos los JSON son listas. Productos: código, nombre, categoría, precio (cadena decimal), cantidad (entero), stock_minimo (entero), activo (booleano). Ventas: número, fecha ISO, detalle, subtotal, iva y total. Movimientos: fecha, código, tipo ENTRADA/SALIDA, cantidad y descripción. Los archivos se buscan respecto a la raíz del proyecto, independientemente del directorio de ejecución.

## Lógica
Códigos únicos sin distinguir mayúsculas; cantidades enteras no negativas; ventas y entradas requieren unidades positivas. Los productos inactivos no se venden. Se valida toda la venta antes de descontar existencias. El IVA se calcula con `Decimal` y redondeo a dos decimales, sobre el subtotal sin IVA. La matriz de ventas tiene columnas `[unidades, subtotal, IVA, total]`.

## Reportes
Ingresos: suma de totales de ventas (IVA incluido). Más vendido: suma de unidades por código. Valor inventario: suma de cantidad por precio sin IVA, incluso productos inactivos con existencias; se trata de valor comercial, no costo. Promedio mensual: media del total de las ventas de cada mes registrado; no incluye meses sin ventas.

## Pruebas
`python -m unittest discover -s tests -v`. Se sustituyen las rutas de datos con carpetas temporales en las pruebas.

## Limitaciones y recuperación
El guardado individual usa reemplazo atómico del JSON, pero **no existe transacción atómica entre los tres archivos** de una venta. Una interrupción entre guardados puede causar inconsistencias. Antes de operaciones importantes, hacer respaldo de `datos/`. Es una demostración educativa, no un sistema multiusuario de producción. No guarda credenciales ni datos personales.

## Instalación y mantenimiento
Descargar el repositorio completo, conservar la carpeta `datos/`, ejecutar desde la raíz. Para restaurar ejemplos, usar `git restore datos/` o extraer nuevamente el ZIP. Las rutas no dependen de la computadora del equipo.
