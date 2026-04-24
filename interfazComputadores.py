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

## Ancho y alto de la ventana
ANCHO = 400
ALTO = 500

## Configuración de fuentes
fuente_general = ("Times New Roman", 14, "bold")
fuente_general_2 = ("Times New Roman", 12, "bold")
fuente_general_titulo = ("Times New Roman", 20, "bold")
fuente_general_sub = ("Times New Roman", 16, "bold")
# Lista donde se almacenarán los computadores
lista_computadores = []

class ComputadorMantenimiento():
    def __init__(self, codigo, hora_entrada, valor_entrada):
        self.__codigo = codigo
        self.__hora_entrada = hora_entrada
        self.__valor_hora = valor_entrada
        self.__hora_salida = None

    def registrar_entrada(self, codigo, valor_entrada,hora):
        self.__codigo = codigo
        self.__hora_entrada = hora
        self.__valor_hora = valor_entrada

    def registrar_salida(self, hora):
        self.__hora_salida = hora
        
    def calcular_valor(self, hora_salida):
        horaE = self.__hora_entrada
        objetohoraE = datetime.strptime(horaE, "%H:%M")
        objetohoraS = datetime.strptime(hora_salida, "%H:%M")

        if objetohoraS < objetohoraE:
            return -1
        else:
            self.registrar_salida(hora_salida)
            deltaHora = objetohoraS - objetohoraE
            deltaHoraF = deltaHora.total_seconds() /3600
            return deltaHoraF*self.__valor_hora
        
    def obtener_codigo(self):
        return self.__codigo
class Usuario():
    def __init__(self, usuario="", password=""):
        self.__password = password
        self.__usuario = usuario
    
    def validar(self, usuario_ingresado, password_ingresada):
        self.__usuario = usuario_ingresado
        self.__password = password_ingresada
        if ((usuario_ingresado.lower() == "programacion") and (password_ingresada.lower() == "programacion")):
            return True
        else:
            return False
    
    def obtenerUser(self):
        return self.__usuario
        
usuario = Usuario()

def registrar_equipo(entry_codigo,entry_valor_h, entry_hora_in, listbox_v):


    cod = entry_codigo.get()
    val = entry_valor_h.get()
    h_in = entry_hora_in.get()

    if not cod or not val or not h_in:
        messagebox.showerror("Registro Computador", "Alguno de los datos no ha sido ingresado")
        return
    try:
        instaComputador = ComputadorMantenimiento(cod, h_in, float(val))
        lista_computadores.append(instaComputador)

        listbox_v.insert(tk.END, cod)

        entry_codigo.delete(0, tk.END)
        entry_valor_h.delete(0, tk.END)
        entry_hora_in.delete(0, tk.END)
        messagebox.showinfo("Exito", f"PC {cod} regisrado correctamente")

    except ValueError:
        messagebox.showerror("Error", "El valor por hora debe ser un número")

def procesar_salida(listbox_v, entry_h_out):
    seleccion = listbox_v.curselection()

    indice = seleccion[0]
    computador_seleccionado = lista_computadores[indice]

    h_salida = entry_h_out.get()

    if not h_salida:
        messagebox.showerror("Error", "Debes ingresar la hora de salida")
        return
    
    try:
        costo_total = computador_seleccionado.calcular_valor(h_salida)

        if costo_total == -1:
            messagebox.showerror("Error", "La hora de salida no puede ser menor a la hora de entrada")
        else:
            messagebox.showinfo("Costo Total", f"El costo de mantenimiento para el PC con código {computador_seleccionado.obtener_codigo()} es:\n${costo_total:,.2f}")
            lista_computadores.pop(indice)
            listbox_v.delete(indice)
            entry_h_out.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Formato de hora incorrecto. Usa HH:MM")


