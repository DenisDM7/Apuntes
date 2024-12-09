import tkinter as tk # importar tkinter

ventana = tk.Tk() # Crear nuetra ventana principal

ventana.title("Mi primer ventana") # Cambiar el titulo de la Ventana
ventana.geometry("600x400") # caqmbiar tamano de la ventana
ventana.minsize(400, 200)  # Cambiar lo minimo que se puede minimizar
ventana.maxsize(800, 600)  # Cambiar lo maximo que se puede maximizar
ventana.configure(bg="lightblue") #Cambair de color la ventana
ventana.resizable(False,False) #bloquear el minimizar y maximizar
# ventana.iconbitmap("icono.jpg") cambiar el icono







ventana.mainloop() # Bucle principal de la aplicacion

