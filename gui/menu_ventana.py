    #Ventana de creación del proceso de venta externo
    def ventaVentana(self):
        #Creación de widgets de la ventana de creación del proceso de venta a partir de una solicitud
        ventaSolicitud = tk.Toplevel(self, width=600, height=700)

        ventanaLabel=Label(ventaSolicitud, text="Confirmación de creación de proceso de venta", font=("Montserrat",20))
        ventanaLabel.place(relx=0.5, y=40, anchor=CENTER)