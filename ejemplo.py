class Animal():
    # Constructor de la clase animal
    # Atributos de la clase animal(caracteristicas compartidas por todos )
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    # Métodos de la clase animal (comportamientos)
    def correr(self):
        print(f"{self.nombre} está corriendo")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo")

# Creando un objeto de la clase animal
gatito = Animal("Michi", "Gato", 4)
perrito = Animal("Firulais", "Perro", 2)
loro = Animal("Loro", "Ave", 1)

print(f"El nombre del animal es: {gatito.nombre}")
print(f"la especie del animal es: {gatito.especie}")
print(f"{gatito.nombre} tiene {gatito.edad} años")

print(f"El nombre del animal es: {perrito.nombre}")
print(f"la especie del animal es: {perrito.especie}")
print(f"{perrito.nombre} tiene {perrito.edad} años")

print(f"El nombre del animal es: {loro.nombre}")
print(f"la especie del animal es: {loro.especie}")
print(f"{loro.nombre} tiene {loro.edad} años")



