# Crear una lista de frutas
frutas = ["Mango", "Manzana", "Banana", "Uvas"]
print(frutas)

# Eliminar elementos de la lista
frutas.pop(0)  # Elimina "Mango"
frutas.pop(1)  # Elimina "Banana"

# Añadir un nuevo elemento
frutas.append("Sandía")
print(frutas)

import tkinter as tk
from tkinter import simpledialog, messagebox

# Inicializar la ventana de diálogo
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

# Crear una lista para almacenar las calificaciones
calificaciones = []

# Capturar las calificaciones
for i in range(5):
    while True:
        try:
            calificacion = int(simpledialog.askstring("Input", f"Captura la calificación {i + 1}:"))
            calificaciones.append(calificacion)
            break
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

# Mostrar las calificaciones capturadas
resultado = "Calificaciones capturadas:\n"
for i, calificacion in enumerate(calificaciones):
    resultado += f"Calificación {i + 1}: {calificacion}\n"

messagebox.showinfo("Resultados", resultado)
