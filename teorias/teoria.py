import tkinter as tk
from tkinter import ttk

# ==============================
# FUNCIÓN PARA MOSTRAR TEORÍA EN UN FRAME
# ==============================
def mostrar_teoria_en_frame(contenedor, titulo, secciones, on_finish=None):
    """Muestra teoría dentro de un frame existente en lugar de crear una nueva ventana."""
    
    # Limpiar el contenedor
    for widget in contenedor.winfo_children():
        widget.destroy()

    # Marco principal
    frame = tk.Frame(contenedor, bg="#0d1117")
    frame.pack(expand=True, fill="both", padx=40, pady=40)

    lbl_titulo = tk.Label(
        frame,
        text=titulo,
        font=("Arial", 26, "bold"),
        fg="#58a6ff",
        bg="#0d1117"
    )
    lbl_titulo.pack(pady=20)

    # Caja de texto con scrollbar
    text_box = tk.Text(
        frame,
        wrap="word",
        font=("Consolas", 14),
        bg="#161b22",
        fg="white",
        insertbackground="white",
        relief="flat"
    )
    text_box.pack(expand=True, fill="both", pady=20)

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text_box.yview)
    scrollbar.pack(side="right", fill="y")
    text_box.config(yscrollcommand=scrollbar.set)

    # Estado interno
    index = 0

    def mostrar_seccion():
        nonlocal index
        if index < len(secciones):
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, secciones[index])
            index += 1
        else:
            if on_finish:
                on_finish()

    btn_siguiente = tk.Button(
        frame,
        text="Continuar",
        font=("Arial", 16, "bold"),
        bg="#238636",
        fg="white",
        command=mostrar_seccion
    )
    btn_siguiente.pack(pady=10)

    mostrar_seccion()  # mostrar primera sección
