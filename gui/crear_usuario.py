from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkcalendar import *
from clases.usuario import Usuario
from bd.conexion import database, cursor
import rut_chile

def crearUsuarioVentana(self):
        #Creación de widgets para crear un usuario
        crearUsuario=tk.Toplevel(self) #width=600, height=600)
        crearUsuario.resizable(0,0)
        usuLabel=Label(crearUsuario, 
                        text="CREAR USUARIO", 
                        font=("Montserrat",25), 
                        bg='alice blue', 
                        padx=300, 
                        pady=40, 
                        relief="raised")
        usuLabel.grid(row=0, column=0, columnspan=4)

        crearUsuario.configure(bg='DarkOliveGreen3')

        #Variables
        primerNombre=tk.StringVar()
        segundoNombre=tk.StringVar()
        apellidoPaterno=tk.StringVar()
        apellidoMaterno=tk.StringVar()
        rut=tk.StringVar()
        genero=tk.StringVar()
        contrasena=tk.StringVar()
        contrasena2=tk.StringVar()
        correo=tk.StringVar()
        pais=tk.StringVar()
        buscarId=tk.StringVar()
        buscarNombre=tk.StringVar()

        #Metodos


        volverButton=tk.Button(crearUsuario, text="Volver Atrás", command=lambda:[self.menuVentana(),
                                                                                    crearUsuario.destroy()]
                                                                                    ,foreground='white', bg='DarkGoldenrod1', font=("Lato",12, "bold"))
                                                                                    
        volverButton.grid(row=0, column=0)

        primerNombreLabel=Label(crearUsuario, text="Primer Nombre:", font=("Lato",12), bg='DarkOliveGreen3')
        primerNombreLabel.grid(row=1, column=0)
        primerNombreEntry=Entry(crearUsuario, textvariable=primerNombre)
        primerNombreEntry.grid(row=1, column=1)

        segundoNombreLabel=Label(crearUsuario, text="Segundo Nombre:", font=("Lato",12), bg='DarkOliveGreen3')
        segundoNombreLabel.grid(row=1, column=2)
        segundoNombreEntry=Entry(crearUsuario, textvariable=segundoNombre)
        segundoNombreEntry.grid(row=1, column=3)

        apellidoPatLabel=Label(crearUsuario, text="Apellido Paterno:", font=("Lato",12), bg='DarkOliveGreen3')
        apellidoPatLabel.grid(row=2, column=0)
        apellidoPatEntry=Entry(crearUsuario, textvariable=apellidoPaterno)
        apellidoPatEntry.grid(row=2, column=1)

        apellidoMatLabel=Label(crearUsuario, text="Apellido Materno:", font=("Lato",12), bg='DarkOliveGreen3')
        apellidoMatLabel.grid(row=2, column=2)
        apellidoMatEntry=Entry(crearUsuario, textvariable=apellidoMaterno)
        apellidoMatEntry.grid(row=2, column=3)

        rutLabel=Label(crearUsuario, text="RUT:", font=("Lato",12), bg='DarkOliveGreen3')
        rutLabel.grid(row=3, column=0)
        rutEntry=Entry(crearUsuario, textvariable=rut)
        rutEntry.grid(row=3, column=1)

        tipoLabel=Label(crearUsuario, text="Tipo de Usuario", font=("Lato",12), bg='DarkOliveGreen3')
        tipoLabel.grid(row=3, column=2) 
        opcionesTipo=["Transportista","Cliente Externo","Cliente Interno","Productor"]    
        tipoCM= Combobox(crearUsuario, width="17", values=opcionesTipo, state="readonly")
        tipoCM.grid(row=3, column=3)
            
        generoLabel=Label(crearUsuario, text="Genero", font=("Lato",12), bg='DarkOliveGreen3')
        generoLabel.grid(row=4, column=0) 
        opciones=["Masculino","Femenino","Otros"]    
        generoCM= Combobox(crearUsuario, width="17", values=opciones, state="readonly")
        generoCM.grid(row=4, column=1)

        correoLabel=Label(crearUsuario, text="Correo", font=("Lato",12), bg='DarkOliveGreen3')
        correoLabel.grid(row=4, column=2)
        correoEntry=Entry(crearUsuario, textvariable=correo)
        correoEntry.grid(row=4, column=3)

        contraLabel=Label(crearUsuario, text="Contraseña:", font=("Lato",12), bg='DarkOliveGreen3')
        contraLabel.grid(row=5, column=0)
        contraEntry=Entry(crearUsuario, textvariable=contrasena, show="*")
        contraEntry.grid(row=5, column=1)

        contra2Label=Label(crearUsuario, text="Repita Contraseña:", font=("Lato",12), bg='DarkOliveGreen3')
        contra2Label.grid(row=5, column=2)
        contra2Entry=Entry(crearUsuario, textvariable=contrasena2, show="*")
        contra2Entry.grid(row=5, column=3)

        paisLabel=Label(crearUsuario, text="País", font=("Lato",12), bg='DarkOliveGreen3')
        paisLabel.grid(row=6, column=0) 
        opcionesPais=["E.E.U.U","Canada","Argentina"]    
        paisCM= Combobox(crearUsuario, width="17", values=opcionesPais, state="readonly")
        paisCM.grid(row=6, column=1)

        nacimientoLabel=Label(crearUsuario, text="Fecha de Nacimiento:", font=("Lato",12), bg='DarkOliveGreen3')
        nacimientoLabel.grid(row=6, column=2)
        nacimientoCalendar=Calendar(crearUsuario, selectmode="day", year=2020, month=5, day=22, date_pattern='y-mm-dd')
        nacimientoCalendar.grid(row=7, column=3)

        #Metodos 

        #Metodo para agregar usuario a la base de datos y validaciones
        def agregarUsuario(self):
                if (primerNombre.get()=="" or segundoNombre.get()=="" or apellidoMaterno.get()=="" or apellidoPaterno.get()=="" or 
                rut.get()=="" or contrasena.get()=="" or contrasena2.get()=="" or correo.get()=="" or tipoCM.get()=="" or generoCM.get()=="" or paisCM.get()==""):
                        messagebox.showinfo("Datos Vacios", "Todos los campos son requeridos")   
                else:
                        if contrasena.get() != contrasena2.get():
                                messagebox.showinfo("Contraseña incorrecta", "Ambas contraseñas deben ser iguales")    
                        else:
                                cursor.execute("INSERT INTO usuario VALUES(null,"+"'"+ rut.get() +"','"+
                                                                                primerNombre.get() +"','"+
                                                                                segundoNombre.get() +"','"+
                                                                                apellidoPaterno.get() +"','"+
                                                                                apellidoMaterno.get() +"','"+
                                                                                correo.get() +"','"+
                                                                                generoCM.get() 
                                                                                +"','"+ nacimientoCalendar.get_date() +"','"+
                                                                                contrasena.get() +"','"+
                                                                                paisCM.get() +"','"+
                                                                                tipoCM.get() +"');")
                                database.commit()
                                messagebox.showinfo("Agregado Correctamente", "Usuario Agregado Satisfactoriamente")


        registrarButton=tk.Button(crearUsuario, text="Registrar Usuario", command=lambda:[agregarUsuario(self)], foreground='white', bg='DarkGoldenrod1', font=("Lato",12, "bold"))
        registrarButton.place(relx=0.2,rely=0.60,width=200, height=50)

        listarButton=tk.Button(crearUsuario, text="Listar Usuarios",foreground='white', bg='DarkGoldenrod1', font=("Lato",12, "bold"))
        listarButton.place(relx=0.2,rely=0.80,width=200, height=50)


