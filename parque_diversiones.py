# parque_diversiones.py
import tkinter as tk
from tkinter import messagebox

def ParqueDiversiones(root):
    def calcular():
        try:
            edad = int(entry.get())
            pago = 50 * 0.75 if edad < 10 else 50
            messagebox.showinfo("Resultado", f"Total a pagar: {pago:.2f} soles")
        except ValueError:
            messagebox.showerror("Error", "Ingrese una edad válida")
    
    ventana = tk.Toplevel(root)
    ventana.title("Parque de Diversiones")
    ventana.geometry("300x150")
    
    tk.Label(ventana, text="Ingrese edad:").pack(pady=5)
    entry = tk.Entry(ventana)
    entry.pack(pady=5)
    
    tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)
