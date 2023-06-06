class Carrera:
    __cod = ""
    __nom = ""
    __fechaI = ""
    __duracion = ""
    __titulo = ""
    
    def __init__ (self, cod, nom , fechaI, duracion, titulo):
        self.__cod=cod
        self.__nom=nom
        self.__fechaI=fechaI
        self.__duracion=duracion
        self.__titulo=titulo
        
    def getNom (self):
        return str(self.__nom)
    
    def getCod (self):
        return str(self.__cod)
    
    def __str__(self):
        cadena = f"Codigo: {self.__cod}, Nombre: {self.__nom}, Fecha Inicio: {self.__fechaI}, Duracion: {self.__duracion}, Titulo: {self.__titulo}" + "\n"
        return cadena
