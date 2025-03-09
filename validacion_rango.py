import tkinter as tk
from tkinter import messagebox

class ValidacionRango(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Validación en Rango (0, 20)")
        self.geometry("300x100")

        tk.Label(self, text="Ingrese un número entre 0 y 20:").pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        tk.Button(self, text="Validar", command=self.validar).pack()

    def validar(self):
        try:
            numero = int(self.entry.get())
            if 0 <= numero <= 20:
                messagebox.showinfo("Éxito", f"Número válido: {numero}")
            else:
                messagebox.showerror("Error", "El número debe estar entre 0 y 20")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número entero válido")