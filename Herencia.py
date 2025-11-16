class Animal:
    def __init__(self, nombre, edad, peso, genero):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.genero = genero

    def comer(self):
        print(f"{self.nombre} está comiendo")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")

    def mostrar_ficha(self):
        print("")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Genero: {self.genero}")
        print("")

class Perro(Animal):
    def __init__(self, nombre, edad, peso, genero, raza):
        super().__init__(nombre, edad, peso, genero)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

class Gato(Animal):
    def __init__(self, nombre, edad, peso, genero, color_pelaje):
        super().__init__(nombre, edad, peso, genero)
        self.color_pelaje = color_pelaje

    def maullar(self):
        print(f"{self.nombre} está ladrando")

class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, genero, color_plumaje):
        super().__init__(nombre, edad, peso, genero)
        self.color_pelaje = color_plumaje

    def volar(self):
        print(f"{self.nombre} está volando alto")

perro1 = Perro("Alex", 10, 19.7, "Masculino", "Pastor Aleman")
gato1 = Gato("Alice", 9, 10.4, "Femenino", "Blanco")
pajaro1 = Pajaro("Jimmy", 5, 5.2, "Masculino", "Naranja")

perro1.ladrar()
perro1.comer()
perro1.mostrar_ficha()
print("")

gato1.maullar()
gato1.comer()
gato1.mostrar_ficha()
print("")

pajaro1.volar()
pajaro1.comer()
pajaro1.mostrar_ficha()
print("")