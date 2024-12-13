import tkinter as tk # importar tkinter

''' Los Frames de manera simplificada  son contenedores en los cuales ingresamos "cosas" como un botton , un evento etc'''

ventana = tk.Tk() # Crear nuetra ventana principal
ventana.title("Ejemplo de frame")
ventana.geometry("600x400") # caqmbiar tamano de la ventana

frame1= tk.Frame(ventana) # Creacion del frame en la ventana
frame1.configure(width=300, height=200, bg="red", bd=5) # Modificar el frame1
frame1.pack() # Empaquetar el frame para mostrarlo en la ventana

frame2= tk.Frame(frame1) # Creacion del frame2 en el frame1
frame2.configure(width=100, height=100, bg="blue", bd=5) # Modificar el frame2
frame2.pack() # Empaquetar el frame para mostrarlo en frame1

frame3= tk.Frame(ventana) # Creacion del frame3
frame3.configure(width=300, height=200, bg="yellow", bd=5) # Modificar el frame3
frame3.pack() # Empaquetar el frame para mostrarlo en la ventana


''' Los Labelframes son parecido a los frame con la diferencia que estos tienen titulo'''

labelframe = tk.LabelFrame(ventana,text="Grupo de widgets",bg="green", padx=10, pady=10) # Crear el label Frame
labelframe.configure(width=300, height=200)# Modificar el labelframe
labelframe.pack() # Empaquetar el labelframe en la ventana




ventana.mainloop() # Bucle principal de la aplicacion