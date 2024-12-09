import tkinter as tk # importar tkinter
import time

ventana = tk.Tk() # Crear nuetra ventana principal
ventana.title("Ejemplo Label") 
ventana.geometry("650x300")


labelframe= tk.LabelFrame(ventana, text="Hora Actual",bg="green", padx=10, pady=10)
labelframe.configure(width=300, height=200)# Modificar el labelframe
labelframe.pack()

etiqueta= tk.Label(labelframe, text= "Hola soy una etiqueta") # Creacion de una etiqueta
etiqueta.config(fg="blue", bg= "yellow", font=("Arial", 12, "bold")) #configurar la etiqueta
etiqueta.pack()

def actualizar_hora(): 
    etiqueta.config(text=time.strftime("%H,%M,%S"))
    ventana.after(1000, actualizar_hora)

actualizar_hora()
    


ventana.mainloop() # Bucle principal de la aplicacion