import tkinter as tk

def guardar_contacto():
    nombre = nombre_entry.get()
    telefono = telefono_entry.get()

    with open("Asistente_virtual/Contactos.txt", "a") as file:
        file.write(nombre + "," + telefono + "\n")

    nombre_entry.delete(0, tk.END)
    telefono_entry.delete(0, tk.END)

# Creamos la ventana
ventana = tk.Tk()
ventana.geometry("300x200")

# Creamos los widgets (nombre, telefono, boton de registrar)
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.pack()

nombre_entry = tk.Entry(ventana)
nombre_entry.pack()

telefono_label = tk.Label(ventana, text="Teléfono:")
telefono_label.pack()

telefono_entry = tk.Entry(ventana)
telefono_entry.pack()

registrar_boton = tk.Button(ventana, text="Registrar", command=guardar_contacto)
registrar_boton.pack()

# Ejecutamos la ventana
ventana.mainloop()
