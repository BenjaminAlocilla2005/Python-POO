class Trabajador:
    def __init__(self, nombre):
        self.nombre = nombre

    # Mensaje generico
    def tarea(self):
        print(f"{self.nombre} tiene un trabajo")


class Chef(Trabajador):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad

    def tarea(self):
        print(f"{self.nombre} esta preparando {self.especialidad}")


class Mesero(Trabajador):
    def __init__(self, nombre, seccion):
        super().__init__(nombre)
        self.seccion = seccion

    def tarea(self):
        print(f"{self.nombre} esta llevando la comida al {self.seccion}")
    

class AyudanteChefMesero(Chef, Mesero):
    def __init__(self, nombre, especialidad, seccion):
        Chef.__init__(self, nombre, especialidad)
        Mesero.__init__(self, nombre, seccion)

    def tarea(self):
        print(f"{self.nombre} esta cocinado {self.especialidad} y despues ira a entregar la comida al {self.seccion}")

# Intancias para poner el codigo a prueba
trabajador_generico = Trabajador("Jon")
cocinero = Chef("Mario", "Espagueti")
camarero = Mesero("Billy", "Primer piso")
ayudante = AyudanteChefMesero("Maria", "Pizza", "Tercer piso")

# Usando prints
print("")
print(trabajador_generico)
print("")
print(cocinero)
print("")
print(camarero)
print("")
print(ayudante)
print("")