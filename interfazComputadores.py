"""
La aplicación debe:

1. Registrar computadores en mantenimiento.
2. Guardarlos en una lista interna.
3. Seleccionar un computador para registrar
4. Calcular y mostrar el costo total.
5. Validar correctamente las horas.


"""



# Importación de modulos
import tkinter as tk
from tkinter import messagebox,ttk # Estos métodos me sirve para mostrar mensajes de error
from datetime import datetime

# Definición de clases, variables y más.

ANCHO = 400
ALTO = 500

class Usuario():
    def __init__(self, usuario="", password=""):
        self.__password = password
        self.__usuario = usuario
    
    def validar(self, usuario_ingresado, password_ingresada):
        self.__usuario = usuario_ingresado
        if ((usuario_ingresado.lower() == "programacion") and (password_ingresada.lower() == "programacion")):
            return True
        else:
            return False
    
    def obtenerUser(self):
        return self.__usuario
        
usuario = Usuario()
def DashboardPrincipal():
    global ventanaJAMGDashboard
    ventanaJAMGDashboard = tk.Tk()
    ventanaJAMGDashboard.title("Aplicación Registro de Computadores")
    etiqueta_saludo_bienvenida = tk.Label(ventanaJAMGDashboard, font=("Times New Roman", 20, "bold"),text=f"Bienvenido {usuario.obtenerUser()}")
    etiqueta_saludo_bienvenida.grid(row=0, column=0, pady= 20)
    ventanaJAMGDashboard.mainloop()

def PantallaInicial():

    global ventanaJAMGInicioSesion, entry_passwordJAMG, entry_usernameJAMG
    ventanaJAMGInicioSesion = tk.Tk()

    ventanaJAMGInicioSesion.grid_columnconfigure(0, weight=1)
    ventanaJAMGInicioSesion.grid_rowconfigure(0, weight=1)
    ventanaJAMGInicioSesion.grid_rowconfigure(6, weight=1)

    ancho_monitor = (ventanaJAMGInicioSesion.winfo_screenwidth())
    alto_monitor = (ventanaJAMGInicioSesion.winfo_screenheight())
    x = (ancho_monitor/2) - (ANCHO/2)
    y = (alto_monitor/2) - (ALTO/2)
    ventanaJAMGInicioSesion.geometry(f"{ANCHO}x{ALTO}+{int(x)}+{int(y)}")
    ventanaJAMGInicioSesion.title("Aplicación Registro de Computadores")
    # Labels y entrys de ventana de inicio de sesión
    frame_login = tk.Frame(ventanaJAMGInicioSesion)
    frame_login.grid(row=1, column=0)
    ## Sesión de nombre de usuario
    label_usernameJAMG = tk.Label(frame_login, font=("Times New Roman", 14, "bold"),text="Username")
    label_usernameJAMG.grid(row=1, column=0, padx=10, pady=10)
    entry_usernameJAMG = tk.Entry(frame_login,width=30)
    entry_usernameJAMG.grid(row=2, column=0, padx=10, pady=10)

    # Sesión de contraseña

    label_passwordJAMG = tk.Label(frame_login, font=("Times New Roman", 14, "bold"),text="Password")
    label_passwordJAMG.grid(row=3, column=0, padx=10, pady=10)
    entry_passwordJAMG = tk.Entry(frame_login, width=30,show="*")
    entry_passwordJAMG.grid(row=4, column=0, padx=10, pady=10)

    # Sección del botón para loguearse
    buttonJAMG = ttk.Button(frame_login,text="Login", command=Login)
    buttonJAMG.grid(row=5, column=0, padx=100, pady=10)
    # Sección de información personal
    etiqueta_informacion_personal = tk.Label(ventanaJAMGInicioSesion, 
        font=("Times New Roman", 14, "bold"), 
        text="Juan Albrin Meza Guzmán\nIngeniería Electrónica\nUniversidad Nacional Abierta y A Distancia",
        justify="center")
    etiqueta_informacion_personal.grid(row=6, column=0, pady= 20)
    ventanaJAMGInicioSesion.mainloop()
    
class ComputadorMantenimiento:
    def __init__(self, codigo, hora_entrada, valor_entrada):
        self.__codigo = codigo
        self.__hora_entrada = hora_entrada
        self.__valor_hora = valor_entrada
        

    def registrar_entrada(self, codigo, valor_entrada,hora):
        self.__codigo = codigo
        self.__hora_entrada = hora
        self.__valor_hora = valor_entrada

    def registrar_salida(self, hora_salida):
        pass
    def calcular_valor(self, hora_salida):
        pass
    def obtener_codigo(self, codigo):
        pass



def Login():
    global usernameJAMG
    passwordJAMG = entry_passwordJAMG.get()
    usernameJAMG = entry_usernameJAMG.get()
    validacion_inicio_sesionJAMG = usuario.validar(usernameJAMG,passwordJAMG)
    if (validacion_inicio_sesionJAMG== True):
        ventanaJAMGInicioSesion.destroy()
        DashboardPrincipal()
    else:
        messagebox.showerror("Login", "Incorrect username or password")
    #En este espacio se cierra la ventana actual de inicio de sesión y se abre una nueva ventana.
    


PantallaInicial()