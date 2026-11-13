import os
import re
import json
import html

CARPETA = "ARCHIVOS"
CARPETA_JSON = "JSON"


def extraer_preguntas(contenido):
    preguntas = []
    contenido = html.unescape(contenido)

    patron_pregunta = re.compile(
        r"\*\*(\d+)\.\*\*\s*(.*?)\n\n(.*?)(?=\n\n\*\*\d+\.|\Z)",
        re.DOTALL
    )

    for numero, enunciado, bloque in patron_pregunta.findall(contenido):
        opciones = {}
        correcta = None
        explicacion = None
        leyendo_explicacion = False
        explicacion_lineas = []

        for linea in bloque.splitlines():
            linea = linea.strip()

            if not linea:
                continue

            # Inicio de explicación
            if linea.startswith("###"):
                leyendo_explicacion = True
                continue

            # Cortar explicación en separadores
            if linea.startswith("---"):
                break

            if leyendo_explicacion:
                explicacion_lineas.append(linea)
                continue

            # Respuesta correcta
            match_correcta = re.match(
                r"==\*\*([a-d])\)\s*(.*?)\*\*==",
                linea,
                re.IGNORECASE
            )
            if match_correcta:
                letra = match_correcta.group(1).lower()
                texto = match_correcta.group(2).strip()
                opciones[letra] = texto
                correcta = letra
                continue

            # Respuesta normal
            match_opcion = re.match(
                r"([a-d])\)\s+(.*)",
                linea,
                re.IGNORECASE
            )
            if match_opcion:
                letra = match_opcion.group(1).lower()
                texto = match_opcion.group(2).strip()
                opciones[letra] = texto

        if explicacion_lineas:
            explicacion = "\n".join(explicacion_lineas)

        if len(opciones) == 4:
            preguntas.append({
                "numero": int(numero),
                "pregunta": enunciado.strip(),
                "opciones": opciones,
                "respuesta_correcta": correcta,
                "explicacion": explicacion
            })

    return preguntas


def procesar_md(md_path, json_path):
    with open(md_path, "r", encoding="utf-8") as f:
        contenido = f.read()

    preguntas = extraer_preguntas(contenido)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(preguntas, f, indent=4, ensure_ascii=False)


def procesar_todos():
    for archivo in os.listdir(CARPETA):
        if archivo.lower().endswith(".md"):
            md_path = os.path.join(CARPETA, archivo)
            json_path = os.path.join(
                CARPETA_JSON,
                os.path.splitext(archivo)[0] + ".json"
            )

            print(f"✔ Procesando {archivo}")
            procesar_md(md_path, json_path)


if __name__ == "__main__":
    procesar_todos()
