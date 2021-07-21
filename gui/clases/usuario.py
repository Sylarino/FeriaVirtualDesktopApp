from bd.conexion import database

class Usuario():

    rut = ""
    primernombre = ""
    segundonombre = ""
    apellidomaterno = ""
    apellidopaterno = ""
    correo = ""
    genero = ""
    fechanacimiento = ""
    contrasena = ""

    def __init__(self, rut, primernombre, segundonombre, apellidomaterno, apellidopaterno, correo, genero, fechanacimiento, contrasena):
        self.rut = rut
        self.primernombre = primernombre
        self.segundonombre = segundonombre
        self.apellidomaterno = apellidomaterno
        self.apellidopaterno = apellidopaterno
        self.correo = correo
        self.genero = genero
        self.fechanacimiento = fechanacimiento
        self.contrasena = contrasena

    def getRut(self):
        return self.rut

    def getPrimerNombre(self):
        return self.primernombre

    def getSegundoNombre(self):
        return self.segundonombre

    def getApellidoMaterno(self):
        return self.apellidomaterno

    def getApellidoPaterno(self):
        return self.apellidopaterno

    def getCorreo(self):
        return self.correo

    def getGenero(self):
        return self.genero

    def getFechaNacimiento(self):
        return self.fechanacimiento
    
    def getContrasena(self):
        return self.contrasena

    #Metodos
    def agregarUsuario(self):
        usuario = Usuario()


    




