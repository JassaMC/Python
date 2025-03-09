import tkinter as tk
from tkinter import messagebox

class CalculoPago(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cálculo de Pago")
        self.geometry("400x200")

        tk.Label(self, text="Nombre del empleado:").pack()
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        tk.Label(self, text="Horas normales trabajadas:").pack()
        self.entry_horas_normales = tk.Entry(self)
        self.entry_horas_normales.pack()

        tk.Label(self, text="Horas extras trabajadas:").pack()
        self.entry_horas_extras = tk.Entry(self)
        self.entry_horas_extras.pack()

        tk.Label(self, text="Pago por hora normal:").pack()
        self.entry_pago_hora = tk.Entry(self)
        self.entry_pago_hora.pack()

        tk.Label(self, text="Número de hijos:").pack()
        self.entry_hijos = tk.Entry(self)
        self.entry_hijos.pack()

        tk.Button(self, text="Calcular Pago", command=self.calcular_pago).pack()

    def calcular_pago(self):
        try:
            nombre = self.entry_nombre.get()
            horas_normales = float(self.entry_horas_normales.get())
            horas_extras = float(self.entry_horas_extras.get())
            pago_hora = float(self.entry_pago_hora.get())
            hijos = int(self.entry_hijos.get())

            pago_normal = horas_normales * pago_hora
            pago_extra = horas_extras * pago_hora * 1.5
            bonificacion = hijos * 0.5
            pago_total = pago_normal + pago_extra + bonificacion

            messagebox.showinfo("Resultado", 
                f"Nombre: {nombre}\n"
                f"Pago por horas normales: {pago_normal}\n"
                f"Pago por horas extras: {pago_extra}\n"
                f"Bonificación por hijos: {bonificacion}\n"
                f"Pago total: {pago_total}"
            )
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos")