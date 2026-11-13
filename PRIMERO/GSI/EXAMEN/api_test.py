import json
import os
import random

RUTA_JSON = os.path.join("JSON", "PREGUNTAS_TODAS.json")


def cargar_preguntas():
    with open(RUTA_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def mostrar_pregunta(pregunta):
    print("\n" + "=" * 70)
    print(f"Examen: {pregunta['origen']}  |  Pregunta nº {pregunta['numero']}\n")
    print(pregunta["pregunta"] + "\n")

    for letra, texto in pregunta["opciones"].items():
        print(f"{letra}) {texto}")

    print()


def pedir_respuesta():
    while True:
        r = input("Elige una opción (a/b/c/d): ").lower().strip()
        if r in ["a", "b", "c", "d"]:
            return r
        print("❗ Opción no válida. Inténtalo de nuevo.")


def mostrar_resultado(respuesta_usuario, pregunta):
    correcta = pregunta["respuesta_correcta"]

    if respuesta_usuario == correcta:
        print("\n✅ ¡Correcto!")
    else:
        print("\n❌ Incorrecto.")
        print(f"✅ La respuesta correcta era: {correcta})")

    if pregunta["explicacion"]:
        print("\n📘 Explicación:")
        print(pregunta["explicacion"])
    else:
        print("\nℹ No hay explicación disponible.")


def ejecutar_test():
    preguntas = cargar_preguntas()
    random.shuffle(preguntas)

    print("📚 TEST DE PREGUNTAS")
    print(f"Total de preguntas disponibles: {len(preguntas)}")

    for pregunta in preguntas:
        mostrar_pregunta(pregunta)
        r = pedir_respuesta()
        mostrar_resultado(r, pregunta)

        continuar = input("\n¿Continuar? (s/n): ").lower().strip()
        if continuar != "s":
            print("\n👋 Test finalizado.")
            break


if __name__ == "__main__":
    ejecutar_test()