import json
import re
import html

def parse_exam_md(md_path, json_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Eliminar espacios HTML
    content = html.unescape(content)

    # Buscar bloques de preguntas **n.**
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
                letra = match.group(1)
                texto = match.group(2).strip()
                opciones[letra] = texto

        preguntas.append({
            "numero": int(numero),
            "pregunta": enunciado.strip(),
            "opciones": opciones,
            "respuesta_correcta": None
        })

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(preguntas, f, indent=4, ensure_ascii=False)


# Uso
if __name__ == "__main__":
    parse_exam_md(
        "EXAMEN_GSI_2014.md",
        "EXAMEN_GSI_2014.json"
    )