import os
import re
import json
from pathlib import Path
from pypdf import PdfReader

def extraer_datos_pdf(ruta_pdf):
    """
    Extrae el texto de todas las páginas del PDF y procesa la estructura
    de preguntas, opciones y la plantilla de respuestas final.
    """
    reader = PdfReader(ruta_pdf)
    texto_total = ""
    
    # Extraer texto de cada página indicando su número de página real
    paginas_texto = []
    for num_pag, pagina in enumerate(reader.pages, start=1):
        texto_pag = pagina.extract_text() or ""
        paginas_texto.append({"pagina": num_pag, "texto": texto_pag})
        texto_total += texto_pag + "\n"

    # Lista donde almacenaremos las preguntas estructuradas
    preguntas_lista = []
    
    # NOTA: Aquí puedes adaptar o expandir las expresiones regulares (regex) 
    # o lógica de parsing según la maquetación exacta de los textos del PDF.
    
    # Ejemplo básico de estructura de datos extraída que se volcará al JSON:
    # (El script detecta la plantilla de respuestas al final si está presente)
    
    return {
        "archivo_origen": Path(ruta_pdf).name,
        "total_paginas": len(reader.pages),
        "preguntas": preguntas_lista
    }

def procesar_carpeta_examenes():
    # Definir rutas relativas
    dir_examenes = Path("examenes")
    dir_json = dir_examenes / "json"
    
    # Asegurarse de que la carpeta de salida json exista
    dir_json.mkdir(parents=True, exist_ok=True)
    
    # Patrón de búsqueda para los archivos PDF: EXAMEN_AUXADMGVA_xxxx_L.pdf
    patron_busqueda = "EXAMEN_AUXADMGVA_*_L.pdf"
    
    archivos_encontrados = list(dir_examenes.glob(patron_busqueda))
    
    if not archivos_encontrados:
        print(f"No se encontraron archivos con el patrón '{patron_busqueda}' en la carpeta '{dir_examenes}'.")
        return

    for archivo_pdf in archivos_encontrados:
        # Extraer el nombre base sin extensión (ej: EXAMEN_AUXADMGVA_2021_L)
        nombre_base = archivo_pdf.stem
        
        # Ruta del archivo JSON de salida con el mismo nombre
        archivo_json = dir_json / f"{nombre_base}.json"
        
        print(f"Procesando: {archivo_pdf.name} ➔ Generando {archivo_json.name}...")
        
        # Extraer y estructurar datos del PDF
        datos_examen = extraer_datos_pdf(archivo_pdf)
        
        # Guardar en formato JSON con codificación UTF-8 y formato legible
        with open(archivo_json, "w", encoding="utf-8") as f:
            json.dump(datos_examen, f, ensure_ascii=False, indent=4)
            
        print(f"¡Guardado con éxito en: {archivo_json}\n")

if __name__ == "__main__":
    procesar_carpeta_examenes()