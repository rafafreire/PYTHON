import os
import re
import json
import html

CARPETA_MD = "ARCHIVOS"
CARPETA_JSON = "JSON"
SALIDA = "PREGUNTAS_TODAS.json"


def extraer_preguntas(contenido, nombre_archivo):
    contenido = html.unescape(contenido)
    preguntas = []

    patron_pregunta = re.compile(
        r"\*\*(\d+)\.\*\*\s*(.*?)\n\n(.*?)(?=\n\n\*\*\d+\.|\Z)",
        re.DOTALL
    )

    for numero, enunciado, bloque in patron_pregunta.findall(contenido):
        opciones = {}
        correcta = None
        explicacion_lineas = []
        leyendo_explicacion = False

        for linea in bloque.splitlines():
            linea = linea.strip()
            if not linea:
                continue

            # Inicio de la explicación
            if linea.startswith("###"):
                leyendo_explicacion = True
                continue

            if linea.startswith("---"):
                break

            if leyendo_explicacion:
                explicacion_lineas.append(linea)
                continue

            # Respuesta correcta
            m_correcta = re.match(r"==\*\*([a-d])\)\s*(.*?)\*\*==", linea, re.I)
            if m_correcta:
                letra = m_correcta.group(1).lower()
                opciones[letra] = m_correcta.group(2).strip()
                correcta = letra
                continue

            # Respuestas normales
            m_opcion = re.match(r"([a-d])\)\s+(.*)", linea, re.I)
            if m_opcion:
                opciones[m_opcion.group(1).lower()] = m_opcion.group(2).strip()

        preguntas.append({
            "origen": nombre_archivo,
            "numero": int(numero),
            "pregunta": enunciado.strip(),
            "opciones": opciones,
            "respuesta_correcta": correcta,
            "explicacion": "\n".join(explicacion_lineas) if explicacion_lineas else None
        })

    return preguntas


def juntar_todos_los_md():
    todas = []

    # Crear carpeta JSON si no existe
    os.makedirs(CARPETA_JSON, exist_ok=True)

    for archivo in os.listdir(CARPETA_MD):
        if archivo.lower().endswith(".md"):
            print(f"\nProcesando archivo: {archivo}")
            ruta_md = os.path.join(CARPETA_MD, archivo)

            try:
                with open(ruta_md, "r", encoding="utf-8") as f:
                    contenido = f.read()

                preguntas = extraer_preguntas(contenido, archivo)
                todas.extend(preguntas)
                print(f"✔ OK: {len(preguntas)} preguntas extraídas")

            except Exception as e:
                print(f"✖ ERROR procesando {archivo}")
                print(f"    Detalle: {e}")

    ruta_salida = os.path.join(CARPETA_JSON, SALIDA)
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(todas, f, indent=4, ensure_ascii=False)

    print("\n" + "=" * 50)
    print(f"✅ Archivo JSON generado correctamente en: {ruta_salida}")
    print(f"✅ Total de preguntas: {len(todas)}")


if __name__ == "__main__":
    juntar_todos_los_md()
