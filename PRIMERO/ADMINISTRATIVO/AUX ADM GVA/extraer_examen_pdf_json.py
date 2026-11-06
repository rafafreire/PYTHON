import json
import os
import re
from pypdf import PdfReader


def procesar_exámenes():
  # Directorios de entrada y salida
  dir_entrada = "examenes"
  dir_salida = os.path.join(dir_entrada, "json")

  # Crear la carpeta de salida si no existe
  os.makedirs(dir_salida, exist_ok=True)

  # Verificar si la carpeta de exámenes existe
  if not os.path.exists(dir_entrada):
    print(
        f"La carpeta '{dir_entrada}' no existe. Por favor, créala y coloca los"
        " archivos PDF dentro."
    )
    return

  # Obtener la lista de todos los archivos PDF
  archivos_pdf = [
      f for f in os.listdir(dir_entrada) if f.lower().endswith(".pdf")
  ]

  if not archivos_pdf:
    print(f"No se encontraron archivos PDF en la carpeta '{dir_entrada}'.")
    return

  print(
      f"Se encontraron {len(archivos_pdf)} archivos PDF para procesar.\n"
      + "-" * 50
  )

  for pdf_file in archivos_pdf:
    ruta_pdf = os.path.join(dir_entrada, pdf_file)
    nombre_base = os.path.splitext(pdf_file)[0]
    ruta_json = os.path.join(dir_salida, f"{nombre_base}.json")

    print(f"Procesando: {pdf_file} ...")

    # 1. Leer el PDF completo
    reader = PdfReader(ruta_pdf)
    texto_completo = ""
    for pagina in reader.pages:
      texto_pagina = pagina.extract_text()
      if texto_pagina:
        texto_completo += texto_pagina + "\n"

    # 2. Extraer plantilla de respuestas oficiales del final del documento
    plantilla_respuestas = {}
    coincidencias_respuestas = re.findall(
        r"(\d+)\s*\|\s*([A-Da-d])", texto_completo
    )
    for num, resp in coincidencias_respuestas:
      plantilla_respuestas[int(num)] = resp.upper()

    # 3. Separar el cuerpo del examen de la plantilla de respuestas
    if "PLANTILLA DE RESPUESTAS" in texto_completo:
      cuerpo_examen = texto_completo.split("PLANTILLA DE RESPUESTAS")[0]
    else:
      cuerpo_examen = texto_completo

    # 4. Dividir por bloques de preguntas (ej: "1. ", "2. ")
    bloques_preguntas = re.split(r"\n(?=\d{1,3}\.\s)", cuerpo_examen)
    preguntas_lista = []

    for bloque in bloques_preguntas:
      bloque = bloque.strip()
      if not bloque:
        continue

      # Identificar el número de pregunta y el texto
      match_pregunta = re.match(r"^(\d{1,3})\.\s+(.*)", bloque, re.DOTALL)
      if not match_pregunta:
        continue

      num_pregunta = int(match_pregunta.group(1))
      texto_y_opciones = match_pregunta.group(2)

      # Separar enunciado de las opciones A), B), C), D)
      partes_opciones = re.split(r"\n\s*([A-Da-d])[\)\.]\s+", texto_y_opciones)

      enunciado = partes_opciones[0].replace("\n", " ").strip()
      enunciado = re.sub(r"\s+", " ", enunciado)

      opciones = {}
      for i in range(1, len(partes_opciones) - 1, 2):
        letra = partes_opciones[i].upper()
        texto_opcion = partes_opciones[i + 1].replace("\n", " ").strip()
        texto_opcion = re.sub(r"\s+", " ", texto_opcion)
        opciones[letra] = texto_opcion

      # Asignar la respuesta correcta desde la plantilla o marcar como Anulada
      respuesta_correcta = plantilla_respuestas.get(num_pregunta, "Anulada")

      # Estructura del diccionario por pregunta
      pregunta_dict = {
          "numero": num_pregunta,
          "pregunta": enunciado,
          "opciones": opciones,
          "respuesta_correcta": respuesta_correcta,
          "explicacion": None,
      }
      preguntas_lista.append(pregunta_dict)

    # Ordenar por número de pregunta para mantener orden secuencial
    preguntas_lista = sorted(preguntas_lista, key=lambda x: x["numero"])

    # 5. Guardar el archivo JSON resultante
    with open(ruta_json, "w", encoding="utf-8") as f:
      json.dump(preguntas_lista, f, ensure_ascii=False, indent=4)

    print(
        f"   -> Generado con éxito: {ruta_json} ({len(preguntas_lista)}"
        " preguntas procesadas)\n"
    )

  print("-" * 50)
  print("¡Todos los exámenes han sido procesados y convertidos a JSON!")


if __name__ == "__main__":
  procesar_exámenes()