import tkinter as tk
from tkinter import messagebox

def tutorial_en_frame(contenedor, on_finish=None):
    """Crea el tutorial dentro de un frame existente en lugar de una nueva ventana."""
    
    # === Datos del tutorial ===
    preguntas_tutorial = {
        1: {
            "pregunta": "¿Cuál de las siguientes etiquetas se usa para crear un enlace?",
            "opciones": {"a": "<a>", "b": "<link>", "c": "<href>"},
            "respuesta": "a",
        },
        2: {
            "pregunta": "¿Qué propiedad de CSS cambia el color del texto?",
            "opciones": {"a": "background-color", "b": "font-color", "c": "color"},
            "respuesta": "c",
        },
        3: {
            "pregunta": "¿Cómo se muestra un mensaje emergente (alerta) al usuario?",
            "opciones": {"a": 'show("Hola")', "b": 'prompt("Hola")', "c": 'alert("Hola")'},
            "respuesta": "c",
        },
        4: {
            "pregunta": "¿Cuál atributo HTML se utiliza para hacer obligatorio un campo de formulario?",
            "opciones": {"a": "required", "b": "mandatory", "c": "obligatory"},
            "respuesta": "a",
        },
        5: {
            "pregunta": "¿Qué hace la propiedad display: flex?",
            "opciones": {
                "a": "Oculta un elemento",
                "b": "Lo convierte en contenedor flexible",
                "c": "Lo posiciona en pantalla completa",
            },
            "respuesta": "b",
        },
        6: {
            "pregunta": "¿Cuál es el método correcto para seleccionar un elemento por ID en el DOM?",
            "opciones": {
                "a": "getElementByClass()",
                "b": 'querySelectorAll("#id")',
                "c": 'getElementById("id")',
            },
            "respuesta": "c",
        },
        7: {
            "pregunta": "¿Cuál es el propósito de las etiquetas semánticas como <article>, <section>, <aside>?",
            "opciones": {
                "a": "Estilizar automáticamente",
                "b": "Mejorar estructura y accesibilidad",
                "c": "Aumentar tamaño del texto",
            },
            "respuesta": "b",
        },
        8: {
            "pregunta": "¿Cuál es el resultado de aplicar position: absolute dentro de un contenedor con position: relative?",
            "opciones": {
                "a": "Se alinea con el body",
                "b": "Desaparece del flujo",
                "c": "Se posiciona relativo al contenedor",
            },
            "respuesta": "c",
        },
        9: {
            "pregunta": "¿Qué es una promesa (Promise) en JavaScript?",
            "opciones": {
                "a": "Se ejecuta inmediatamente",
                "b": "Encapsula operación asíncrona",
                "c": "Un bucle",
            },
            "respuesta": "b",
        },
        10: {
            "pregunta": '¿Qué hace este código?\n'
                        'document.querySelector("button").addEventListener("click", () => {\n'
                        '  alert("¡Hola!");\n'
                        '});',
            "opciones": {
                "a": "Agrega un botón",
                "b": "Cambia el color del botón",
                "c": "Muestra una alerta al hacer clic",
            },
            "respuesta": "c",
        },
    }

    # Limpiar el contenedor
    for widget in contenedor.winfo_children():
        widget.destroy()

    frame = tk.Frame(contenedor, bg="#0d1117")
    frame.pack(expand=True, fill="both", padx=50, pady=30)

    lbl_titulo = tk.Label(
        frame, text="🧠 Tutorial Interactivo", font=("Arial", 28, "bold"), fg="#58a6ff", bg="#0d1117"
    )
    lbl_titulo.pack(pady=20)

    lbl_pregunta = tk.Label(
        frame, text="", font=("Arial", 20, "bold"), fg="white", 
        bg="#0d1117", wraplength=1000, justify="left"
    )
    lbl_pregunta.pack(pady=30)

    # ====== NUEVO: Mensaje instructivo permanente ======
    lbl_instruccion = tk.Label(
        frame,
        text="👉 Seleccioná una de las opciones a continuación:",
        font=("Arial", 16, "bold"),
        fg="#ffa657",
        bg="#1a1a1a",
        relief="solid",
        borderwidth=1,
        pady=10
    )
    lbl_instruccion.pack(pady=10)

    respuesta_var = tk.StringVar(value="")  # Inicializar explícitamente
    botones = []

    # Función para limpiar el mensaje de advertencia cuando se selecciona una opción
    def limpiar_advertencia(*args):
        texto_actual = lbl_feedback.cget("text").lower()
        # Solo limpiar si es un mensaje de advertencia
        if "seleccionar una opción" in texto_actual or "debés seleccionar" in texto_actual:
            lbl_feedback.config(text="", bg="#0d1117", relief="flat", borderwidth=0)
    
    # Agregar trace a la variable para detectar cambios
    respuesta_var.trace_add("write", limpiar_advertencia)

    for opcion in ["a", "b", "c"]:
        btn = tk.Radiobutton(
            frame,
            text="",
            variable=respuesta_var,
            value=opcion,
            font=("Arial", 18),
            fg="#c9d1d9",
            bg="#0d1117",
            selectcolor="#21262d",
            activebackground="#161b22",
            anchor="w",
            width=60,
            justify="left",
        )
        btn.pack(pady=5)
        botones.append(btn)

    # Label para mostrar feedback (correcto/incorrecto/advertencia)
    lbl_feedback = tk.Label(
        frame,
        text="",
        font=("Arial", 18, "bold"),
        bg="#0d1117",
        wraplength=1000,
        justify="center",
        pady=20,
        relief="flat"
    )
    lbl_feedback.pack(pady=20)

    # Frame para los botones
    frame_botones = tk.Frame(frame, bg="#0d1117")
    frame_botones.pack(pady=20)

    btn_siguiente = tk.Button(
        frame_botones,
        text="Siguiente",
        font=("Arial", 18, "bold"),
        bg="#238636",
        fg="white",
        width=20,
    )
    btn_siguiente.grid(row=0, column=0, padx=10)

    # Botón para volver al menú
    btn_menu = tk.Button(
        frame_botones,
        text="Volver al Menú",
        font=("Arial", 18, "bold"),
        bg="#d73a49",
        fg="white",
        width=20,
        command=lambda: volver_al_menu()
    )
    btn_menu.grid(row=0, column=1, padx=10)

    # === Lógica de navegación ===
    indice = 1
    correctas = 0
    respondida = False  # Para controlar si ya respondió la pregunta actual

    def volver_al_menu():
        """Confirma y vuelve al menú principal"""
        if messagebox.askyesno(
            "Volver al Menú",
            "¿Estás seguro de que querés abandonar el tutorial?\nSe perderá tu progreso actual."
        ):
            # Llamar al callback sin resultado
            if on_finish:
                on_finish("tutorial abandonado")

    def mostrar_pregunta():
        nonlocal indice, respondida
        respondida = False  # Resetear el estado
        lbl_feedback.config(text="", relief="flat", bg="#0d1117", borderwidth=0)  # Limpiar feedback anterior
        
        if indice > len(preguntas_tutorial):
            terminar_tutorial()
            return

        pregunta = preguntas_tutorial[indice]
        lbl_pregunta.config(text=f"Pregunta {indice}/{len(preguntas_tutorial)}: {pregunta['pregunta']}")
        respuesta_var.set("")  # Limpiar selección explícitamente

        # Actualiza el texto de los botones
        for i, (clave, texto) in enumerate(pregunta["opciones"].items()):
            botones[i].config(text=f"{clave}) {texto}", value=clave)

    def siguiente():
        nonlocal indice, correctas, respondida
        
        # ====== VALIDACIÓN: Verificar si seleccionó una opción ======
        seleccion = respuesta_var.get().strip()  # Obtener y limpiar espacios
        
        # PRIMERO: Verificar si NO seleccionó nada
        if not seleccion or seleccion == "":
            # Mostrar advertencia en amarillo
            lbl_feedback.config(
                text="⚠️  Por favor, debés seleccionar una de las opciones para poder continuar  ⚠️",
                fg="#ffcc00",  # Amarillo brillante
                bg="#332200",  # Fondo oscuro amarillento
                relief="solid",
                borderwidth=2
            )
            # NO avanzar, simplemente retornar
            return

        # SEGUNDO: Si ya respondió esta pregunta, pasar a la siguiente
        if respondida:
            indice += 1
            mostrar_pregunta()
            return

        correcta = preguntas_tutorial[indice]["respuesta"]

        if seleccion == correcta:
            correctas += 1
            # Mostrar feedback verde
            lbl_feedback.config(
                text="✅ ¡CORRECTO! ¡Muy bien!",
                fg="#3fb950",
                bg="#0d1117",
                relief="flat",
                borderwidth=0
            )
        else:
            correcta_texto = preguntas_tutorial[indice]["opciones"][correcta]
            # Mostrar feedback rojo con la respuesta correcta
            lbl_feedback.config(
                text=f"❌ INCORRECTO\n\nLa respuesta correcta era: {correcta}) {correcta_texto}",
                fg="#f85149",
                bg="#0d1117",
                relief="flat",
                borderwidth=0
            )

        respondida = True  # Marcar que ya respondió

    def terminar_tutorial():
        # ====== MODIFICADO: Sin segundo cartel, solo uno ======
        if correctas >= 7:
            messagebox.showinfo(
                "🎉 ¡Felicitaciones!", 
                f"Aprobaste el tutorial con {correctas}/10 respuestas correctas.\n\n"
                f"Ahora pasarás al Nivel 2."
            )
            if on_finish:
                on_finish("tutorial aprobado")
        else:
            messagebox.showwarning(
                "😕 Tutorial no aprobado", 
                f"Obtuviste {correctas}/10 respuestas correctas.\n"
                f"Necesitás al menos 7 para aprobar.\n\n"
                f"Seras redireccionado a la teoría de Nivel 1."
            )
            if on_finish:
                on_finish("tutorial no aprobado")

    btn_siguiente.config(command=siguiente)
    mostrar_pregunta()
