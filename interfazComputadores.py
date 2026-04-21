# Importación de modulos
import tkinter as tk
from tkinter import messagebox,ttk
# Definición de clases, variables y más.
def DashboardPrincipal():
    global ventanaJAMGDashboard
    ventanaJAMGDashboard = tk.Tk()
    ventanaJAMGDashboard.title("Aplicación Registro de Computadores")

def PantallaInicial():

    global ventanaJAMGInicioSesion, entry_passwordJAMG, entry_usernameJAMG
    ventanaJAMGInicioSesion = tk.Tk()
    ventanaJAMGInicioSesion.title("Aplicación Registro de Computadores")
    # ventana de inicio de sesión

    ## Sesión de nombre de usuario
    label_usernameJAMG = tk.Label(ventanaJAMGInicioSesion, text="Username")
    label_usernameJAMG.grid(row=0, column=0, padx=100, pady=10)
    entry_usernameJAMG = tk.Entry(ventanaJAMGInicioSesion,width=30)
    entry_usernameJAMG.grid(row=1, column=0, padx=100, pady=10)

    # Sesión de contraseña

    label_passwordJAMG = tk.Label(ventanaJAMGInicioSesion, text="Password")
    label_passwordJAMG.grid(row=2, column=0, padx=100, pady=10)
    entry_passwordJAMG = tk.Entry(ventanaJAMGInicioSesion, width=30,show="*")
    entry_passwordJAMG.grid(row=3, column=0, padx=100, pady=10)

    buttonJAMG = ttk.Button(ventanaJAMGInicioSesion,text="Login", command=Login)
    buttonJAMG.grid(row=4, column=0, padx=100, pady=10)
    ventanaJAMGInicioSesion.mainloop()
    
class ComputadorMantenimiento:
    def __init__(self, codigo, hora_entrada, valor_entrada):
        self._codigo = codigo
        self._hora_entrada = hora_entrada
        self._valor_hora = valor_entrada
        

    def registrar_entrada(self, codigo, valor_entrada,hora):
        self._codigo = codigo
        
    def registrar_salida(hora_salida):
        pass
    def calcular_valor(self, hora_salida):
        pass
    def obtener_codigo(self, codigo):
        pass



def Login():
    passwordJAMG = entry_passwordJAMG.get()
    usernameJAMG = entry_usernameJAMG.get()
    if ((passwordJAMG.lower() == "programacion") and (usernameJAMG.lower() == "programacion")):
        ventanaJAMGInicioSesion.destroy()
        DashboardPrincipal()
    else:
        messagebox.showerror("Login", "Incorrect username or password")
    #En este espacio se cierra la ventana actual de inicio de sesión y se abre una nueva ventana.
    


PantallaInicial()