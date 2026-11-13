import json
import re
import html
import os

def parse_exam_md(md_path, json_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Eliminar entidades HTML como &nbsp;
    content = html.unescape(content)

    patron_pregunta = re.compile(
        r"\*\*(\d+)\.\*\*\s*(.*?)\n\n(.*?)(?=\n\n\*\*\d+\.|\Z)",
        re.DOTALL
    )

    preguntas = []

    for numero, enunciado, bloque_opciones in patron_pregunta.findall(content):
        opciones = {}

        for linea in bloque_opciones.splitlines():
            match = re.match(r"([a-d])\)\s+(.*)", linea.strip())
            if match:
                opciones[match.group(1)] = match.group(2)

        preguntas.append({
            "numero": int(numero),
            "pregunta": enunciado.strip(),
            "opciones": opciones,
            "respuesta_correcta": None
        })

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(preguntas, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    md_file = os.path.join("ARCHIVOS", "EXAMEN_GSI_2025.md")
    json_file = os.path.join("ARCHIVOS", "EXAMEN_GSI_2025.json")

    parse_exam_md(md_file, json_file)