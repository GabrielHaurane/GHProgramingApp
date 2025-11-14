import tkinter as tk
from tkinter import messagebox
from inicioProgram.inicio_program import iniciar_programa
passw = "123"
ventana = tk.Tk() 
ventana.geometry("800x500")
ventana.title("Inicio de Sesión")
intentos = 3
def verificar_clave():
    global intentos
    clave_ingresada = entry_clave.get()

    if clave_ingresada == passw:
        messagebox.showinfo("Acceso concedido", "Clave correcta. Iniciando programa...")
        ventana.destroy() 
        iniciar_programa()  
    else:
        intentos_restantes = intentos - 1
        if intentos_restantes > 0:
            mensaje_incorrecto.config(
                text=f"❌ Clave incorrecta. Te quedan {intentos_restantes} intentos.",
                fg="red"
            )
            intentos -= 1
            entry_clave.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Se agotaron los intentos. El programa se cerrará.")
            ventana.destroy()

frame = tk.Frame(ventana, bg="#101820")
frame.place(relx=0.5, rely=0.5, anchor="center")

titulo = tk.Label(frame, text="🔐 INGRESE LA CLAVE DE ACCESO", font=("Arial", 22, "bold"), fg="#00BFFF", bg="#101820")
titulo.pack(pady=20)

entry_clave = tk.Entry(frame, show="*", font=("Consolas", 18), width=25, justify="center")
entry_clave.pack(pady=10)

btn_enviar = tk.Button(frame, text="Ingresar", font=("Arial", 16), bg="#00BFFF", fg="white", command=verificar_clave)
btn_enviar.pack(pady=15)

mensaje_incorrecto = tk.Label(frame, text="", font=("Arial", 14), fg="red", bg="#101820")
mensaje_incorrecto.pack(pady=10)

entry_clave.bind("<Return>", lambda event: verificar_clave())

ventana.mainloop()