import json
import os
import re
import pandas as pd

def generar_informe_solo_discrepancias():
    ruta_json = "JSON"
    ruta_respuestas = "RESPUESTAS"
    
    if not os.path.exists(ruta_respuestas):
        print(f"❌ No existe la carpeta: {ruta_respuestas}")
        return

    # Buscar todos los archivos de respuestas en la carpeta
    archivos_plantilla = [f for f in os.listdir(ruta_respuestas) if f.startswith("RESPUESTAS_GSI_") and f.endswith(".json")]

    if not archivos_plantilla:
        print("No se encontraron archivos de respuestas para comparar.")
        return

    for archivo in archivos_plantilla:
        match = re.search(r"RESPUESTAS_GSI_(\d{4})", archivo)
        if not match: continue
        
        anio = match.group(1)
        f_examen = os.path.join(ruta_json, f"EXAMEN_GSI_{anio}.json")
        f_plantilla = os.path.join(ruta_respuestas, archivo)

        if not os.path.exists(f_examen):
            continue

        try:
            with open(f_examen, 'r', encoding='utf-8') as f:
                examen_data = json.load(f)
            with open(f_plantilla, 'r', encoding='utf-8') as f:
                plantilla_data = json.load(f)

            # Detectar estructura de plantilla (2022 vs 2024)
            if "plantilla_definitiva" in plantilla_data:
                oficiales = plantilla_data["plantilla_definitiva"].get("respuestas", {})
            else:
                oficiales = plantilla_data.get("respuestas", {})

            solo_errores = []

            for item in examen_data:
                num = str(item['numero'])
                resp_examen = str(item.get('respuesta_correcta', '')).lower().strip()
                resp_oficial_raw = str(oficiales.get(num, "")).lower().strip()

                # Ignorar preguntas anuladas
                if "anulada" in resp_oficial_raw:
                    continue

                # Limpiar letra oficial (quitar "(MODIFICADA)", etc.)
                resp_oficial_letra = resp_oficial_raw.split(" ")[0]

                # COMPARACIÓN: Solo si NO coinciden
                if resp_examen != resp_oficial_letra:
                    opc = item.get('opciones', {})
                    solo_errores.append({
                        "Año": anio,
                        "Pregunta Nº": num,
                        "Enunciado": item.get('pregunta', ''),
                        "A": opc.get('a', ''),
                        "B": opc.get('b', ''),
                        "C": opc.get('c', ''),
                        "D": opc.get('d', ''),
                        "Tu Respuesta (JSON)": resp_examen.upper(),
                        "Respuesta Correcta (Plantilla)": resp_oficial_letra.upper()
                    })

            # Generar archivos solo si hay discrepancias encontradas
            if solo_errores:
                df = pd.DataFrame(solo_errores)
                
                # Guardar Excel
                ruta_xlsx = os.path.join(ruta_respuestas, f"DISCREPANCIAS_GSI_{anio}.xlsx")
                df.to_excel(ruta_xlsx, index=False)
                
                # Guardar JSON para inspección técnica
                ruta_json_err = os.path.join(ruta_respuestas, f"DISCREPANCIAS_GSI_{anio}.json")
                with open(ruta_json_err, 'w', encoding='utf-8') as f:
                    json.dump(solo_errores, f, indent=4, ensure_ascii=False)

                print(f"✅ Año {anio}: Se han encontrado y guardado {len(solo_errores)} errores en la carpeta RESPUESTAS.")
            else:
                print(f"✨ Año {anio}: Los datos coinciden al 100%. No se ha generado informe de errores.")

        except Exception as e:
            print(f"💥 Error procesando el año {anio}: {e}")

if __name__ == "__main__":
    generar_informe_solo_discrepancias()