from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkcalendar import *
from ver_solicitudes_ventana import verSolicitudesVentana
from crear_usuario import crearUsuarioVentana
from crear_ventana import crearVentana   
from crear_proceso_externo import crearProcesoExterno
import rut_chile
from bd.conexion import database, cursor

class Application(Frame):

    def __init__(self, master=None):
        #Inicialización
        super().__init__(master, width=350, height=420)
        self.master = master
        self.pack()
        self.loginVentana()
        self.master.title("Feria Virtual")
        self.master.iconbitmap("img/feria.ico")
        self.master.resizable(0,0)
        self.configure(bg='DarkOliveGreen1')

    def menuVentana(self):
        root.withdraw()  
        #Creación de widgets del menú principal del administrador
        menuAdmin=tk.Toplevel(self, width=600, height=500)
        menuAdmin.configure(bg="DarkOliveGreen2")

        menuLabel=Label(menuAdmin, 
                        text="BIENVENIDO A FERIA VIRTUAL", 
                        font=("Montserrat",25), 
                        bg='alice blue', 
                        padx=600, 
                        pady=40, 
                        relief="raised")
        menuLabel.place(relx=0.5, y=40, anchor=CENTER)

        nombreUsuario=Label(menuAdmin, 
                        text="ADMINISTRADOR", 
                        font=("Montserrat",18),
                        bg='alice blue',
                        fg='dark slate gray')
        nombreUsuario.place(relx=0.5, y=80, anchor=CENTER)

        """
        img = Image.open('log-out.png')
        img = img.resize((80, 80), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        img = ImageTk.PhotoImage(img)

        botonCerrarSesion=ttk.Button(menuAdmin, image=img)
        botonCerrarSesion.place(relx=0.1, rely=0.3, anchor=CENTER, width=50, height=50)
        """
        botonCrear= tk.Button(menuAdmin, text="Mantención de Usuarios",foreground='thistle1',bg='salmon1',command=lambda: [crearUsuarioVentana(self),
                                                                                                                            menuAdmin.destroy()]
                                                                                            ,font=("Lato",12, "bold"))
        botonCrear.place(relx=0.5, y=140, anchor=CENTER, width=300, height=50)

        #botonSubasta=ttk.Button(menuAdmin, text="Publicar subasta")
        #botonSubasta.place(relx=0.5, y=200, anchor=CENTER, width=300, height=50)

        botonVenta=tk.Button(menuAdmin, text="Creación de Proceso de Venta",foreground='thistle1', bg='salmon1', command=lambda: [crearVentana(self), 
                                                                                                                            menuAdmin.destroy()]
                                                                                                        ,font=("Lato",12, "bold"))
        botonVenta.place(relx=0.5, y=200, anchor=CENTER, width=300, height=50)

        botonSubasta=tk.Button(menuAdmin, text="Creación de Reportes",foreground='thistle1',bg='salmon2',font=("Lato",12, "bold"))
        botonSubasta.place(relx=0.5, y=260, anchor=CENTER, width=300, height=50)

        botonSubasta=tk.Button(menuAdmin, text="Control de Contratos",foreground='thistle1',bg='salmon2',font=("Lato",12, "bold"))
        botonSubasta.place(relx=0.5, y=320, anchor=CENTER, width=300, height=50)

        #botonSubasta=ttk.Button(menuAdmin, text="Crear reportes de venta")
        #botonSubasta.place(relx=0.5, y=440, anchor=CENTER, width=300, height=50)

        botonSubasta=tk.Button(menuAdmin, text="Solicitudes de Venta Externa",foreground='thistle1',bg='salmon3', command=lambda: [verSolicitudesVentana(self),
                                                                                                                                            menuAdmin.destroy()]
                                                                                                                            ,font=("Lato",12, "bold"))
        botonSubasta.place(relx=0.5, y=380, anchor=CENTER, width=300, height=50)

        cerrarSesion=tk.Button(menuAdmin, text="Cerrar Sesión",foreground='thistle1',bg='salmon3',command=lambda: [root.deiconify(),
                                                                                                                    menuAdmin.destroy()]
                                                                                                ,font=("Lato",12, "bold"))
        cerrarSesion.place(relx=0.5, y=440, anchor=CENTER, width=200, height=50)

    def validacionUsuario(self, usr, pwd):
        #Validación de las credenciales del usuario
        cursor.execute("SELECT correo, contrasena, tipo_usuario FROM usuario WHERE correo = '"+ usr +"' AND contrasena = '"+ pwd +"' AND tipo_usuario = 'Administrador';")
        result = cursor.fetchone()
        print(result)
        if result is None:
            messagebox.showinfo(message="Contraseña y/o Usuario Incorrecto", 
                                title="Inicio de sesión fallido") 
        else:
            if (usr == result[0] and pwd == result[1] and result[2] == 'Administrador'):
                messagebox.showinfo(message="Contraseña y/o Usuario correcto", 
                                title="¡Inicio de sesión exitoso!")
                self.entradaUsuario.delete(0, 'end')
                self.entradaContraseña.delete(0, 'end')
                self.menuVentana()
            else:
                messagebox.showinfo(message="Contraseña y/o Usuario Incorrecto", 
                                    title="Inicio de sesión fallido")    

    #Ventana de Inicio de Sesión
    def loginVentana(self):
        #Ventana principal
        #Creación de los widgets de la interfaz de inicio de sesión del usuario        
        self.usuario=tk.StringVar()
        self.contrasena=tk.StringVar()

        self.iniciarLabel=Label(self, text="¡INICIA SESIÓN!", font=("Montserrat",30),
                                                            bg='alice blue', 
                                                            padx=600, pady=110, 
                                                            relief="raised")
        self.iniciarLabel.place(relx=0.5, y=40, anchor=CENTER)

        self.s = ttk.Style()
        self.s.configure('Kim.TButton', bg='maroon')

        self.icono=Image.open('img/feria.png')
        self.icono=self.icono.resize((206,98)) #Altura, Anchura
        self.render = ImageTk.PhotoImage(self.icono)

        self.iconoFeria=Label(self, image=self.render)
        self.iconoFeria.place(relx=0.5, y=120, anchor=CENTER)

        self.usuarioLabel=Label(self, text="Correo:", foreground='gray20',font=("Lato",12), bg='DarkOliveGreen1')
        self.usuarioLabel.place(relx=0.5, y=200, anchor=CENTER)

        self.entradaUsuario=Entry(self, textvariable=self.usuario)
        self.entradaUsuario.place(relx=0.5, y=230, anchor=CENTER)

        self.contrasenaLabel=Label(self, text="Contraseña:", foreground='gray20',font=("Lato",12), bg='DarkOliveGreen1')
        self.contrasenaLabel.place(relx=0.5, y=290, anchor=CENTER)

        self.entradaContraseña=Entry(self, textvariable=self.contrasena, show="*")
        self.entradaContraseña.place(relx=0.5, y=320, anchor=CENTER)

        self.botonIngresar=tk.Button(self, text="INGRESAR", font=("Lato",12, "bold") ,foreground='gray20',bg='thistle1',command= lambda: self.validacionUsuario(self.usuario.get(), 
                                                                                                    self.contrasena.get()))
        self.botonIngresar.place(relx=0.5, y=380, anchor=CENTER, width=100, height=40)


root = Tk()
app = Application(root)
app.mainloop()