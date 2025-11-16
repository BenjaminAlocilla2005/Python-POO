class Jugador:
    # Contador que incrementa
    JUGADORES_CREADOS = 0
    POSICIONES_VALIDAS = {"DEL", "VOL", "DEF", "ARQ"}

    def __init__(self, nombre:str, edad:int, posicion, club:str, energia, goles=0):
        self.__nombre = nombre
        self.__edad = edad
        self.__posicion = posicion
        self.__goles = goles
        self.club = club
        self.energia = energia

    @classmethod
    def creados(cls):
        return 
    
    @staticmethod
    def posicion_valida():
        return f""
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre():
        return ""

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad():
        return ""
    
    @property
    def posicion():
        return f""
    

    def entrenar(self, min):
        if not min > 0:
            raise ValueError("No puede ser un valor negativo")
        
        if min > 0:
            self.energia -= min
            return f"{self.nombre} entreno por {min} minutos"
        else:
            return f"{self.nombre} decidio no entrenar"
    
    def anotar_gol(self, anotaciones):
        if not self.__goles > 0:
            raise ValueError("Los goles no deben quedar negativos")
        
        if self.__goles > 0:
            return f"{self.nombre} anoto {self.__goles} gol/es"
        else:
            return f"{self.nombre} no anoto gol"
        

    def __str__(self):
        return f"Nombre: {self.nombre}, Club: {self.club}, Posicion: {self.__posicion}, Energia: {self.energia}, Goles: {self.__goles}"
    
    def invariantes_clase():
        pass
    
# Instancias de clase
jugador1 = Jugador("Luis", 20, "DEL", "Deportes Castro", 85)
jugador2 = Jugador("Jeremy", 18, "ARQ", "Deportes Castro", 90)

print(jugador1.__str__())

# Acciones de los jugadores
print(jugador1.entrenar(30))
print(jugador1.anotar_gol(3)) # Jugador 1 anota un o dos goles
print(jugador1.invariantes_clase())

