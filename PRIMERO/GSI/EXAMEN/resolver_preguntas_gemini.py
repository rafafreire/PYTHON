import json
import os
import time
import re
import google.generativeai as genai
from google.api_core import exceptions

# --- CONFIGURACIÓN ---
API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("Falta la variable de entorno GEMINI_API_KEY o GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# Usamos el modelo que ya vimos que te funciona
MODELO_FUNCIONANDO = "models/gemini-2.5-flash-lite" 

def extraer_json_valido(texto):
    try:
        # Buscamos el bloque JSON por si la IA añade texto extra
        match = re.search(r'\{.*\}', texto, re.DOTALL)
        if match:
            return json.loads(match.group())
        return None
    except:
        return None

def procesar_examen():
    model = genai.GenerativeModel(MODELO_FUNCIONANDO)
    
    ruta_entrada = os.path.join('JSON', 'EXAMEN_GSI_2007.json')
    ruta_salida = os.path.join('RESPUESTAS', 'RESPUESTA_GEM_GSI_2007.json')

    with open(ruta_entrada, 'r', encoding='utf-8') as f:
        preguntas = json.load(f)

    print(f"Continuando proceso con {MODELO_FUNCIONANDO}...")

    for i, item in enumerate(preguntas):
        # Saltar si ya tiene respuesta correcta para no gastar cuota
        if item.get('respuesta_correcta') and item['respuesta_correcta'] not in ["Error", ""]:
            continue

        print(f"[{i+1}/{len(preguntas)}] Pregunta {item.get('numero')}...", end=" ", flush=True)
        
        prompt = (
            f"Pregunta GSI: {item['pregunta']}. "
            f"Opciones: a){item['opciones']['a']}, b){item['opciones']['b']}, c){item['opciones']['c']}, d){item['opciones']['d']}. "
            f"Responde solo JSON: {{\"letra\":\"letra_correcta\", \"explicacion\":\"breve_explicacion\"}}"
        )

        success = False
        intentos_fallidos = 0
        
        while not success:
            try:
                response = model.generate_content(prompt)
                datos = extraer_json_valido(response.text)
                if datos:
                    item['respuesta_correcta'] = datos.get('letra')
                    item['explicacion'] = datos.get('explicacion')
                    print(f"OK ({item['respuesta_correcta']})")
                    success = True
                else:
                    print("Error formato, reintentando...", end=" ")
                    intentos_fallidos += 1
                    if intentos_fallidos > 2: success = True # Saltar tras 3 fallos de formato

            except exceptions.ResourceExhausted:
                # Si nos bloquean mucho, aumentamos el tiempo de espera progresivamente
                espera = 70 + (intentos_fallidos * 10)
                print(f"\n[!] Saturación. Esperando {espera}s...", end=" ")
                time.sleep(espera)
                intentos_fallidos += 1
            except Exception as e:
                print(f"\n[!] Error: {e}. Reintentando...")
                time.sleep(10)

        # Guardar cada pregunta para no perder nada si lo cortas
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(preguntas, f, ensure_ascii=False, indent=4)
        
        # Pausa base más larga para evitar el baneo temporal
        time.sleep(12) 

if __name__ == "__main__":
    procesar_examen()