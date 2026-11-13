import json
import os
import time
import re
from groq import Groq

# 1. CONFIGURACIÓN - Volvemos al modelo rápido para evitar bloqueos por límite
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("Falta la variable de entorno GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)
MODELO_RAPIDO = "llama-3.1-8b-instant" 

def obtener_estructura_inicial():
    return {
        "BLOQUE I. Organización del Estado y Administración electrónica": {
            "B1.1 La Constitución Española de 1978": [], "B1.2 Las Cortes Generales y TC": [],
            "B1.3 El Gobierno y sus funciones": [], "B1.4 Transparencia y Agenda 2030": [],
            "B1.5 Políticas de igualdad y LGTBI": [], "B1.6 Sociedad de la información y eIDAS": [],
            "B1.7 Protección de datos y Derechos digitales": [], "B1.8 Leyes 39/2015, 40/2015 y EBEP": [],
            "B1.9 Administración Electrónica, ENS y ENI": [], "B1.10 Cooperación entre Administraciones": []
        },
        "BLOQUE II. Tecnología básica": {
            "B2.1 Tecnologías actuales de ordenadores": [], "B2.2 Conceptos y fundamentos de los sistemas operativos": [],
            "B2.3 Lenguajes y paradigmas de programación": [], "B2.4 Inteligencia de negocios y OLAP": [],
            "B2.5 BBDD Relacionales y SQL": [], "B2.6 Arquitectura Cliente-Servidor y Web Services": [],
            "B2.7 Contenedores y Microservicios": [], "B2.8 Modelo TCP/IP y OSI": [],
            "B2.9 XML, HTML y Scripting": [], "B2.10 Gestión de Riesgos": [],
            "B2.11 Auditoría Informática": [], "B2.12 CRM, IVR y Voice XML": [],
            "B2.13 Ciberseguridad e Informática Forense": [], "B2.14 Software Libre, Propietario y Licencias": [],
            "B2.15 Evaluación de alternativas y costes": [], "B2.16 Gestión Documental, SEO y Colaboración": []
        },
        "BLOQUE III. Desarrollo de sistemas": {
            "B3.1 Ciclo de vida de los sistemas": [], "B3.2 Gestión y planificación de proyectos": [],
            "B3.3 Requerimientos y Prototipos": [], "B3.4 Diseño de BBDD y Normalización": [],
            "B3.5 Algoritmos, Estructuras e IA": [], "B3.6 Construcción, CI/CD y DevOps": [],
            "B3.7 Pruebas de software": [], "B3.8 Instalación, Cambio y Mantenimiento": [],
            "B3.9 OO, UML y Patrones de diseño": [], "B3.10 Arquitectura Java EE / Jakarta EE": [],
            "B3.11 Plataforma .NET": [], "B3.12 Aplicaciones Web y Servicios Web": [],
            "B3.13 Calidad del software y métricas": [], "B3.14 Accesibilidad, UX y Usabilidad": [],
            "B3.15 Minería de datos, Big Data y NoSQL": []
        },
        "BLOQUE IV. Sistemas y comunicaciones": {
            "B4.1 Administración de SO y Software de base": [], "B4.2 Administración de SGBD": [],
            "B4.3 Mantenimiento y Backup": [], "B4.4 Configuración, Monitorización y Capacidad": [],
            "B4.5 Almacenamiento y Virtualización": [], "B4.6 CPD, Alta disponibilidad y Desastres": [],
            "B4.7 Medios de transmisión y Cableado": [], "B4.8 Redes locales y Seguridad": [],
            "B4.9 Administración de Redes y SNMP": [], "B4.10 WAN, WDM, MPLS y SD-WAN": [],
            "B4.11 Redes Inalámbricas y Seguridad": [], "B4.12 Seguridad en Redes, VPN y Criptografía": [],
            "B4.13 Internet e IoT": [], "B4.14 VoIP, NGN e IMS": [],
            "B4.15 Comunicaciones Móviles y MDM": [], "B4.16 Videoconferencia y Calidad de servicio": []
        }
    }

def clasificar_con_ia_rapida(pregunta_texto, lista_temas):
    # Prompt ultra-directo optimizado para modelos rápidos (sin rodeos)
    prompt = f"""Como profesor experto en la oposición GSI, clasifica la siguiente pregunta seleccionando estrictamente UN código de la lista.

LISTA DE TEMAS:
{lista_temas}

PREGUNTA:
"{pregunta_texto}"

Responde en este formato exacto: "Código: Bx.x" (Sustituye Bx.x por el código real). No añadas explicaciones.
"""
    for intento in range(3):
        try:
            res = client.chat.completions.create(
                model=MODELO_RAPIDO,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0, # Forzamos máxima precisión/coherencia
                max_tokens=15
            )
            txt = res.choices[0].message.content.strip()
            if txt:
                return txt
            print(f"   [!] Respuesta vacía de la API, reintentando en 3s...")
            time.sleep(3)
        except Exception as e:
            print(f"   [!] Error de API ({e}), esperando 5s...")
            time.sleep(5)
    return ""

def ejecutar():
    ruta_in = 'json/PREGUNTAS_TODAS.json'
    ruta_out = 'SALIDA/PREGUNTAS_TEMAS_GROQ.json'
    
    with open(ruta_in, 'r', encoding='utf-8') as f:
        preguntas = json.load(f)

    estructura = obtener_estructura_inicial()
    
    # Lista de temas simplificada para no saturar de tokens el prompt
    referencia_temas = ""
    for bloque, temas in estructura.items():
        referencia_temas += f"\n- {bloque}:\n"
        for t in temas.keys(): referencia_temas += f"  {t}\n"

    guardadas = 0
    print(f"--- INICIANDO PROCESAMIENTO OPTIMIZADO (1630 preguntas) ---")

    for i, p in enumerate(preguntas):
        print(f"\n[{i+1}/{len(preguntas)}] Analizando: {p['pregunta'][:50]}...")
        
        respuesta_ia = clasificar_con_ia_rapida(p['pregunta'], referencia_temas)
        print(f" > Respuesta IA: {respuesta_ia}")
        
        # Regex más permisivo: busca cualquier coincidencia de B1.1 a B4.16 en la respuesta
        match = re.search(r"B[1-4]\.\d+", respuesta_ia, re.IGNORECASE)
        
        if match:
            cod = match.group(0).upper()
            hallado = False
            for bloque, temas in estructura.items():
                for tema_full in temas.keys():
                    if tema_full.startswith(cod):
                        estructura[bloque][tema_full].append(p)
                        guardadas += 1
                        hallado = True
                        print(f" > ✅ CLASIFICADO EN: {cod}")
                        break
                if hallado: break
            if not hallado: print(f" > ❌ Código {cod} fuera de rango oficial.")
        else:
            print(f" > ❌ No se detectó código válido en la respuesta.")

        # Guardar cada 10 preguntas
        if (i+1) % 10 == 0:
            with open(ruta_out, 'w', encoding='utf-8') as f:
                json.dump(estructura, f, ensure_ascii=False, indent=4)
        
        # Pausa de seguridad para no quemar la API rate limit
        time.sleep(0.8)

    with open(ruta_out, 'w', encoding='utf-8') as f:
        json.dump(estructura, f, ensure_ascii=False, indent=4)
    print(f"\n--- PROCESO COMPLETADO: {guardadas}/{len(preguntas)} guardadas con éxito ---")

if __name__ == "__main__":
    ejecutar()