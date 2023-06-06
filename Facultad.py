class Facultad:
    __codigo = ""
    __nombre = ""
    __direccion = ""
    __localidad = ""
    __telefono = ""
    __carrera: object
    
    def __init__ (self, codigo,nombre,direccion,localidad,telefono, carrera):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__carrera=carrera
        
    def getCodigo (self):
        return str(self.__codigo)
    
    def getNombre (self):
        return str(self.__nombre)
    
    def getTelefono (self):
        return str(self.__telefono)
    
    def getDireccion (self):
        return str(self.__direccion)
    
    def getLocalidad (self):
        return str(self.__localidad)
    
    def getFacultad(self):
        return str(self.__codigo)+""+str(self.__nombre)+""+str(self.__direccion)+""+str(self.__localidad)+""+str(self.__telefono)+""
    
    def getCarrera(self):
        return str(self.__carrera)
