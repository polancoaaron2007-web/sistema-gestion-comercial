# Actualización de inventario

**Nombre del proceso:** Actualización de inventario.

**Objetivo:** Registrar entradas y consultar movimientos.

**Descripción:** El usuario elige la opción del menú, el sistema obtiene la información, aplica las validaciones y muestra el resultado. Si ocurre un error, informa al usuario y permite volver al menú.

**Datos de entrada:** Código, unidades, descripción.

**Procesamiento:** Validar; sumar existencias; guardar movimiento.

**Datos de salida:** Existencias y registro.

**Reglas de negocio:** Solo activos; cantidad positiva.

**Validaciones y errores:** Código inexistente, cantidad inválida, archivo inaccesible.

**Diagrama:** `docs/diagramas/actualizacion-inventario.mmd` (abrir en Mermaid o importar a diagrams.net).
