import json
from collections import defaultdict
import os

RUTA_JSON = os.path.join("JSON", "PREGUNTAS_TODAS.json")


def normalizar_texto(texto):
    """
    Normaliza el texto de la pregunta para comparar:
    - minúsculas
    - sin espacios duplicados
    """
    return " ".join(texto.lower().split())


def detectar_preguntas_repetidas():
    with open(RUTA_JSON, "r", encoding="utf-8") as f:
        preguntas = json.load(f)

    # Diccionario:
    # clave = texto normalizado de la pregunta
    # valor = lista de apariciones
    mapa_preguntas = defaultdict(list)

    for p in preguntas:
        clave = normalizar_texto(p["pregunta"])
        mapa_preguntas[clave].append({
            "origen": p["origen"],
            "numero": p["numero"]
        })

    repetidas = {
        texto: apariciones
        for texto, apariciones in mapa_preguntas.items()
        if len(apariciones) > 1
    }

    if not repetidas:
        print("✅ No se han encontrado preguntas repetidas.")
        return

    print("\n📌 PREGUNTAS REPETIDAS ENCONTRADAS\n")

    for i, (texto, apariciones) in enumerate(repetidas.items(), start=1):
        print(f"{i}. Pregunta:")
        print(f"   \"{texto}\"")
        print(f"   Veces que aparece: {len(apariciones)}")
        print("   Aparece en:")

        for ap in apariciones:
            print(f"     - {ap['origen']} (pregunta nº {ap['numero']})")

        print("-" * 60)

    print(f"\n✅ Total de preguntas repetidas: {len(repetidas)}")


if __name__ == "__main__":
    detectar_preguntas_repetidas()