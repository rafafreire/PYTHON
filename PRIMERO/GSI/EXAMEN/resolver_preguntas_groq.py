import json
import os
import time
import re
from groq import Groq

# --- CONFIGURACIÓN ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("Falta la variable de entorno GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)
MODELO_GROQ = "llama-3.3-70b-versatile"

def extraer_json_valido(texto):
    try:
        match = re.search(r'\{.*\}', texto, re.DOTALL)
        if match:
            return json.loads(match.group())
        return None
    except:
        return None

def procesar_un_archivo(ruta_entrada, ruta_salida, modo_completo):
    """
    Procesa un archivo JSON. 
    Si modo_completo es False, solo procesa los que tienen respuesta vacía o "Error".
    """
    try:
        # Cargar datos base
        if os.path.exists(ruta_salida):
            with open(ruta_salida, 'r', encoding='utf-8') as f:
                preguntas = json.load(f)
        else:
            with open(ruta_entrada, 'r', encoding='utf-8') as f:
                preguntas = json.load(f)
        
        total = len(preguntas)
        print(f"\n>>> TRABAJANDO EN: {os.path.basename(ruta_entrada)}")

        for i, item in enumerate(preguntas):
            # Lógica de salto según la elección del usuario
            tiene_respuesta = item.get('respuesta_correcta') and item['respuesta_correcta'] not in ["Error", "", None]
            
            if not modo_completo and tiene_respuesta:
                continue

            print(f"    [{i+1}/{total}] Pregunta {item.get('numero')}...", end=" ", flush=True)
            
            prompt = f"""Actúa como preparador GSI. Pregunta: {item['pregunta']}
            Opciones: a) {item['opciones']['a']}, b) {item['opciones']['b']}, c) {item['opciones']['c']}, d) {item['opciones']['d']}
            Responde ÚNICAMENTE en JSON: {{"letra": "x", "explicacion": "..."}}"""

            try:
                completion = client.chat.completions.create(
                    model=MODELO_GROQ,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.1,
                    response_format={"type": "json_object"}
                )
                datos = extraer_json_valido(completion.choices[0].message.content)
                if datos:
                    item['respuesta_correcta'] = datos.get('letra')
                    item['explicacion'] = datos.get('explicacion')
                    print(f"OK ({item['respuesta_correcta']})")
                
                with open(ruta_salida, 'w', encoding='utf-8') as f:
                    json.dump(preguntas, f, ensure_ascii=False, indent=4)
                
                time.sleep(1.2)

            except Exception as e:
                if "429" in str(e):
                    print("\n[!] Límite de cuota. Esperando 20s...")
                    time.sleep(20)
                else:
                    print(f"Error: {e}")
                    break

    except Exception as e:
        print(f"Error en el archivo: {e}")

def main():
    carpeta_input = 'JSON'
    carpeta_output = 'RESPUESTAS'
    
    if not os.path.exists(carpeta_output):
        os.makedirs(carpeta_output)

    # 1. Detectar archivos
    archivos_dict = {}
    for f in os.listdir(carpeta_input):
        if f.startswith('EXAMEN_GSI_') and f.endswith('.json'):
            match = re.search(r'\d{4}', f)
            if match:
                año = match.group()
                archivos_dict[año] = f

    if not archivos_dict:
        print(f"No hay archivos en /{carpeta_input}")
        return

    # 2. Selección de Años
    años_disponibles = sorted(archivos_dict.keys())
    print("\n" + "="*40)
    print("      GESTOR DE EXÁMENES GSI (GROQ)")
    print("="*40)
    print(f"Años disponibles: {', '.join(años_disponibles)}")
    
    entrada_años = input("\n1. ¿Qué años procesar? (Ej: 2008, 2011 o ENTER para todos): ").strip()

    if entrada_años == "":
        años_a_procesar = años_disponibles
    else:
        seleccion = [a.strip() for a in entrada_años.split(',')]
        años_a_procesar = [a for a in seleccion if a in archivos_dict]

    if not años_a_procesar:
        print("Selección no válida.")
        return

    # 3. Selección de Modo de Ejecución
    print("\n2. ¿Qué quieres hacer con las preguntas ya contestadas?")
    print("   [1] Omitirlas (solo procesar las nuevas o con errores)")
    print("   [2] Sobrescribir TODO (volver a procesar el examen completo)")
    
    modo_input = input("\nElige una opción (1 o 2, por defecto 1): ").strip()
    modo_completo = (modo_input == "2")

    # 4. Ejecución
    print(f"\n--- Iniciando: {'MODO COMPLETO' if modo_completo else 'MODO PENDIENTES'} ---")

    for año in años_a_procesar:
        archivo = archivos_dict[año]
        ruta_in = os.path.join(carpeta_input, archivo)
        ruta_out = os.path.join(carpeta_output, f"RESPUESTA_GROQ_GSI_{año}.json")
        procesar_un_archivo(ruta_in, ruta_out, modo_completo)

    print("\n--- ¡PROCESO COMPLETADO EXITOSAMENTE! ---")

if __name__ == "__main__":
    main()