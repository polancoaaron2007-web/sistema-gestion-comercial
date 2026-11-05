# Guía de entrega en GitHub
1. Un integrante crea repositorio público `sistema-gestion-comercial` en GitHub sin agregar otro README.
2. Desde la carpeta del proyecto: `git init`, `git add .`, `git commit -m "Crear estructura y datos de ejemplo"`, `git branch -M main`, `git remote add origin URL_DEL_REPOSITORIO`, `git push -u origin main`.
3. Para cumplir ocho commits **reales**, dividir el desarrollo en cambios verificables. Ejemplos de mensajes: `Implementar validaciones de productos`, `Agregar registro de ventas e IVA`, `Registrar movimientos de inventario`, `Crear reportes estadísticos`, `Agregar pruebas automatizadas`, `Documentar procesos y diagramas`, `Redactar manuales`, `Mejorar mensajes de error`. No crear commits vacíos para aparentar actividad.
4. Crear rama: `git switch -c mejora-reportes`. Realizar una mejora real, `git add .`, `git commit -m "Mejorar reporte mensual"`, `git push -u origin mejora-reportes`. Abrir Pull Request en GitHub y fusionarlo tras revisión del equipo.
5. Crear al menos dos Issues: uno para un problema detectado y otro para una mejora pendiente. Documentar pasos y resultado.
6. Crear release/tag `v1.0.0` cuando todo esté probado.
7. Cada integrante debe realizar contribuciones verificables desde su cuenta. No inventar commits, capturas o autorías.
8. Subir capturas auténticas a `evidencias/`, comprobar que los JSON de ejemplo estén versionados y que una descarga nueva pueda ejecutar `python -m src.main`.
9. No subir contraseñas, tokens ni datos personales.
