from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkcalendar import *
from bd.conexion import database, cursor

#Menu del crear proceso de venta
def crearVentana(self):
    #Creación de los widgets de la ventana de proceso de venta, donde el administrador elije que tipo de proceso de venta creara
    procesoVenta = tk.Toplevel(self, width=600, height=400)

    procesoVenta.configure(bg='DarkOliveGreen2')

    volverButton=tk.Button(procesoVenta, font=("Lato",12, "bold"), text="Volver Atrás", command=lambda:[self.menuVentana(),
                                                                                procesoVenta.destroy()]
                                                                                ,foreground='gray24', bg='cyan2')
    volverButton.place(relx=0.1, rely=0.3, anchor=CENTER, width=100, height=30)

    crearLabel=Label(procesoVenta, text="CREACIÓN DE PROCESO DE VENTA", font=("Montserrat",20), 
                                                                        bg='alice blue', 
                                                                        padx=300, 
                                                                        pady=40, 
                                                                        relief="raised")
    crearLabel.place(relx=0.5, y=40, anchor=CENTER)

    preguntaLabel=Label(procesoVenta, text="¿Cuál proceso de venta desea crear?", foreground='gray24',font=("Montserrat",15, "bold"), bg='DarkOliveGreen2')
    preguntaLabel.place(relx=0.5, y=170, anchor=CENTER)

    botonExterno=tk.Button(procesoVenta, font=("Lato",12, "bold"),text="Proceso de Venta Externo", foreground='gray24', bg='SeaGreen1',command=lambda: [procesoVentana(self),
                                                                                            procesoVenta.destroy()])
    botonExterno.place(relx=0.5, y=250, anchor=CENTER, width=300, height=50)

    botonInterno=tk.Button(procesoVenta, font=("Lato",12, "bold"),text="Proceso de Venta Interno", foreground='gray24', bg='SeaGreen2')
    botonInterno.place(relx=0.5, y=350, anchor=CENTER, width=300, height=50)

#Ventana para seleccionar el proceso de venta
def procesoVentana(self):
    #Creación de widgets de la ventana de proceso de venta externo
    crearVenta = tk.Toplevel(self, width=600, height=700)
    crearVenta.configure(bg='DarkOliveGreen2')
    selectLabel=Label(crearVenta, text="Solicitudes Pendientes", font=("Montserrat",20), bg='DarkOliveGreen2')
    selectLabel.grid(row=0, column=0, columnspan = 3)

    #Tabla 
    tabla = ttk.Treeview(crearVenta,height =10, columns=('#1','#2'))
    tabla.grid(row = 1, column = 0, columnspan = 3)
    tabla.heading('#0', text = 'Cliente', anchor = CENTER)
    tabla.heading('#1', text = 'Fecha de Orden', anchor = CENTER)
    tabla.heading('#2', text = 'Solicitud N°', anchor = CENTER)

    #Metodos
    # Obtener Solicitudes
    def obtenerSolicitudes(self):
        # Limpiado de tabla
        solicitudes = tabla.get_children()
        for elemento in solicitudes:
            tabla.delete(elemento)
        # Buscando datos
        cursor.execute("SELECT id_pedido, CONCAT(primer_nombre, ' ',ap_paterno), created_at FROM pedidos "+
                        "INNER JOIN usuario ON usuario.id_usuario = pedidos.id_cliente "+
                        "WHERE activo = 1 ORDER BY created_at ASC LIMIT 10")
        resultado = cursor.fetchall()
        # Llenando la tabla
        for (id_pedido,cliente,fecha) in resultado:
            tabla.insert('', 'end',text=(cliente), values=(fecha,id_pedido))

    #Llenado de tabla
    obtenerSolicitudes(self)

    # Eliminar una solicitud
    def eliminarSolicitud(self):
        try:
            tabla.item(tabla.selection())['values'][1]
        except IndexError as e:
            messagebox.showerror("Error en Eliminar","Seleccione una solicitud de la tabla para eliminar")
            return
        
        id_soli = tabla.item(tabla.selection())['values'][1]
        cursor.execute("DELETE FROM pedidos WHERE id_pedido = "+str(id_soli))
        cursor.execute("DELETE FROM pedido_frutas WHERE pedido_id = "+str(id_soli))
        messagebox.showinfo("Eliminado correctamente","La solicitud con ID: "+str(id_soli)+" fue eliminado satisfactoriamente")
        obtenerSolicitudes(self)
    
    #Validación previa antes de ir a crear la venta externa
    def validarVentaExterna(self):
        try:
            tabla.item(tabla.selection())['values'][1]
        except IndexError as e:
            messagebox.showerror("Error en Crear Venta","Seleccione una solicitud de la tabla para crear la venta")
            return
        id_solicitud = tabla.item(tabla.selection())['values'][1]
        crearVenta.destroy()
        crearProcesoExterno(self,id_solicitud)
 
    #Botones 
    crearButton=tk.Button(crearVenta, text="Crear Venta", command=lambda:[validarVentaExterna(self)]
                                                        ,foreground='thistle1', bg='MediumPurple4', font=("Lato",12, "bold"))
    crearButton.grid(row=2, column=0)
    eliminarButton=tk.Button(crearVenta, text="Eliminar Solicitud", command=lambda:[eliminarSolicitud(self)]
                                                                    ,foreground='thistle1', bg='MediumPurple3', font=("Lato",12, "bold"))
    eliminarButton.grid(row=2, column=1)
    volverButton=tk.Button(crearVenta, text="Volver Atrás", command=lambda:[crearVentana(self),
                                                                            crearVenta.destroy()],
                                                            foreground='thistle1', bg='MediumPurple2', font=("Lato",12, "bold"))
    volverButton.grid(row=2, column=2)

