from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkcalendar import *

#Ventana de ver solicitudes
def verSolicitudesVentana(self):
    #Creación de widgets para ver todas las solicitudes pendientes de venta
    verSolicitud=tk.Toplevel(self, width=700, height=600)
    solicitudLabel=Label(verSolicitud, 
                    text="VER SOLICITUDES DE VENTA AL EXTRANJERO", 
                    font=("Montserrat",25), 
                    bg='alice blue', 
                    #padx=600, 
                    #pady=40, 
                    relief="raised")
    solicitudLabel.grid(row=0, column=0)

    tabla = ttk.Treeview(verSolicitud,height =30, columns=('#1','#2','#3'))
    tabla.grid(row = 1, column = 0, columnspan = 1)
    tabla.heading('#0', text = 'Solicitud', anchor = CENTER)
    tabla.heading('#1', text = 'Cliente', anchor = CENTER)
    tabla.heading('#2', text = 'Fecha de Orden', anchor = CENTER)
    tabla.heading('#3', text = 'Productos', anchor = CENTER)

    volverButton=ttk.Button(verSolicitud, text="Volver Atrás", command=lambda:[self.menuVentana(),
                                                                            verSolicitud.destroy()])
    volverButton.grid(row=32, column=1)