import tkinter as tk # importar tkinter

ventana = tk.Tk() # Crear nuestra ventana principal
ventana.title("Ejemplo Boton") 
ventana.geometry("650x300")

etiqueta = tk.Label(ventana, text="Lo de abajo es un entry")
etiqueta.pack()

entrada= tk.Entry(ventana) #Creacion de la entrada
entrada.config(fg="white", bg="black", font=("Arial", 12))
entrada.pack()

entrada.insert(0, "Nombre") # poner un texto por defecto

def aplicar_texto():
    texto= entrada.get() # Obtener el texto del entry
    etiqueta.config(text=texto)

boton_aplicar =tk.Button(ventana,text="Aplicar texto a la etiqueta", command=aplicar_texto)
boton_aplicar.pack()


ventana.mainloop() 




