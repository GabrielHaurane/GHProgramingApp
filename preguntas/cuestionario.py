import tkinter as tk
from tkinter import messagebox

def crear_cuestionario_en_frame(
    contenedor,
    titulo,
    preguntas,
    on_menu=None,
    on_releer=None,
    siguiente_nivel=None
):
    """Crea el cuestionario dentro de un frame existente en lugar de una nueva ventana."""
    
    # Limpiar el contenedor
    for widget in contenedor.winfo_children():
        widget.destroy()

    frame = tk.Frame(contenedor, bg="#0d1117")
    frame.pack(expand=True, fill="both", padx=50, pady=30)

    # Título del cuestionario
    lbl_titulo = tk.Label(
        frame, text=titulo, font=("Arial", 28, "bold"), fg="#58a6ff", bg="#0d1117"
    )
    lbl_titulo.pack(pady=20)

    # Pregunta
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

    # Opciones de respuesta
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
    
    for i in ["a", "b", "c"]:
        rb = tk.Radiobutton(
            frame,
            text="",
            variable=respuesta_var,
            value=i,
            font=("Arial", 18),
            fg="#c9d1d9",
            bg="#0d1117",
            selectcolor="#21262d",
            activebackground="#161b22",
            anchor="w",
            width=60,
            justify="left",
        )
        rb.pack(pady=5)
        botones.append(rb)

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

    # Botón Siguiente
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

    indice = 1
    correctas = 0
    respondida = False  # Para controlar si ya respondió la pregunta actual

    def volver_al_menu():
        """Confirma y vuelve al menú principal"""
        if messagebox.askyesno(
            "Volver al Menú",
            "¿Estás seguro de que querés abandonar el cuestionario?\nSe perderá tu progreso actual."
        ):
            if on_menu:
                on_menu()

    def mostrar_pregunta():
        nonlocal indice, respondida
        respondida = False  # Resetear el estado
        lbl_feedback.config(text="", relief="flat", bg="#0d1117", borderwidth=0)  # Limpiar feedback anterior
        
        if indice > len(preguntas):
            finalizar()
            return

        q = preguntas[indice]
        lbl_pregunta.config(text=f"Pregunta {indice}/{len(preguntas)}: {q['pregunta']}")
        respuesta_var.set("")  # Limpiar selección explícitamente
        
        # Actualizar opciones
        for j, (k, v) in enumerate(q["opciones"].items()):
            botones[j].config(text=f"{k}) {v}", value=k)

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

        # TERCERO: Verificar si la respuesta es correcta o incorrecta
        correcta = preguntas[indice]["respuesta"]
        
        if seleccion == correcta:
            correctas += 1
            # Mostrar feedback verde
            lbl_feedback.config(
                text="✅ ¡CORRECTO! ¡Excelente trabajo!",
                fg="#3fb950",
                bg="#0d1117",
                relief="flat",
                borderwidth=0
            )
        else:
            correcta_txt = preguntas[indice]["opciones"][correcta]
            # Mostrar feedback rojo con la respuesta correcta
            lbl_feedback.config(
                text=f"❌ INCORRECTO\n\nLa respuesta correcta era: {correcta}) {correcta_txt}",
                fg="#f85149",
                bg="#0d1117",
                relief="flat",
                borderwidth=0
            )
        
        respondida = True  # Marcar que ya respondió

    def mostrar_pantalla_final_curso():
        """Pantalla especial de felicitación al completar el curso completo (Nivel 2)"""
        # Limpiar el contenedor
        for widget in contenedor.winfo_children():
            widget.destroy()
        
        # Frame principal
        frame_final = tk.Frame(contenedor, bg="#0d1117")
        frame_final.pack(expand=True, fill="both")
        
        # Contenedor central
        contenido = tk.Frame(frame_final, bg="#0d1117")
        contenido.place(relx=0.5, rely=0.5, anchor="center")
        
        # Emoji/Icono de celebración
        lbl_icono = tk.Label(
            contenido,
            text="🎉🎓🏆",
            font=("Arial", 80),
            bg="#0d1117",
            fg="white"
        )
        lbl_icono.pack(pady=20)
        
        # Título principal
        lbl_titulo_final = tk.Label(
            contenido,
            text="¡FELICITACIONES!",
            font=("Arial", 48, "bold"),
            fg="#3fb950",
            bg="#0d1117"
        )
        lbl_titulo_final.pack(pady=10)
        
        # Mensaje de éxito
        lbl_mensaje = tk.Label(
            contenido,
            text="Has completado exitosamente\nla PROGRAMACIÓN BÁSICA",
            font=("Arial", 28, "bold"),
            fg="#58a6ff",
            bg="#0d1117",
            justify="center"
        )
        lbl_mensaje.pack(pady=20)
        
        # Línea decorativa
        separator = tk.Frame(contenido, height=3, width=600, bg="#3fb950")
        separator.pack(pady=20)
        
        # Mensaje adicional
        lbl_adicional = tk.Label(
            contenido,
            text="Ahora tenés los conocimientos fundamentales de:\n\n"
                 "✅ HTML - Estructura de páginas web\n"
                 "✅ CSS - Diseño y estilos\n"
                 "✅ JavaScript - Interactividad y programación",
            font=("Arial", 20),
            fg="white",
            bg="#0d1117",
            justify="center"
        )
        lbl_adicional.pack(pady=30)
        
        # Mensaje de despedida
        lbl_despedida = tk.Label(
            contenido,
            text="Gracias por visitar GH Programming",
            font=("Arial", 22, "italic"),
            fg="#c9d1d9",
            bg="#0d1117"
        )
        lbl_despedida.pack(pady=20)
        
        # Frame para los botones
        frame_botones_final = tk.Frame(contenido, bg="#0d1117")
        frame_botones_final.pack(pady=40)
        
        # Botón para volver al menú
        btn_volver_menu = tk.Button(
            frame_botones_final,
            text="🏠 Volver al Menú Principal",
            font=("Arial", 20, "bold"),
            bg="#1f6feb",
            fg="white",
            width=30,
            height=2,
            command=lambda: on_menu() if on_menu else None
        )
        btn_volver_menu.grid(row=0, column=0, padx=15, pady=10)
        
        # Botón para salir
        btn_salir = tk.Button(
            frame_botones_final,
            text="🚪 Salir de la Aplicación",
            font=("Arial", 20, "bold"),
            bg="#d73a49",
            fg="white",
            width=30,
            height=2,
            command=lambda: contenedor.master.destroy()
        )
        btn_salir.grid(row=0, column=1, padx=15, pady=10)

    def finalizar():
        total = len(preguntas)
        
        if correctas >= 8:
            # --- Aprobado ---
            if siguiente_nivel:
                # ====== MODIFICADO: Un solo cartel para Nivel 1 ======
                if messagebox.askyesno(
                    "🎉 ¡Felicitaciones!",
                    f"¡Aprobaste el cuestionario con {correctas}/{total}!\n\n"
                    f"¿Querés continuar al Nivel 2?"
                ):
                    siguiente_nivel()  # Va directo al siguiente nivel
                else:
                    if on_menu:
                        on_menu()
            else:
                # Es Nivel 2 (curso completo) - Mostrar pantalla especial directamente
                mostrar_pantalla_final_curso()

        else:
            # --- No aprobado ---
            opciones = messagebox.askyesno(
                "❌ No aprobado",
                f"Tu puntaje fue {correctas}/{total}.\nNecesitás al menos 8 respuestas correctas.\n\n¿Querés intentar el cuestionario de nuevo?"
            )
            if opciones:
                crear_cuestionario_en_frame(contenedor, titulo, preguntas, on_menu, on_releer, siguiente_nivel)
            else:
                # Releer o volver
                if messagebox.askyesno(
                    "Releer teoría",
                    "¿Querés releer la teoría antes de volver al menú?"
                ):
                    if on_releer:
                        on_releer()
                else:
                    if on_menu:
                        on_menu()

    btn_siguiente.config(command=siguiente)
    mostrar_pregunta()

    
