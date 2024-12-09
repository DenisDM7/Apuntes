import tkinter as tk # importar tkinter

ventana = tk.Tk() # Crear nuetra ventana principal
ventana.title("Ejemplo Label") 
ventana.geometry("650x300")

etiqueta= tk.Label(ventana, text= "Hola soy una etiqueta") # Creacion de una etiqueta
etiqueta.config(fg="blue", bg= "yellow", font=("Arial", 12, "bold")) #configurar la etiqueta
etiqueta.pack()


ventana.mainloop() # Bucle principal de la aplicacion