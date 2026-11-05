# Consulta y modificación

**Nombre del proceso:** Consulta y modificación.

**Objetivo:** Consultar y actualizar datos de un producto.

**Descripción:** El usuario elige la opción del menú, el sistema obtiene la información, aplica las validaciones y muestra el resultado. Si ocurre un error, informa al usuario y permite volver al menú.

**Datos de entrada:** Código, opción y nuevo valor.

**Procesamiento:** Buscar código; validar modificación; guardar.

**Datos de salida:** Ficha actualizada o mensaje.

**Reglas de negocio:** No modificar código; cantidades mediante Inventario.

**Validaciones y errores:** Código inexistente, valor inválido, archivo dañado.

**Diagrama:** `docs/diagramas/consulta-modificacion.mmd` (abrir en Mermaid o importar a diagrams.net).
