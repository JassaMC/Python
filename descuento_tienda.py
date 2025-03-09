# descuento_tienda.py
import tkinter as tk
from tkinter import messagebox

def DescuentoTienda(root):
    def calcular():
        try:
            mes = entry_mes.get().strip().lower()
            importe = float(entry_importe.get())
            descuento = importe * 0.15 if mes == "octubre" else 0
            total = importe - descuento
            messagebox.showinfo("Resultado", f"Total a pagar: {total:.2f} soles")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un importe válido")
    
    ventana = tk.Toplevel(root)
    ventana.title("Descuento en Tienda")
    ventana.geometry("300x200")
    
    tk.Label(ventana, text="Ingrese mes:").pack(pady=5)
    entry_mes = tk.Entry(ventana)
    entry_mes.pack(pady=5)
    
    tk.Label(ventana, text="Ingrese importe:").pack(pady=5)
    entry_importe = tk.Entry(ventana)
    entry_importe.pack(pady=5)
    
    tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)
