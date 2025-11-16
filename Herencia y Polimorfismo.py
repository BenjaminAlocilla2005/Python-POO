class Vehiculos:
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    def moverse(self): # Orden generica
        print(f"{self.tipo} se está moviendo")

"""
Todos los vehículos de carrera deben responder a la orden "moverse", pero
lo harán a su manera. Se debe definir un método moverse(self) en todas las
clases (ejemplo: Coche, Lancha, VehiculoAnfibio, Hidroavion).
Coche.moverse() debe llamar a self.rodar().
Lancha.moverse() debe llamar a self.navegar().
VehiculoAnfibio.moverse() debe llamar a self.rodar() y self.navegar().
Hidroavion.moverse() debe llamar a self.navegar() y self.volar().
"""

class Terrestres(Vehiculos):
    def __init__(self, tipo, color):
        super().__init__(tipo, color)
    
    def rodar(self):
        return super().moverse(f"El {self.tipo} esta rodando")

class Acuáticos(Vehiculos):
    def __init__(self, tipo, color):
        super().__init__(tipo, color)
    
    def navegar(self):
        return super().moverse(f"El {self.tipo} esta navegando")

class Aéreos(Vehiculos):
    def __init__(self, tipo, color):
        super().__init__(tipo, color)
    
    def volar(self):
        return super().moverse(f"El {self.tipo} esta volando")

class Hibridos(Vehiculos):
    def __init__(self, tipo, color):
        super().__init__(tipo, color)

Carrera = [
    Terrestres("Auto", "Rojo"),
    Acuáticos("Submarino", "Verde"),
    Aéreos("Helicoptero", "Cafe"),
    Hibridos("Hidrocoptero", "Blanco y Negro")
]