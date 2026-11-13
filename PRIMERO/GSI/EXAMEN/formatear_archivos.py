import os
import re

DIR_ENTRADA = "ARCHIVOS"
DIR_SALIDA = "SALIDA"

os.makedirs(DIR_SALIDA, exist_ok=True)

archivos_md = [f for f in os.listdir(DIR_ENTRADA) if f.lower().endswith(".md")]

print(f"📄 Archivos encontrados: {archivos_md}")

for archivo in archivos_md:
    print(f"\n📄 Archivo: {archivo}")
    if input("¿Deseas procesarlo? (s/n): ").strip().lower() != "s":
        print("⏭️ Omitido")
        continue

    with open(os.path.join(DIR_ENTRADA, archivo), encoding="utf-8") as f:
        texto = f.read()

    # Normalizar HTML
    texto = re.sub(r"&nbsp;+", " ", texto)

    lineas = [l.rstrip() for l in texto.splitlines()]

    titulo = ""
    preguntas = []
    pregunta = None

    for linea in lineas:
        if linea.startswith("EJERCICIO"):
            titulo = linea
            continue

        m = re.match(r"\*\*(\d+)\.\*\*\s*(.*)", linea)
        if m:
            if pregunta:
                preguntas.append(pregunta)
            pregunta = {
                "num": m.group(1),
                "enunciado": m.group(2),
                "opciones": {}
            }
            continue

        m = re.match(r"([a-d])\)\s*(.*)", linea, re.IGNORECASE)
        if m and pregunta:
            pregunta["opciones"][m.group(1).lower()] = m.group(2)

    if pregunta:
        preguntas.append(pregunta)

    # =====================
    # GENERAR SALIDA FINAL
    # =====================

    salida = []
    salida.append(titulo)
    salida.append("")

    for p in preguntas:
        salida.append(f"**{p['num']}.** {p['enunciado']}")
        salida.append("")

        for letra in ["a", "b", "c", "d"]:
            salida.append(f"{letra}) {p['opciones'].get(letra, '')}")

        salida.append("")
        salida.append("NOTA:")
        salida.append("")
        salida.append("")
        salida.append("")
        salida.append("")
        salida.append("")
        salida.append("")

    with open(os.path.join(DIR_SALIDA, archivo), "w", encoding="utf-8") as f:
        f.write("\n".join(salida))

    print(f"✅ Archivo creado en {DIR_SALIDA}/{archivo}")

print("\n🎉 Proceso finalizado")
