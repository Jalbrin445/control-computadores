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
from tkinter import messagebox,ttk # Estos métodos me sirve para mostrar mensajes de error y el otro me sirve para los botones
from datetime import datetime # Este modulo es utilizado para formatear horas

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
    """
    Esta es la clase de los computadores que se van a 
    ingresar al sistema.
    """
    def __init__(self, codigo, hora_entrada, valor_entrada):
        """
        Este es el método inicial que sirve para definir 
        los atributos de la clase de los
        computadores en mantenimiento
        """
        self.__codigo = codigo
        self.__hora_entrada = hora_entrada
        self.__valor_hora = valor_entrada
        self.__hora_salida = None

    def registrar_entrada(self, codigo, valor_entrada,hora):
        """
        Método para registrar los datos de entrada, esto con el fin de acceder a los atributos de forma privada
        y seguir con el estandar de encapsulamiento
        """
        self.__codigo = codigo
        self.__hora_entrada = hora
        self.__valor_hora = valor_entrada

    def registrar_salida(self, hora):
        """Método utilizado para registrar la hora de salida"""
        self.__hora_salida = hora
        
    def calcular_valor(self, hora_salida):
        """
        Método de la clase de los computadores utilizado para calcular el valor del mantenimiento,
        en este orden de ideas primero se formatean las horas de entrada y salida a un formato Hora y Minutos, posteriormente
        se verifica si la hora de salida es mayor a la hora de entrada y en tal caso de no serlo se retorna el valor
        de 1 (Para posteriormente utilizarlo en la función), pero si la condición anterior se cumple entonces
        se registra la hora de salida, se saca el deltaHora con el formateo y posteriormente se convierte el tiempo
        transcurrido a un número decimal, para posteriormente devolver o retornar
        la operación del calculo del valor total
        """
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
        """
        Este método sirve para obtener el código
        """
        return self.__codigo
    

class Usuario():
    """
    Esta es la clase para instanciar todos los usuarios que ingresen
    Los métodos que lo componen son:

    1. Método init que permite definir las propiedades del objeto
    2. Método validar que valida los valores ingresados por el usuario
    3. El método obtener usuario que permite obtener el usuario para utilizarlo posteriormente

    """

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

# Instanciamos la clase Usuario()
usuario = Usuario()

def registrar_equipo(entry_codigo,entry_valor_h, entry_hora_in, listbox_v):
    """
    esta función es desarrollada para registrar equipos, 
    primero se obtienen los datos ingresados por el usuario,
    luego se verifica si ha ingresado datos o no, si falta algún dato
    arroja el mensaje de que le hace falta un dato y sino pasa 
    a crear la instancia u objeto de la clase 
    ComputadorMantenimiento y almacena la instancia en la lista_computadores
    para posteriormente arrojarla en una lista visual, luego se eliminan
    los datos de pantalla y se arroja un mensaje de exito
    Pero si existe un error durante la ejecución de este bloque entonces se
    asocia al error del formato de hora ingresado
    """

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
        messagebox.showinfo("Exito", f"PC {cod} registrado correctamente")

    except ValueError:
        messagebox.showerror("Error", "El valor por hora debe ser un número")