# ============================================================
# PREGUNTAS NIVEL 1
# ============================================================
preguntas_nivel_1 = {
    1: {"pregunta": "¿Qué etiqueta HTML se usa para crear un título principal?",
        "opciones": {"a": "<h1>", "b": "<head>", "c": "<title>"},
        "respuesta": "a"},
    2: {"pregunta": "¿Qué propiedad de CSS se usa para cambiar el color del texto?",
        "opciones": {"a": "text-color", "b": "font-style", "c": "color"},
        "respuesta": "c"},
    3: {"pregunta": "¿Qué símbolo se usa para crear comentarios en JavaScript?",
        "opciones": {"a": "<!-- -->", "b": "//", "c": "#"},
        "respuesta": "b"},
    4: {"pregunta": "¿Qué etiqueta se utiliza para insertar imágenes en HTML?",
        "opciones": {"a": "<img>", "b": "<image>", "c": "<src>"},
        "respuesta": "a"},
    5: {"pregunta": "¿Qué atributo HTML se usa para especificar la URL de un enlace?",
        "opciones": {"a": "src", "b": "href", "c": "link"},
        "respuesta": "b"},
    6: {"pregunta": "¿Qué propiedad CSS se usa para centrar un texto?",
        "opciones": {"a": "text-position", "b": "align-text", "c": "text-align"},
        "respuesta": "c"},
    7: {"pregunta": "¿Dónde se coloca el código JavaScript dentro de un HTML?",
        "opciones": {"a": "En <body> o <head> usando <script>", "b": "Dentro de <style>", "c": "En <link>"},
        "respuesta": "a"},
    8: {"pregunta": "¿Qué se necesita para hacer que un input sea obligatorio?",
        "opciones": {"a": "mustfill", "b": "required", "c": "validate"},
        "respuesta": "b"},
    9: {"pregunta": "¿Qué etiqueta crea una lista ordenada?",
        "opciones": {"a": "<ul>", "b": "<li>", "c": "<ol>"},
        "respuesta": "c"},
    10: {"pregunta": "¿Qué tipo de dato representa true o false en JavaScript?",
        "opciones": {"a": "string", "b": "boolean", "c": "number"},
        "respuesta": "b"},
}

