import json
import re
from pathlib import Path
from pypdf import PdfReader


def convertir_examen_a_json(ruta_pdf: str, ruta_salida_json: str):
  """Extrae las preguntas de un PDF de exámenes y las formatea

  con la estructura exacta requerida (numero, tema, enunciado, options,
  respuesta_correcta).
  """
  path_pdf = Path(ruta_pdf)
  if not path_pdf.exists():
    raise FileNotFoundError(f"No se encuentra el archivo PDF en: {ruta_pdf}")

  reader = PdfReader(path_pdf)
  texto_completo = ""
  for pagina in reader.pages:
    texto_completo += (pagina.extract_text() or "") + "\n"

  # Expresión regular para capturar preguntas del tipo:
  # 1. T1 ¿Enunciado?
  # a) Opc 1
  # b) Opc 2
  # c) Opc 3
  patron_pregunta = re.compile(
      r"(\d+)\.\s+([A-Za-z0-9]+)\s+(adores?|[\¿\?].+?)"
      r"\s+a\)\s+([^\n]+)"
      r"\s+b\)\s+([^\n]+)"
      r"\s+c\)\s+([^\n]+)",
      re.DOTALL,
  )

  # Patrón más general por si el enunciado no empieza siempre por ¿
  patron_general = re.compile(
      r"(\d+)\.\s+([A-Za-z0-9]+)\s+(.+?)\s+a\)\s+([^\n]+)\s+b\)\s+([^\n]+)"
      r"\s+c\)\s+([^\n]+)",
      re.DOTALL,
  )

  # Buscamos todas las coincidencias
  coincidencias = patron_general.findall(texto_completo)
  preguntas_lista = []

  for match in coincidencias:
    num_str, tema, enunciado, opt_a, opt_b, opt_c = match

    # Limpieza básica de espacios y saltos de línea
    enunciado_limpio = " ".join(enunciado.split())

    pregunta_dict = {
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
        ),
        "explicación": (
                    "**"
                ),    # Valor por defecto o asignado según plantilla de respuestas
    }
    preguntas_lista.append(pregunta_dict)

  # Estructura contenedor final
  estructura_final = {
      "titulo": "Examen TAE Informático",
      "total_preguntas": len(preguntas_lista),
      "preguntas": preguntas_lista,
  }

  # Guardar en archivo JSON
  path_json = Path(ruta_salida_json)
  with open(path_json, "w", encoding="utf-8") as f:
    json.dump(estructura_final, f, ensure_ascii=False, indent=4)

  print(
      f"¡Estructura generada con éxito! Archivo guardado en: {path_json.resolve()}"
  )
  print(f"Total de preguntas procesadas: {len(preguntas_lista)}")


# --- Ejecución del script ---
if __name__ == "__main__":
  archivo_pdf = "EXAMENES_TAE_INFORMATICO.pdf"
  archivo_json_salida = "examen_tae_informatico_corregido.json"

  try:
    convertir_examen_a_json(archivo_pdf, archivo_json_salida)
  except Exception as e:
    print(f"Ocurrió un error durante el procesamiento: {e}")