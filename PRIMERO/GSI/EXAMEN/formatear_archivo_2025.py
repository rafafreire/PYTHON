import re

def formatear_preguntas(texto):
    """
    Convierte números de preguntas tipo '1.' en '** 1.**'
    solo cuando están al inicio de línea.
    """
    patron = r'(^|\n)(\d+)\.'

    def reemplazo(match):
        inicio = match.group(1)
        numero = match.group(2)
        return f"{inicio}** {numero}.**"

    return re.sub(patron, reemplazo, texto)


def main():
    input_path = "ARCHIVOS/EXAMEN_GSI_2025.md"
    output_path = "ARCHIVOS/EXAMEN_GSI_2025_formateado.md"

    # Leer archivo
    with open(input_path, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Procesar
    resultado = formatear_preguntas(contenido)

    # Guardar resultado
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(resultado)

    print(f"✅ Archivo generado correctamente en: {output_path}")


if __name__ == "__main__":
    main()
    