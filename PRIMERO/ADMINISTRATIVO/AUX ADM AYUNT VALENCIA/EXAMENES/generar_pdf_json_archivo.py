import json
import re
from pathlib import Path
from pypdf import PdfReader


def procesar_pdf_a_estructura_json(ruta_pdf: str, ruta_json_salida: str):
  """Procesa un archivo PDF de examen y genera un JSON con la estructura exacta:

  numero, tema, enunciado, options (a, b, c) y respuesta_correcta.
  """
  path_pdf = Path(ruta_pdf)
  if not path_pdf.exists():
    raise FileNotFoundError(
        f"No se ha encontrado el archivo '{ruta_pdf}'. Comprueba la ruta."
    )

  # Leer el contenido completo del PDF
  reader = PdfReader(path_pdf)
  texto_completo = ""
  for num_pag, pagina in enumerate(reader.pages, start=1):
    texto_extraido = pagina.extract_text()
    if texto_extraido:
      texto_completo += texto_extraido + "\n"

  # Expresión regular para capturar preguntas estructuradas
  # Ejemplo: 874. T30 ¿Qué significa... \n a) ... \n b) ... \n c) ...
  patron_pregunta = re.compile(
      r"(\d+)\.\s+([A-Za-z0-9]+)\s+(.+?)\s+a\)\s+([^\n]+)\s+b\)\s+([^\n]+)"
      r"\s+c\)\s+([^\n]+)",
      re.DOTALL,
  )

  coincidencias = patron_pregunta.findall(texto_completo)
  lista_preguntas = []

  for match in coincidencias:
    num_str, tema, enunciado, opt_a, opt_b, opt_c = match

    # Limpiar saltos de línea y espacios sobrantes en el enunciado
    enunciado_limpio = " ".join(enunciado.split())

    pregunta_item = {
        "numero": int(num_str),
        "tema": tema.strip(),
        "enunciado": enunciado_limpio,
        "options": {
            "a": opt_a.strip(),
            "b": opt_b.strip(),
            "c": opt_c.strip(),
        },
        "respuesta_correcta": (
            "B"
        ),  # Puedes ajustarlo según tu plantilla de soluciones
    }
    lista_preguntas.append(pregunta_item)

  # Objeto JSON contenedor
  resultado_final = {
      "titulo": path_pdf.stem,
      "total_preguntas": len(lista_preguntas),
      "preguntas": lista_preguntas,
  }

  # Guardar el archivo JSON resultante
  path_json = Path(ruta_json_salida)
  with open(path_json, "w", encoding="utf-8") as f:
    json.dump(resultado_final, f, ensure_ascii=False, indent=4)

  print(
      f"¡Listo! Se han procesado {len(lista_preguntas)} preguntas y se han"
      f" guardado en: {path_json.resolve()}"
  )


# --- Ejecución interactiva cambiando el nombre del archivo ---
if __name__ == "__main__":
  # Introduce aquí el nombre exacto de tu archivo PDF o la ruta donde lo tengas
  nombre_archivo_pdf = input(
      "Introduce el nombre o ruta del archivo PDF (ej:"
      " EXAMENES_TAE_INFORMATICO.pdf): "
  ).strip()

  if not nombre_archivo_pdf:
    nombre_archivo_pdf = "EXAMENES TAE INFORMATICO.pdf"  # Valor por defecto

  nombre_archivo_json = (
      Path(nombre_archivo_pdf).stem + "_estructurado.json"
  )

  try:
    procesar_pdf_a_estructura_json(nombre_archivo_pdf, nombre_archivo_json)
  except Exception as e:
    print(f"Ha ocurrido un error: {e}")