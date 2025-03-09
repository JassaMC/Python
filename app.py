# app.py (Archivo principal)
import tkinter as tk
from aumento_salario import AumentoSalario
from parque_diversiones import ParqueDiversiones
from descuento_tienda import DescuentoTienda
from validacion_menor_10 import ValidacionMenor10
from validacion_rango import ValidacionRango
from validacion_contador import ValidacionContador
from suma_n_numeros import SumaNNumeros
from suma_hasta_cero import SumaHastaCero
from suma_hasta_100 import SumaHasta100
from calculo_pago import CalculoPago

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación de Problemas")
        self.geometry("400x300")

        tk.Label(self, text="Seleccione un problema:").pack()

        opciones = [
            ("Aumento Salario", AumentoSalario),
            ("Parque de Diversiones", ParqueDiversiones),
            ("Descuento en Tienda", DescuentoTienda),
            ("Validación Menor 10", ValidacionMenor10),
            ("Validación en Rango", ValidacionRango),
            ("Validación con Contador", ValidacionContador),
            ("Suma de N Números", SumaNNumeros),
            ("Suma hasta Cero", SumaHastaCero),
            ("Suma hasta 100", SumaHasta100),
            ("Cálculo de Pago", CalculoPago),
        ]

        for texto, clase in opciones:
            # Usamos una función lambda con un valor predeterminado para evitar el problema de captura
            tk.Button(
                self,
                text=texto,
                command=lambda c=clase: self.abrir_ventana(c)
            ).pack()

    def abrir_ventana(self, clase):
        """Abre una ventana con la clase seleccionada."""
        ventana = clase(self)
        ventana.grab_set()  # Hace que la ventana sea modal
    
