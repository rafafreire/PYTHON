import json
import os
import random
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

JSON_PREGUNTAS = os.path.join("JSON", "PREGUNTAS_TODAS.json")
JSON_STATS = os.path.join("JSON", "estadisticas.json")

PENALIZACION_FALLO = 0.33


class AppTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Test de Exámenes")
        self.master.geometry("950x650")

        self.todas_preguntas = self.cargar_preguntas()
        self.menu_seleccion()

    # ---------- CARGA ----------
    def cargar_preguntas(self):
        with open(JSON_PREGUNTAS, "r", encoding="utf-8") as f:
            return json.load(f)

    def obtener_anios(self):
        return sorted({p["origen"].split("_")[-1].split(".")[0] for p in self.todas_preguntas})

    # ---------- SELECCIÓN ----------
    def menu_seleccion(self):
        self.frame_sel = tk.Frame(self.master, padx=20, pady=20)
        self.frame_sel.pack(fill="both", expand=True)

        tk.Label(self.frame_sel, text="Selecciona examen", font=("Arial", 16, "bold")).pack(pady=20)

        self.anio_var = tk.StringVar(value="TODOS")
        ttk.Combobox(
            self.frame_sel,
            textvariable=self.anio_var,
            values=["TODOS"] + self.obtener_anios(),
            state="readonly",
            width=20
        ).pack(pady=10)

        tk.Button(
            self.frame_sel,
            text="Comenzar",
            font=("Arial", 12),
            command=self.iniciar_test
        ).pack(pady=20)

    def iniciar_test(self):
        self.frame_sel.destroy()

        anio = self.anio_var.get()
        self.anio_seleccionado = anio

        if anio == "TODOS":
            self.preguntas = self.todas_preguntas[:]
        else:
            self.preguntas = [p for p in self.todas_preguntas if anio in p["origen"]]

        random.shuffle(self.preguntas)

        self.indice = 0
        self.aciertos = 0
        self.errores = 0
        self.puntuacion = 0.0

        self.interfaz_test()
        self.mostrar_pregunta()

    # ---------- INTERFAZ ----------
    def interfaz_test(self):
        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack(fill="both", expand=True)

        self.lbl_info = tk.Label(self.frame, font=("Arial", 11, "bold"))
        self.lbl_info.pack(anchor="w")

        self.barra = ttk.Progressbar(self.frame, length=900)
        self.barra.pack(pady=10)

        self.lbl_pregunta = tk.Label(
            self.frame, font=("Arial", 14), wraplength=900, justify="left"
        )
        self.lbl_pregunta.pack(pady=15)

        self.lbl_opciones = tk.Label(
            self.frame, font=("Arial", 12), justify="left", wraplength=900
        )
        self.lbl_opciones.pack(pady=10)

        # Botones A B C D (solo letra)
        frame_btn = tk.Frame(self.frame)
        frame_btn.pack(pady=15)

        for letra in ["a", "b", "c", "d"]:
            tk.Button(
                frame_btn,
                text=f"{letra.upper()})",
                font=("Arial", 14, "bold"),
                width=5,
                command=lambda l=letra: self.responder(l)
            ).pack(side="left", padx=10)

        # Navegación
        nav = tk.Frame(self.frame)
        nav.pack(pady=20)

        tk.Button(nav, text="⬅ Anterior", font=("Arial", 12), command=self.anterior).pack(side="left", padx=20)
        tk.Button(nav, text="Siguiente ➡", font=("Arial", 12), command=self.siguiente).pack(side="right", padx=20)

    # ---------- LÓGICA ----------
    def mostrar_pregunta(self):
        p = self.preguntas[self.indice]

        self.lbl_info.config(
            text=f"Examen: {self.anio_seleccionado} | "
                 f"Pregunta {self.indice + 1}/{len(self.preguntas)} | "
                 f"Aciertos: {self.aciertos}  Errores: {self.errores}"
        )

        self.barra["maximum"] = len(self.preguntas)
        self.barra["value"] = self.indice

        self.lbl_pregunta.config(text=p["pregunta"])

        opciones_texto = "\n".join(
            f"{l}) {p['opciones'][l]}" for l in ["a", "b", "c", "d"]
        )
        self.lbl_opciones.config(text=opciones_texto)

    def responder(self, letra):
        p = self.preguntas[self.indice]

        if letra == p["respuesta_correcta"]:
            self.aciertos += 1
            self.puntuacion += 1
            correcto = True
        else:
            self.errores += 1
            self.puntuacion -= PENALIZACION_FALLO
            correcto = False

        self.ventana_resultado(correcto, p)

    # ---------- RESULTADO ----------
    def ventana_resultado(self, correcto, p):
        v = tk.Toplevel(self.master)
        v.title("Resultado")
        v.geometry("700x400")
        v.grab_set()

        texto = "✅ Correcto" if correcto else f"❌ Incorrecto\nCorrecta: {p['respuesta_correcta']})"
        color = "green" if correcto else "red"

        tk.Label(v, text=texto, font=("Arial", 14, "bold"), fg=color).pack(pady=10)

        tk.Label(
            v,
            text=p["explicacion"] or "Sin explicación disponible",
            wraplength=650,
            justify="left",
            font=("Arial", 11)
        ).pack(pady=15)

        tk.Button(v, text="Cerrar", font=("Arial", 12), command=v.destroy).pack(pady=10)

    # ---------- NAVEGACIÓN ----------
    def siguiente(self):
        if self.indice < len(self.preguntas) - 1:
            self.indice += 1
            self.mostrar_pregunta()
        else:
            self.finalizar()

    def anterior(self):
        if self.indice > 0:
            self.indice -= 1
            self.mostrar_pregunta()

    # ---------- FINAL ----------
    def finalizar(self):
        self.guardar_stats()
        messagebox.showinfo(
            "Fin",
            f"Aciertos: {self.aciertos}\nErrores: {self.errores}\nPuntuación: {self.puntuacion:.2f}"
        )
        self.master.quit()

    def guardar_stats(self):
        stats = []
        if os.path.exists(JSON_STATS):
            with open(JSON_STATS, "r", encoding="utf-8") as f:
                stats = json.load(f)

        stats.append({
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "examen": self.anio_seleccionado,
            "aciertos": self.aciertos,
            "errores": self.errores,
            "puntuacion": round(self.puntuacion, 2)
        })

        with open(JSON_STATS, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    root = tk.Tk()
    AppTest(root)
    root.mainloop()