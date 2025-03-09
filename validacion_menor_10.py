import tkinter as tk
from tkinter import messagebox

class ValidacionMenor10(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Validación Menor que 10")
        self.geometry("300x100")

        tk.Label(self, text="Ingrese un número menor que 10:").pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        tk.Button(self, text="Validar", command=self.validar).pack()

    def validar(self):
        try:
            numero = int(self.entry.get())
            if numero >= 10:
                messagebox.showerror("Error", "El número debe ser menor que 10")
            else:
                messagebox.showinfo("Éxito", f"Número válido: {numero}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número entero válido")