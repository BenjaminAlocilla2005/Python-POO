class Automovil():
    # Constructor de la clase Automovil
    # Atributos de la clase Automovil (caracteristicas compartidas por todos los)
    def __init__(self, marca, modelo, anio, color):
        self.marca = str(marca)
        self.modelo = modelo
        self.anio = anio
        self.color = color


    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando")

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando")


auto1 = Automovil("Toyota", "Corolla", 2020, "Rojo")
auto2 = Automovil("Ford", "Mustang", 2021, "Azul")
auto3 = Automovil("Honda", "Civic", 2019, "Negro")

print(f"El auto1 es un {auto1.marca} {auto1.modelo} del año {auto1.anio}")
print("")

auto1.arrancar()
print("")
auto1.frenar()
print("")
auto1.acelerar()
print("")