#Ventana para editar el proceso de venta externo elegido
def crearProcesoExterno(self, id):
    crearExterno=tk.Toplevel(self,width=700, height=600)
    crearExterno.configure(bg='DarkOliveGreen2')
    solicitudLabel=Label(crearExterno, 
                    text="CREAR PROCESO DE VENTA EXTERNO", 
                    font=("Montserrat",25), 
                    bg='alice blue', 
                    #padx=600, 
                    #pady=40, 
                    relief="raised")
    solicitudLabel.grid(row=0, column=0, columnspan = 8)

    #Metodos
    ##Metodo para obtener los datos, en este caso frutas del pedido y sus detalles.
    def obtenerDatos(self):
        #Buscar las frutas del pedido
        cursor.execute("SELECT pedido_frutas.fruta_id, pedido_frutas.id_pedido_fruta, pedido_frutas.pedido_id "+
                        "FROM pedido_frutas 	INNER JOIN pedidos ON pedido_frutas.pedido_id = pedidos.id_pedido "+
					    "INNER JOIN frutas ON pedido_frutas.fruta_id = frutas.id_fruta "+
                        "WHERE pedido_frutas.pedido_id = "+str(id))
        frutas = cursor.fetchall()

        frutas_baratas = []

        #Recorrer las frutas de productores para hallar la fruta más accesible 
        for id_fruta, id_pe_fru, id_pedido in frutas:
            cursor.execute("SELECT 	fruta_productor.id_fru_pro, frutas.nombre, pedido_frutas.cantidad, fruta_productor.precio_kilo * pedido_frutas.cantidad, fruta_productor.id_productor, fruta_productor.precio_kilo, pedidos.id_cliente, pedidos.id_pedido, CONCAT(primer_nombre, ' ',ap_materno) "+
                            "FROM fruta_productor INNER JOIN frutas ON fruta_productor.id_fruta = frutas.id_fruta "+
						    "INNER JOIN pedido_frutas ON fruta_productor.id_fruta = pedido_frutas.fruta_id "+
                            "INNER JOIN pedidos ON pedido_frutas.pedido_id = pedidos.id_pedido "+
                            "INNER JOIN usuario ON fruta_productor.id_productor = usuario.id_usuario "+
                            "WHERE pedidos.id_pedido = "+ str(id_pedido) +" AND "+
	                        "pedido_frutas.id_pedido_fruta = "+ str(id_pe_fru) +" AND fruta_productor.id_fruta = "+ str(id_fruta) +" AND fruta_productor.id_fru_pro = (SELECT fruta_productor.id_fru_pro "+
                            "FROM fruta_productor INNER JOIN frutas ON fruta_productor.id_fruta = frutas.id_fruta WHERE fruta_productor.id_fruta = "+ str(id_fruta) +" ORDER BY fruta_productor.precio_kilo ASC LIMIT 1)")
                        
            frutas_cursor = cursor.fetchone()
            frutas_baratas.append([frutas_cursor[0],frutas_cursor[1],frutas_cursor[2],frutas_cursor[3],frutas_cursor[4],frutas_cursor[5],frutas_cursor[6],frutas_cursor[7],frutas_cursor[8]])

        print(frutas_baratas)

        crearCampos(self,frutas_baratas)

    #Metodo que se ejecuta al presionar el boton de crear venta en el formulario.
    def crearVentaFinal(self, frutas):

        fila = 0
        monto_total = 0
        for row in frutas:
            monto_total = frutas[fila][3] + monto_total
            fila = fila + 0

        fila = 0

        try:
            cursor.execute("INSERT INTO venta (id_venta, monto_total, id_cliente,id_pedido,activo) VALUES(null,"+str(monto_total)+","
                                                                                                                +str(frutas[0][6])+","
                                                                                                                +str(frutas[0][7])+",1);")
            id_venta = cursor.lastrowid
            database.commit()
            try:
                for row in frutas:
                    cursor.execute("INSERT INTO detalle_venta VALUES(null," +str(frutas[fila][2])+","
                                                                            +str(frutas[fila][3])+","
                                                                            +str(frutas[fila][0])+","
                                                                            +str(id_venta)+");")
                    database.commit()
                    fila = fila + 1
                cursor.execute("UPDATE pedidos SET activo = 0 WHERE id_pedido="+str(frutas[0][7]))
                database.commit()
                messagebox.showinfo("Venta Creada", "La venta ha sido creada satisfactoriamente")
                procesoVentana(self)
                crearExterno.destroy()
            except IndexError as e:
                messagebox.showerror("Error en Crear Venta","No se pudo agregar la venta correctamente, verifique detalles del pedido")
        except IndexError as e:
            messagebox.showerror("Error en Crear Venta","No se pudo agregar la venta correctamente, verifique datos")
        

    #Metodo para crear los campos a partir de los datos seleccionados de la tabla
    def crearCampos(self, frutas_baratas): 
        #Declaración de variables incrementables
        cons = 1
        fila = 0

        for row in frutas_baratas:

            productoLabel=selectLabel=Label(crearExterno, text="Producto: ", font=("Montserrat",12), bg='DarkOliveGreen2')
            productoLabel.grid(row=cons, column=0)

            productoEntry=Entry(crearExterno, textvariable=StringVar(value=frutas_baratas[fila][1]), state='readonly')
            productoEntry.grid(row=cons, column=1)

            cantidadLabel=selectLabel=Label(crearExterno, text="Cantidad: ", font=("Montserrat",12), bg='DarkOliveGreen2')
            cantidadLabel.grid(row=cons, column=2)

            cantidadEntry=Entry(crearExterno, textvariable=IntVar(value=frutas_baratas[fila][2]))
            cantidadEntry.grid(row=cons, column=3)

            frutas_baratas[fila][3] = frutas_baratas[fila][2] * frutas_baratas[fila][5]

            totalPagar=selectLabel=Label(crearExterno, text="Precio Total: ", font=("Montserrat",12), bg='DarkOliveGreen2')
            totalPagar.grid(row=cons, column=4)

            totalEntry=Entry(crearExterno, textvariable=StringVar(value=("$"+str(frutas_baratas[fila][3]))), state='readonly')
            totalEntry.grid(row=cons, column=5)

            productorLabel=selectLabel=Label(crearExterno, text="Productor: ", font=("Montserrat",12), bg='DarkOliveGreen2')
            productorLabel.grid(row=cons, column=6)

            productorEntry=Entry(crearExterno, textvariable=StringVar(value=frutas_baratas[fila][8]))
            productorEntry.grid(row=cons, column=7)

            fila = fila + 1
            cons = cons + 1

        enviarButton=tk.Button(crearExterno, text="Crear Proceso de Venta", command=lambda:[crearVentaFinal(self, frutas_baratas)]
                                                                            ,foreground='thistle1', bg='DarkGoldenrod3', font=("Lato",12, "bold"))
        enviarButton.grid(row=cons, column=1)
        cancelarButton=tk.Button(crearExterno, text="Anular Solicitud"
                                                ,foreground='thistle1', bg='DarkGoldenrod2', font=("Lato",12, "bold"))
        cancelarButton.grid(row=cons, column=3) 
        volverAtrasButton=tk.Button(crearExterno, text="Volver Atrás", command=lambda:[procesoVentana(self),
                                                                                    crearExterno.destroy()]
                                                                        ,foreground='thistle1', bg='DarkGoldenrod1', font=("Lato",12, "bold"))
        volverAtrasButton.grid(row=cons, column=5)

    #Llamado de Metodos
    obtenerDatos(self)
        
