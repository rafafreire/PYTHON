import json
import re

def normalizar(valor):
    if valor == "null":
        return None
    return valor


def parsear_md(ruta_md):
    preguntas = {}

    with open(ruta_md, "r", encoding="utf-8") as f:
        texto = f.read()

    # Dividir por preguntas (** X.**)
    bloques = re.split(r"\*\*\s*(\d+)\.\*\*", texto)

    # bloques = [texto inicial, num1, texto1, num2, texto2, ...]
    for i in range(1, len(bloques), 2):
        numero = bloques[i]
        contenido = bloques[i + 1].strip()

        lineas = contenido.split("\n")

        enunciado = []
        opciones = {}

        for linea in lineas:
            linea = linea.strip()

            if re.match(r"^[a-d]\)", linea):
                letra = linea[0]
                opciones[letra] = linea[3:].strip()
            else:
                enunciado.append(linea)

        preguntas[numero] = {
            "enunciado": " ".join(enunciado),
            "opciones": opciones
        }

    return preguntas


def comparar():

    ruta_md = "ARCHIVOS/EXAMEN_GSI_2025.md"
    ruta_oficial = "RESPUESTAS/RESPUESTAS_GSI_2025_FIN.json"
    ruta_rafa = "RESPUESTAS/RESPUESTAS_RAFA_GSI_2025.json"
    salida = "RESPUESTAS/RESULTADO_COMPLETO_GSI_2025.json"

    preguntas = parsear_md(ruta_md)

    with open(ruta_oficial, "r", encoding="utf-8") as f:
        oficial = json.load(f)

    with open(ruta_rafa, "r", encoding="utf-8") as f:
        rafa = json.load(f)

    respuestas_oficial = oficial["plantilla_provisional"]["respuestas"]
    respuestas_rafa = rafa["respuestas_rafa"]["respuestas"]

    resultado_detallado = {}

    correctas = []
    incorrectas = []
    blanco = []

    print("\n📋 DETALLE PREGUNTA A PREGUNTA\n")

    for num in respuestas_oficial:

        pregunta = preguntas.get(num, {})

        correcta = normalizar(respuestas_oficial[num])
        usuario = normalizar(respuestas_rafa.get(num))

        # estado
        if usuario is None:
            estado = "blanco"
        elif usuario == correcta:
            estado = "correcta"
        else:
            estado = "incorrecta"

        # Mostrar
        print(f"Pregunta {num}: {usuario} / {correcta} → {estado}")

        resultado_detallado[num] = {
            "numero": int(num),
            "enunciado": pregunta.get("enunciado"),
            "opciones": pregunta.get("opciones"),
            "respuesta_usuario": usuario,
            "respuesta_correcta": correcta,
            "estado": estado
        }

        # Solo 1–100 cuentan
        if int(num) <= 100:
            if estado == "correcta":
                correctas.append(num)
            elif estado == "incorrecta":
                incorrectas.append(num)
            else:
                blanco.append(num)

    # nota
    nota = len(correctas) - (len(incorrectas) * (1/3))
    nota_interna = len(correctas) - (len(incorrectas) * (1/4))

    print("\n📊 RESULTADO FINAL")
    print(f"✅ Correctas: {len(correctas)}")
    print(f"❌ Incorrectas: {len(incorrectas)}")
    print(f"⚪ En blanco: {len(blanco)}")
    print(f"📝 Nota: {nota:.2f}")
    print(f"📝 Nota Interna: {nota_interna:.2f}")

    # guardar JSON
    with open(salida, "w", encoding="utf-8") as f:
        json.dump({
            "resumen": {
                "correctas": len(correctas),
                "incorrectas": len(incorrectas),
                "blanco": len(blanco),
                "nota": round(nota, 2),
                "nota_interna": round(nota_interna, 2)
            },
            "preguntas": resultado_detallado
        }, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Archivo generado: {salida}")


if __name__ == "__main__":
    comparar()