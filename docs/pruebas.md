# Plan de pruebas y evidencias
Ejecutar primero `python -m unittest discover -s tests -v`. La columna "obtenido" se llena después de ejecutar en la computadora del equipo; no se afirma haber tomado capturas.

| Caso | Datos | Esperado | Obtenido | Conclusión |
|---|---|---|---|---|
| T01 producto válido | P100, USB, 60, 10, mínimo 2 | Se registra | Pendiente de captura | Pendiente |
| T02 código duplicado | P001 existente | Error | Pendiente de captura | Pendiente |
| T03 cantidad negativa | -3 | Error | Pendiente de captura | Pendiente |
| T04 dato incorrecto | `abc` como cantidad | Error | Pendiente de captura | Pendiente |
| T05 venta sin stock | P002, 100 unidades | Error sin descontar | Pendiente de captura | Pendiente |
| T06 consulta inexistente | Z999 | Producto inexistente | Pendiente de captura | Pendiente |
| T07 IVA | P001, 2 unidades, precio Q125 | Subtotal Q250, IVA Q30, total Q280 | Pendiente de captura | Pendiente |
| T08 matriz | Venta ejemplo de Q325 + IVA Q39 | `[3,325,39,364]` | Pendiente de captura | Pendiente |
| T09 entrada | P001 +3 | Stock aumenta 3 y queda movimiento | Pendiente de captura | Pendiente |
| T10 reporte | Datos de ejemplo | Ingresos Q364, más vendido P001 (2) | Pendiente de captura | Pendiente |

Guardar capturas con nombres `evidencias/T01.png`, etc. No reemplazar evidencias con imágenes simuladas.
