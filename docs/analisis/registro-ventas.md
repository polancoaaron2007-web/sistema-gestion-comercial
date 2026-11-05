# Registro de ventas

**Nombre del proceso:** Registro de ventas.

**Objetivo:** Cobrar y descontar productos disponibles.

**Descripción:** El usuario elige la opción del menú, el sistema obtiene la información, aplica las validaciones y muestra el resultado. Si ocurre un error, informa al usuario y permite volver al menú.

**Datos de entrada:** Lista de códigos y cantidades.

**Procesamiento:** Validar stock; sumar subtotales; IVA 12%; guardar venta y salidas.

**Datos de salida:** Comprobante, venta y existencias actualizadas.

**Reglas de negocio:** Solo activos; unidades positivas; no vender más que stock.

**Validaciones y errores:** Producto inexistente, insuficiencia, archivo inaccesible.

**Diagrama:** `docs/diagramas/registro-ventas.mmd` (abrir en Mermaid o importar a diagrams.net).
