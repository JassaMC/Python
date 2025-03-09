# %%
# aumento_salario.py

import tkinter as tk
from tkinter import messagebox

def AumentoSalario(root):
    def calcular():
        try:
            sueldo = float(entry.get())
            aumento = sueldo * 0.15 if sueldo < 4000 else sueldo * 0.08
            nuevo_sueldo = sueldo + aumento
            messagebox.showinfo("Resultado", f"Nuevo sueldo: {nuevo_sueldo:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido")
    
    ventana = tk.Toplevel(root)
    ventana.title("Aumento de Salario")
    ventana.geometry("300x150")
    
    tk.Label(ventana, text="Ingrese sueldo:").pack(pady=5)
    entry = tk.Entry(ventana)
    entry.pack(pady=5)
    
    tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)