def procesar_salida(listbox_v, entry_h_out):
    """
    Esta función permite procesar los datos del requerimiento de salida
    de las computadoras del estado de mantenimiento, es por ello que en este orden de ideas
    en primer lugar se toma lo que el usuario ha seleccionado
    en pantalla, luego se saca el indice de dicha selección
    teniendo en cuenta que este indice coincide con el de la
    lista donde se guardan las PCs, por otro lado, se toma
    el valor ingresado por el usuario en el campo de hora de
    salida y no existe o el usuario no escribio dicho campo se arroja
    una ventana de error, pero si existe, se sigue con la ejecución normal

    luego, se toma el objeto que se selecciono de la lista de computadores
    y se utiliza el método calcular_valor() que calcula el valor con una operación simple

    Ahora bien, si el usuario digito una hora incorrecta, es decir, menor a la hora de entrada
    entonces se evaluara en una sentencia condicional y se arrojará un error, pero si ingreso todo correctamente entonces
    se arroja un mensaje de información dandole al usuario toda la información correctamente

    Por último, si en el bloque anterior ocurre un error 
    entonces se arrojará una ventana emergente con el mensaje de
    que el formato de hora no es correcto
    """
    seleccion = listbox_v.curselection()
    if not seleccion:
        messagebox.showerror("Error", "No hay computadores registrados")
        return
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
    """
    Esta es la función que contiene toda la información de la dashboard principal
    al ser un código largo, lo documentaré poco a poco
    """
    # Inicializamos la variable de la pantalla Dashboard
    global ventanaJAMGDashboard
    ventanaJAMGDashboard = tk.Tk()
    ventanaJAMGDashboard.title("Dashboard - Computer Registration")
    ventanaJAMGDashboard.geometry(f"{ANCHO}x{ALTO}") # Definir el tamaño inicial de la pantalla
    
    ventanaJAMGDashboard.grid_columnconfigure(0, weight=1) # Este método sirve para que las columna seleccionada (0) tenga algunas reglas especiales
    etiqueta_saludo_bienvenida = tk.Label(ventanaJAMGDashboard, font=fuente_general_titulo,text=f"Welcome {usuario.obtenerUser()}")
    etiqueta_saludo_bienvenida.grid(row=0, column=0, pady= 20) # Método utilizado para posicionar un elemento en la ventana

    # Sección de entrada
    seccion_entradaJAMG = tk.LabelFrame(ventanaJAMGDashboard, font=fuente_general_sub,text="Check-in", padx=10, pady=10) # Método utilizado para generar frame o piezas completas en una ventana
    seccion_entradaJAMG.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")
    seccion_entradaJAMG.grid_columnconfigure(1, weight=1)

    tk.Label(seccion_entradaJAMG, font=fuente_general_2, text="PC Code:").grid(row=0, column=0, sticky="w")
    entry_codigo = tk.Entry(seccion_entradaJAMG)
    entry_codigo.grid(row=0, column=1, sticky="ew", pady=2)
    

    tk.Label(seccion_entradaJAMG, font=fuente_general_2, text="Hourly Rate:").grid(row=1, column=0,sticky="w")
    entry_valor_h = tk.Entry(seccion_entradaJAMG) # Método utilizado para crear un campo de entrada
    entry_valor_h.grid(row=1, column=1, sticky="ew", pady=2)
    

    tk.Label(seccion_entradaJAMG, font=fuente_general_2, text="Check-in Time (HH:MM):").grid(row=2, column=0,sticky="w")
    entry_hora_in = tk.Entry(seccion_entradaJAMG)
    entry_hora_in.grid(row=2, column=1, sticky="ew", pady=2)
    

    btn_registrar = ttk.Button(seccion_entradaJAMG, text="Save", command= lambda: registrar_equipo(entry_codigo, entry_valor_h, entry_hora_in, lista_visual)) # Método utilizado para crear un botón en la interfaz
    btn_registrar.grid(row=3, column=0, columnspan=2, pady=5)


    # Sección de salida
    seccion_salidaJAMG = tk.LabelFrame(ventanaJAMGDashboard, font=fuente_general_sub,text="Outgoing management and collection", padx=10, pady=10)
    seccion_salidaJAMG.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
    seccion_salidaJAMG.grid_columnconfigure(1,weight=1)

    tk.Label(seccion_salidaJAMG, font=fuente_general,text="Computers in the Workshop:").grid(row=0, column=0, sticky="w")

    lista_visual = tk.Listbox(seccion_salidaJAMG, height=4) # Este método puede generar una lista en pantalla, donde el usuario puede seleccionar elementos
    lista_visual.grid(row=1, column=0, columnspan=2, sticky="ew", pady=2)

    tk.Label(seccion_salidaJAMG, font=fuente_general_2,text="Departure Time (HH:MM):").grid(row=2, column=0, sticky="w")
    entry_hora_out = tk.Entry(seccion_salidaJAMG)
    entry_hora_out.grid(row=2, column=1, sticky="ew", pady=2)

    btn_cobrar = ttk.Button(seccion_salidaJAMG, text="Calculate Final Cost", command=lambda: procesar_salida(lista_visual, entry_hora_out))
    btn_cobrar.grid(row=3, column=0, columnspan=2, pady=5)

    ventanaJAMGDashboard.mainloop()

def PantallaInicial():
    """
    En esta función se encuentran todos los elementos relacionados con la pantalla principal
    o inicial de la pantalla, en primer lugar, se definen todos los parametros de la pantalla, como la dimensión
    de la ventana, el titulo y un frame que es aquel
    que contiene el formulario de inicio de sesión
    posteriormente se utilizan se definen todos los labels, entry y el boton que
    actuara cuando se ingresen los datos en la pantalla (el usuario y la contraseña)
    y por último se muestra un label estático en el cual se encuentra información del estudiante
    """

    global ventanaJAMGInicioSesion, entry_passwordJAMG, entry_usernameJAMG
    ventanaJAMGInicioSesion = tk.Tk() # Instancia de la clase Tk en el modulo tkinter

    ventanaJAMGInicioSesion.grid_columnconfigure(0, weight=1)
    ventanaJAMGInicioSesion.grid_rowconfigure(0, weight=1)
    ventanaJAMGInicioSesion.grid_rowconfigure(6, weight=1)

    # Ancho y alto del monitor
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
    """
    Esta es la función para el Login, se utiliza para validar el usuario y contraseña
    haciendo uso del método validar dentro de la clase Usuario,
    siempre y cuando el usuario y contraseña sean correctos entonces
    "destruirá" la pantalla de login o inicial para posteriormente llamar a la función
    que contiene la pantalla de dashboard principal, pero si el usuario no es valido o si el
    método validar de la clase Usuario arroja False entonces se mostrará un mensaje por pantalla
    en forma de error, el cual le avisa al usuario que el usuario o contraseña son incorrectos
    """

    global usernameJAMG
    passwordJAMG = entry_passwordJAMG.get()
    usernameJAMG = entry_usernameJAMG.get()
    validacion_inicio_sesionJAMG = usuario.validar(usernameJAMG,passwordJAMG)
    
    # Estructura de validación de usuario logueandose
    if (validacion_inicio_sesionJAMG== True):
        ventanaJAMGInicioSesion.destroy() #En este espacio se cierra la ventana actual de inicio de sesión y se abre una nueva ventana.
        DashboardPrincipal()
    else:
        messagebox.showerror("Login", "Incorrect username or password")
    


PantallaInicial()