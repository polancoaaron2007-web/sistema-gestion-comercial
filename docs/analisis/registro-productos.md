# Registro de productos

**Nombre del proceso:** Registro de productos.

**Objetivo:** Crear productos únicos y válidos.

**Descripción:** El usuario elige la opción del menú, el sistema obtiene la información, aplica las validaciones y muestra el resultado. Si ocurre un error, informa al usuario y permite volver al menú.

**Datos de entrada:** Código, nombre, categoría, precio, cantidad y mínimo.

**Procesamiento:** Validar campos y duplicados; guardar JSON.

**Datos de salida:** Producto nuevo o mensaje de error.

**Reglas de negocio:** Código único; no negativos; campos obligatorios.

**Validaciones y errores:** Duplicado, vacío, formato numérico, archivo inaccesible.

**Diagrama:** `docs/diagramas/registro-productos.mmd` (abrir en Mermaid o importar a diagrams.net).
