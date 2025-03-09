import tkinter as tk
from tkinter import messagebox

class ValidacionContador(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Validación con Contador")
        self.geometry("300x150")

        self.contador = 0

        tk.Label(self, text="Ingrese un número entre 0 y 20:").pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        tk.Button(self, text="Validar", command=self.validar).pack()

        self.label_contador = tk.Label(self, text="Intentos: 0")
        self.label_contador.pack()

    def validar(self):
        try:
            numero = int(self.entry.get())
            self.contador += 1
            self.label_contador.config(text=f"Intentos: {self.contador}")
            if 0 <= numero <= 20:
                messagebox.showinfo("Éxito", f"Número válido: {numero}")
            else:
                messagebox.showerror("Error", "El número debe estar entre 0 y 20")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número entero válido")