# ============================================================
# PREGUNTAS NIVEL 2
# ============================================================
preguntas_nivel_2 = {
    1: {"pregunta": "¿Qué es el atributo placeholder en un input?",
        "opciones": {"a": "Muestra un texto de ayuda", "b": "Cambia el color", "c": "Lo hace obligatorio"},
        "respuesta": "a"},
    2: {"pregunta": "¿Cuál es la función de getElementById()?",
        "opciones": {"a": "Crea un elemento", "b": "Elimina un elemento", "c": "Selecciona un elemento por ID"},
        "respuesta": "c"},
    3: {"pregunta": "¿Qué es Flexbox en CSS?",
        "opciones": {"a": "Redondear bordes", "b": "Sistema de diseño", "c": "Hoja de estilos"},
        "respuesta": "b"},
    4: {"pregunta": "¿Cuál es el tipo de input para ingresar una fecha?",
        "opciones": {"a": "text", "b": "date", "c": "calendar"},
        "respuesta": "b"},
    5: {"pregunta": "¿Qué es el DOM?",
        "opciones": {"a": "Una API", "b": "Estructura del HTML", "c": "Una base de datos"},
        "respuesta": "b"},
    6: {"pregunta": "¿Qué propiedad CSS oculta un elemento?",
        "opciones": {"a": "visibility: off", "b": "display: none", "c": "opacity: 0"},
        "respuesta": "b"},
    7: {"pregunta": "¿Cómo detectar un clic en JS?",
        "opciones": {"a": "addClick()", "b": "addEventListener('click')", "c": "onMouseDown()"},
        "respuesta": "b"},
    8: {"pregunta": "¿Qué etiqueta es para contenido independiente?",
        "opciones": {"a": "<div>", "b": "<aside>", "c": "<section>"},
        "respuesta": "c"},
    9: {"pregunta": "¿Qué propiedad posiciona un elemento relativamente?",
        "opciones": {"a": "absolute", "b": "static", "c": "relative"},
        "respuesta": "c"},
    10: {"pregunta": "¿Qué valor de text-align alinea a la derecha?",
        "opciones": {"a": "right", "b": "end", "c": "justify"},
        "respuesta": "a"},
}
