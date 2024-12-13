import tkinter as tk # importar tkinter
import time

ventana = tk.Tk() # Crear nuestra ventana principal
ventana.title("Ejemplo Boton") 
ventana.geometry("650x300")

boton = tk.Button(ventana, text="Presione aqui") # creacion de botones
boton.config(fg="white", bg="green",font=("Arial,12")) # configurracion de botones
boton.pack()

def boton_presionado():
    print("Boton Presionado")

boton.config(command=boton_presionado) # obtener eventos con botones

ventana.mainloop()
