import tkinter as tk
from tkinter import messagebox

class SumaNNumeros(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Suma de N Números")
        self.geometry("300x100")

        tk.Label(self, text="Ingrese un número entero positivo:").pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack()

    def calcular(self):
        try:
            n = int(self.entry.get())
            if n < 0:
                messagebox.showerror("Error", "El número debe ser positivo")
            else:
                suma = n * (n + 1) // 2
                messagebox.showinfo("Resultado", f"La suma de los primeros {n} números es: {suma}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número entero válido")