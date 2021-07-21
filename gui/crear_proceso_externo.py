from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkcalendar import *

#Ventana para crear el proceso de venta externo
def crearProcesoExterno(self):
    crearExterno=tk.Toplevel(self,width=700, height=600)
    crearExterno.config()
    solicitudLabel=Label(crearExterno, 
                    text="CREAR PROCESO DE VENTA EXTERNO", 
                    font=("Montserrat",25), 
                    bg='alice blue', 
                    #padx=600, 
                    #pady=40, 
                    relief="raised")
    solicitudLabel.grid(row=0, column=0)

    
