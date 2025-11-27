import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio **2

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2

class Trapecio:
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
    
    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

class Pentagono_Regular:
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        # Fórmula del área de un pentágono regular: (perímetro * apotema) / 2
        perimetro = 5 * self.lado
        # Cálculo del apotema: apotema = lado / (2 * tan(36°))
        apotema = self.lado / (2 * math.tan(math.radians(36)))
        return (perimetro * apotema) / 2
    
def mostrar_area(figura):
    """
    Función que utiliza Duck Typing - no le importa el tipo exacto de la figura,
    solo que tenga el método calcular_area()
    """
    try:
        area = figura.calcular_area()
        nombre_figura = figura.__class__.__name__
        print(f"El área del {nombre_figura} es: {area:.2f}")
    except AttributeError:
        print("Error: La figura proporcionada no tiene el método calcular_area()")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de diferentes figuras
    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)
    triangulo = Triangulo(3, 8)
    cuadrado = Cuadrado(5)
    trapecio = Trapecio(8, 4, 5)
    pentagono = Pentagono_Regular(6)
    
    # Lista con todas las figuras
    figuras = [circulo, rectangulo, triangulo, cuadrado, trapecio, pentagono]
    
    print("=== CÁLCULO DE ÁREAS USANDO DUCK TYPING ===\n")
    
    # Calcular y mostrar áreas usando la función mostrar_area
    for figura in figuras:
        mostrar_area(figura)
    
    print("\n" + "="*50)
    
    # También podemos usar la función individualmente
    print("== Uso individual de la función ==\n")
    mostrar_area(circulo)
    mostrar_area(rectangulo)