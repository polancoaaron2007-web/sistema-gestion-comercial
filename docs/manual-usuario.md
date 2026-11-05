# Manual de usuario
## 1. Presentación
El sistema permite administrar productos, ventas, inventario y reportes desde una terminal.
## 2. Requisitos
Python 3.10+ y acceso de escritura a la carpeta del proyecto. No necesita conocimientos de programación.
## 3. Inicio y cierre
Abra una terminal en la carpeta principal y ejecute `python -m src.main`. Seleccione `5` para salir. En los submenús, `0` regresa al principal.
## 4. Menú principal
`1` Productos, `2` Ventas, `3` Inventario, `4` Reportes, `5` Salir.
## 5. Productos
Elija `1 > 1` para registrar: código único, nombre, categoría, precio sin IVA, existencias iniciales y stock mínimo. `1 > 2` consulta por código; `1 > 3` lista; `1 > 4` modifica nombre/categoría/precio/mínimo o reactiva; `1 > 5` desactiva. El cambio de existencias se hace en Inventario.
## 6. Ventas
Elija `2 > 1`. Ingrese código y unidades, agregue más productos si desea. El sistema valida la existencia y muestra un comprobante con subtotal, IVA 12 % y total. `2 > 2` muestra historial.
## 7. Inventario
`3 > 1` consulta existencias; `3 > 2` registra entradas indicando código, unidades y descripción; `3 > 3` muestra productos activos con stock igual o inferior al mínimo; `3 > 4` muestra movimientos.
## 8. Reportes
En `4` elija del 1 al 8: catálogo, stock bajo, historial, ingresos, más vendido, valor inventario, promedios mensuales o matriz de ventas.
## 9. Errores frecuentes
`Opción inválida`: seleccione un número del menú. `Ya existe ese código`: use otro código. `Producto no disponible`: compruebe el código y que esté activo. `Stock insuficiente`: reduzca unidades o registre una entrada. `Error de lectura`: compruebe que el JSON esté bien formado.
## 10. Ejemplos
Para registrar un producto: `1 > 1`, código `P100`, nombre `Memoria USB`, categoría `Almacenamiento`, precio `60`, existencias `10`, mínimo `2`. Para vender una unidad: `2 > 1`, código `P100`, cantidad `1`, agregar otro `n`. **Capturas reales pendientes**: guardar imágenes en `evidencias/` después de ejecutar.
## 11. Conservación de archivos
Mantenga una copia de seguridad de `datos/`. No borre ni edite manualmente los archivos JSON mientras usa el sistema. Al descargar el repositorio, los ejemplos ya están incluidos.
