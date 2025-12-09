class Vehiculo():
    def __init__(self, marca, gasolina, kilometros):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros = kilometros
    def conducir(self, km):
        print("")
    
    def cargar_gasolina(self):
        litros = input("Escoja por favor la cantidad de litros de gasolina que desea cargar: ")
        print(f"Usted ha cargado {litros} Litros de gasolina")



coche1 = Vehiculo("Mustang", 10.4)
coche2 = Vehiculo("Toyota", 20.7)

coche1.cargar_gasolina()