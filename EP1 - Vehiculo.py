
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__disponible = True
    
    def marcar_vendido(self):
        disponibilidad = self.__disponible
        if disponibilidad : True
        else:
            print(f"El {self.__marca} no se encuentra disponible")
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_año(self):
        return self.__año

    def __str__(self):
        return f"El auto es de marca {self.__marca}, su modelo es {self.__modelo}"
    
class Concesionaria:
    def __init__(self):
        self.gestion = []
    
    def agregar_vehiculo(self, vehiculo):
        """Agrega un vehiculo"""
        if not isinstance(vehiculo, Vehiculo):
            return "Error: Solo se pueden agregar objetos Vehiculo"
        

Auto1 = Vehiculo("Auto", "Ferrari", 2000)

Auto1.marcar_vendido()
Auto1.get_marca()
Auto1.get_modelo()
Auto1.get_año
