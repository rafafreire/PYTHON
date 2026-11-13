## EXPORTAR JSON A EXCEL

import json
import pandas as pd
import os

CARPETA_JSON = "JSON"
ARCHIVO_JSON = "PREGUNTAS_TODAS.json"
ARCHIVO_EXCEL = "PREGUNTAS_TODAS.xlsx"


def json_a_excel():
    ruta_json = os.path.join(CARPETA_JSON, ARCHIVO_JSON)
    ruta_excel = os.path.join(CARPETA_JSON, ARCHIVO_EXCEL)

    with open(ruta_json, "r", encoding="utf-8") as f:
        preguntas = json.load(f)

    filas = []

    for p in preguntas:
        filas.append({
            "origen": p.get("origen"),
            "numero": p.get("numero"),
            "pregunta": p.get("pregunta"),
            "opcion_a": p.get("opciones", {}).get("a"),
            "opcion_b": p.get("opciones", {}).get("b"),
            "opcion_c": p.get("opciones", {}).get("c"),
            "opcion_d": p.get("opciones", {}).get("d"),
            "respuesta_correcta": p.get("respuesta_correcta"),
            "explicacion": p.get("explicacion")
        })

    df = pd.DataFrame(filas)

    # Guardar en Excel
    df.to_excel(ruta_excel, index=False, engine="openpyxl")

    print(f"✅ Excel generado correctamente: {ruta_excel}")
    print(f"✅ Total de preguntas exportadas: {len(df)}")


if __name__ == "__main__":
    json_a_excel()
