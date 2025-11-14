from tkinter import *
ventana = Tk()
ventana.geometry("1600x920")
# def saludo(nombre):
#     print("Hola " + nombre) 
def mostrarTexto():
    texto = cajaTexto.get()
    etiqueta2["text"] = texto
etiqueta = Label(ventana, text="Hola Mundo", bg="black", fg="white", font=("Arial", 32))
etiqueta.pack(fill=X)
# boton1 = Button(ventana, text="click", font=("Arial", 16), command=lambda: saludo(cajaTexto.get()))
# boton1.pack()
boton2 = Button(ventana, text="Mostrar Texto", font=("Arial", 16), command=mostrarTexto)
boton2.pack()
cajaTexto = Entry(ventana, font=("Arial", 16))
cajaTexto.pack()
etiqueta2 = Label(ventana, font=("Arial", 16))
etiqueta2.pack()
ventana.mainloop()