def DashboardPrincipal():
    global ventanaJAMGDashboard
    ventanaJAMGDashboard = tk.Tk()
    ventanaJAMGDashboard.title("Dashboard - Registro de Computadores")
    ventanaJAMGDashboard.geometry(f"{ANCHO}x{ALTO}")

    ventanaJAMGDashboard.grid_columnconfigure(0, weight=1)
    etiqueta_saludo_bienvenida = tk.Label(ventanaJAMGDashboard, font=fuente_general_titulo,text=f"Bienvenido {usuario.obtenerUser()}")
    etiqueta_saludo_bienvenida.grid(row=0, column=0, pady= 20)

    # Sección de entrada
    seccion_entradaJAMG = tk.LabelFrame(ventanaJAMGDashboard, font=fuente_general_sub,text="Registro de Entrada", padx=10, pady=10)
    seccion_entradaJAMG.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")
    seccion_entradaJAMG.grid_columnconfigure(1, weight=1)

    tk.Label(seccion_entradaJAMG, font=fuente_general_2, text="Código PC:").grid(row=0, column=0, sticky="w")
    entry_codigo = tk.Entry(seccion_entradaJAMG)
    entry_codigo.grid(row=0, column=1, sticky="ew", pady=2)
    

    tk.Label(seccion_entradaJAMG, font=fuente_general_2, text="Valor Hora:").grid(row=1, column=0,sticky="w")
    entry_valor_h = tk.Entry(seccion_entradaJAMG)
    entry_valor_h.grid(row=1, column=1, sticky="ew", pady=2)
    

    tk.Label(seccion_entradaJAMG, font=fuente_general_2, text="Hora Entrada (HH:MM)").grid(row=2, column=0,sticky="w")
    entry_hora_in = tk.Entry(seccion_entradaJAMG)
    entry_hora_in.grid(row=2, column=1, sticky="ew", pady=2)
    

    btn_registrar = ttk.Button(seccion_entradaJAMG, text="Guardar", command= lambda: registrar_equipo(entry_codigo, entry_valor_h, entry_hora_in, lista_visual))
    btn_registrar.grid(row=3, column=0, columnspan=2, pady=5)


    # Sección de salida
    seccion_salidaJAMG = tk.LabelFrame(ventanaJAMGDashboard, font=fuente_general_sub,text="Gestión de salida y Cobro", padx=10, pady=10)
    seccion_salidaJAMG.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
    seccion_salidaJAMG.grid_columnconfigure(1,weight=1)

    tk.Label(seccion_salidaJAMG, font=fuente_general,text="Computadores en Taller:").grid(row=0, column=0, sticky="w")

    lista_visual = tk.Listbox(seccion_salidaJAMG, height=4)
    lista_visual.grid(row=1, column=0, columnspan=2, sticky="ew", pady=2)

    tk.Label(seccion_salidaJAMG, font=fuente_general_2,text="Hora Salida (HH:MM)").grid(row=2, column=0, sticky="w")
    entry_hora_out = tk.Entry(seccion_salidaJAMG)
    entry_hora_out.grid(row=2, column=1, sticky="ew", pady=2)

    btn_cobrar = ttk.Button(seccion_salidaJAMG, text="Calcular Costo Final", command=lambda: procesar_salida(lista_visual, entry_hora_out))
    btn_cobrar.grid(row=3, column=0, columnspan=2, pady=5)

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
    tk.Label(frame_login, font=fuente_general_titulo,text="Login").grid(row=0, column=0, padx=10, pady=10)
    
    ## Sesión de nombre de usuario
    label_usernameJAMG = tk.Label(frame_login, font=fuente_general,text="Username")
    label_usernameJAMG.grid(row=1, column=0, padx=10, pady=10)
    entry_usernameJAMG = tk.Entry(frame_login,width=30)
    entry_usernameJAMG.grid(row=2, column=0, padx=10, pady=10)

    # Sesión de contraseña

    label_passwordJAMG = tk.Label(frame_login, font=fuente_general,text="Password")
    label_passwordJAMG.grid(row=3, column=0, padx=10, pady=10)
    entry_passwordJAMG = tk.Entry(frame_login, width=30,show="*")
    entry_passwordJAMG.grid(row=4, column=0, padx=10, pady=10)

    # Sección del botón para loguearse
    buttonJAMG = ttk.Button(frame_login,text="Login", command=Login)
    buttonJAMG.grid(row=5, column=0, padx=100, pady=10)
    # Sección de información personal
    etiqueta_informacion_personal = tk.Label(ventanaJAMGInicioSesion, 
        font=fuente_general, 
        text="Juan Albrin Meza Guzmán\nElectronic Engineering\nNational Open and Distance University",
        justify="center")
    etiqueta_informacion_personal.grid(row=6, column=0, pady= 20)
    ventanaJAMGInicioSesion.mainloop()
    




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