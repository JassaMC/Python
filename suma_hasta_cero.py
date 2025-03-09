import tkinter as tk
from tkinter import messagebox

class SumaHastaCero(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Suma hasta Cero")
        self.geometry("300x150")

        self.suma = 0

        tk.Label(self, text="Ingrese números (0 para terminar):").pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        tk.Button(self, text="Agregar", command=self.agregar).pack()

        self.label_suma = tk.Label(self, text="Suma: 0")
        self.label_suma.pack()

    def agregar(self):
        try:
            numero = float(self.entry.get())
            if numero == 0:
                messagebox.showinfo("Resultado", f"La suma total es: {self.suma}")
            else:
                self.suma += numero
                self.label_suma.config(text=f"Suma: {self.suma}")
                self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido")