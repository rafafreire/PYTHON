import os
import json
from pathlib import Path

def crear_archivo_json():
    # Definir rutas relativas
    dir_salida = Path("examenes/json")
    
    # Crear la carpeta de destino si no existe
    dir_salida.mkdir(parents=True, exist_ok=True)
    
    # Ruta completa del archivo JSON de salida
    ruta_json = dir_salida / "examen_auxiliar_generalitat_157_21.json"
    
    # Datos estructurados del examen (preguntas, opciones y respuestas correctas)
    datos_examen = [
        {
            "numero": 1,
            "pregunta": "De conformidad con lo dispuesto en el artículo 13 de la Ley 39/2015, de 1 de octubre, del procedimiento administrativo común de las administraciones públicas, donde se recogen los derechos de las personas en sus relaciones con las Administraciones Públicas, señale cuál de los siguientes derechos es incorrecto:",
            "opciones": {
                "A": "A comunicarse con las Administraciones Públicas a través de un Punto de Acceso General electrónico de la Administración.",
                "B": "A ser asistidos en el uso de medios electrónicos en sus relaciones con las Administraciones Públicas.",
                "C": "A no presentar datos y documentos no exigidos por las normas aplicables al procedimiento de que se trate, que ya se encuentren en poder de las Administraciones Públicas o que hayan sido elaborados por éstas.",
                "D": "A la protección de datos de carácter personal, y en particular a la seguridad y confidencialidad de los datos que figuren en los ficheros, sistemas y aplicaciones de las Administraciones Públicas."
            },
            "respuesta_correcta": "C",
            "pagina": 112
        },
        {
            "numero": 2,
            "pregunta": "De conformidad con lo dispuesto en la Ley 39/2015, de 1 de octubre, del procedimiento administrativo común de las administraciones públicas, señale cuál de los siguientes enunciados es correcto:",
            "opciones": {
                "A": "Los plazos expresados por horas se contarán de hora en hora y de minuto en minuto desde la hora y minuto en que tenga lugar la notificación o publicación del acto de que se trate y no podrán tener una duración inferior a veinticuatro horas, en cuyo caso se expresarán en días.",
                "B": "Los plazos expresados en días se contarán a partir del día siguiente a aquel en que tenga lugar la notificación o publicación del acto de que se trate, o desde aquel en que se produzca la estimación o la desestimación por silencio administrativo.",
                "C": "El plazo concluirá el mismo día en que se produjo la notificación, publicación o silencio administrativo en el mes o el año de vencimiento. Si en el mes de vencimiento no hubiera día equivalente a aquel en que comienza el cómputo, se entenderá que el plazo expira el primer día del mes siguiente.",
                "D": "Siempre que por Ley o en el Derecho de la Unión Europea no se exprese otro cómputo, cuando los plazos se señalen por días, se entiende que éstos son hábiles, excluyéndose del cómputo los sábados, los domingos y los declarados festivos."
            },
            "respuesta_correcta": "D",
            "pagina": 112
        },
        {
            "numero": 3,
            "pregunta": "De conformidad con lo dispuesto en la Ley 39/2015, de 1 de octubre, del procedimiento administrativo común de las administraciones públicas, señale cuál de los siguientes enunciados es incorrecto:",
            "opciones": {
                "A": "La Administración, salvo precepto en contrario, podrá conceder de oficio o a petición del órgano instructor una ampliación de los plazos establecidos, que no exceda de la mitad de los mismos, si las circunstancias lo aconsejan y con ello no se perjudican derechos de tercero. El acuerdo de ampliación deberá ser notificado a los interesados.",
                "B": "La ampliación de los plazos por el tiempo máximo permitido se aplicará en todo caso a los procedimientos tramitados por las misiones diplomáticas y oficinas consulares, así como a aquellos que, sustanciándose en el interior, exijan cumplimentar algún trámite en el extranjero o en los que intervengan interesados residentes fuera de España.",
                "C": "Tanto la petición de los interesados como la decisión sobre la ampliación deberán producirse, en todo caso, antes del vencimiento del plazo de que se trate. En ningún caso podrá ser objeto de ampliación un plazo ya vencido.",
                "D": "Los acuerdos sobre ampliación de plazos o sobre su denegación no serán susceptibles de recurso, sin perjuicio del procedente contra la resolución que ponga fin al procedimiento."
            },
            "respuesta_correcta": "A",
            "pagina": 113
        }
        # Nota: Puedes añadir el resto de preguntas completando esta lista con la misma estructura.
    ]

    # Escribir los datos en el archivo JSON con formato legible (indentado)
    with open(ruta_json, "w", encoding="utf-8") as archivo:
        json.dump(datos_examen, archivo, ensure_ascii=False, indent=4)
        
    print(f"¡Archivo JSON generado con éxito en: {ruta_json.resolve()}!")

if __name__ == "__main__":
    crear_archivo_json()