import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import hashlib
import os

def crear_archivo_usuarios():
    if not os.path.exists("usuarios.txt"): 
        with open("usuarios.txt", "w") as f:
            usuarios = [
                ("admin", "password"),
                ("sarai", "1234")
            ]
            for usuario, contrasena in usuarios:
                hash_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
                f.write(f"{usuario},{hash_contrasena}\n")
        print("Archivo usuarios.txt creado con éxito.")
    else:
        print("El archivo usuarios.txt ya existe.")

class VentanaInicioSesion:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Inicio de Sesión")
        self.raiz.geometry("300x200")
        
        self.marco = ttk.Frame(self.raiz, padding="10")
        self.marco.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(self.marco, text="Usuario:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entrada_usuario = ttk.Entry(self.marco)
        self.entrada_usuario.grid(row=0, column=1, sticky=tk.EW, pady=5)
        
        ttk.Label(self.marco, text="Contraseña:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entrada_contrasena = ttk.Entry(self.marco, show="*")
        self.entrada_contrasena.grid(row=1, column=1, sticky=tk.EW, pady=5)
        
        self.boton_iniciar = ttk.Button(self.marco, text="Iniciar Sesión", command=self.autenticar)
        self.boton_iniciar.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.marco.columnconfigure(1, weight=1)

    def autenticar(self):
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()
        
        try:
            with open("usuarios.txt", "r") as f:
                usuarios = [linea.strip().split(",") for linea in f.readlines()]
                
                for user in usuarios:
                    if len(user) >= 2 and user[0] == usuario:
                        hash_ingresado = hashlib.sha256(contrasena.encode()).hexdigest()
                        if user[1] == hash_ingresado:
                            self.raiz.destroy()
                            app_principal = AplicacionPrincipal()
                            app_principal.ejecutar()
                            return
                
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo de usuarios no encontrado")

class AplicacionPrincipal:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Sistema de Consultas de Bienes Raíces")
        self.raiz.geometry("1000x700")
        
        try:
            self.datos = pd.read_csv("Sacramentorealestatetransactions (1).csv")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo CSV.")
            self.datos = pd.DataFrame()

        self.marco_principal = ttk.Frame(self.raiz, padding="10")
        self.marco_principal.pack(fill=tk.BOTH, expand=True)

        self.marco_consultas = ttk.LabelFrame(self.marco_principal, text="Consultas Disponibles", padding="10")
        self.marco_consultas.pack(fill=tk.X, pady=5)

        consultas = [
            ("Top 10 casas más caras", self.top_10_caras),
            ("Top 10 casas más baratas", self.top_10_baratas),
            ("Precio promedio por ciudad", self.precio_promedio_ciudad),
            ("Top 10 casas más grandes", self.top_10_grandes),
            ("Top 10 casas con más habitaciones", self.top_10_habitaciones),
            ("Distribución de baños", self.distribucion_banos),
            ("Precio promedio por código postal", self.precio_promedio_zip),
            ("Cantidad de casas vendidas por ciudad", self.casas_vendidas_ciudad),
            ("Relación precio/tamaño", self.relacion_precio_tamano),
            ("Casa más cara y barata por ciudad", self.caras_baratas_ciudad)
        ]

        for i, (texto, comando) in enumerate(consultas):
            boton = ttk.Button(self.marco_consultas, text=texto, command=comando)
            boton.grid(row=i//3, column=i%3, padx=5, pady=5, sticky=tk.EW)

        self.marco_resultados = ttk.LabelFrame(self.marco_principal, text="Resultados", padding="10")
        self.marco_resultados.pack(fill=tk.BOTH, expand=True)

        self.arbol = ttk.Treeview(self.marco_resultados)
        self.arbol.pack(fill=tk.BOTH, expand=True)

    def ejecutar(self):
        self.raiz.mainloop()

    def mostrar_resultados(self, df):
        for item in self.arbol.get_children():
            self.arbol.delete(item)

        self.arbol["columns"] = list(df.columns)
        self.arbol["show"] = "headings"

        for col in df.columns:
            self.arbol.heading(col, text=col)
            self.arbol.column(col, width=100, anchor=tk.CENTER)

        for _, fila in df.iterrows():
            self.arbol.insert("", tk.END, values=list(fila))

    def top_10_caras(self):
        resultado = self.datos.nlargest(10, 'price')
        self.mostrar_resultados(resultado)

    def top_10_baratas(self):
        resultado = self.datos.nsmallest(10, 'price')
        self.mostrar_resultados(resultado)

    def precio_promedio_ciudad(self):
        resultado = self.datos.groupby('city')['price'].mean().reset_index()
        self.mostrar_resultados(resultado)

    def top_10_grandes(self):
        resultado = self.datos.nlargest(10, 'sq__ft')
        self.mostrar_resultados(resultado)

    def top_10_habitaciones(self):
        resultado = self.datos.nlargest(10, 'beds')
        self.mostrar_resultados(resultado)

    def distribucion_banos(self):
        resultado = self.datos['baths'].value_counts().reset_index()
        resultado.columns = ['Número de Baños', 'Cantidad']
        self.mostrar_resultados(resultado)

    def precio_promedio_zip(self):
        resultado = self.datos.groupby('zip')['price'].mean().reset_index()
        self.mostrar_resultados(resultado)

    def casas_vendidas_ciudad(self):
        resultado = self.datos['city'].value_counts().reset_index()
        resultado.columns = ['Ciudad', 'Cantidad de Casas Vendidas']
        self.mostrar_resultados(resultado)

    def relacion_precio_tamano(self):
        self.datos['Precio por Pie Cuadrado'] = self.datos['price'] / self.datos['sq__ft']
        resultado = self.datos[['city', 'street', 'price', 'sq__ft', 'Precio por Pie Cuadrado']]
        self.mostrar_resultados(resultado)

    def caras_baratas_ciudad(self):
        resultado = self.datos.groupby('city').agg({'price': ['max', 'min']}).reset_index()
        self.mostrar_resultados(resultado)

if __name__ == "__main__":
    crear_archivo_usuarios() 
    raiz = tk.Tk()
    app = VentanaInicioSesion(raiz)
    raiz.mainloop()