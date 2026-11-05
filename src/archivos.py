"""Lectura y escritura segura de archivos JSON del proyecto."""
import json
import os
import tempfile
from pathlib import Path

DATOS = Path(__file__).resolve().parent.parent / 'datos'

class ErrorDatos(Exception):
    pass

def leer_datos(nombre):
    ruta = DATOS / nombre
    if not ruta.exists():
        return []
    try:
        with ruta.open('r', encoding='utf-8') as archivo:
            contenido = json.load(archivo)
        if not isinstance(contenido, list):
            raise ErrorDatos(f'{nombre} debe contener una lista JSON.')
        return contenido
    except (OSError, json.JSONDecodeError) as exc:
        raise ErrorDatos(f'No se pudo leer {nombre}: {exc}') from exc

def guardar_datos(nombre, registros):
    DATOS.mkdir(parents=True, exist_ok=True)
    temporal = None
    try:
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=DATOS,
                                         suffix='.tmp', delete=False) as archivo:
            temporal = Path(archivo.name)
            json.dump(registros, archivo, indent=2, ensure_ascii=False)
            archivo.write('\n')
        os.replace(temporal, DATOS / nombre)
    except OSError as exc:
        raise ErrorDatos(f'No se pudo guardar {nombre}: {exc}') from exc
    finally:
        if temporal and temporal.exists():
            temporal.unlink()
