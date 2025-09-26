class Libro:
    _tasa_descuento = 0.05

    def __init__(self, titulo, autor, valor, cantidad_disponible):
        self.__titulo = titulo
        self.__autor = autor
        self.__valor = valor
        self.cantidad_disponible = cantidad_disponible

        assert valor > 0, "El valor de supone debe que ser mayor a 0" # Usar una aserción para evitar que el precio sea negativo
    
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo,str) and nuevo_titulo.strip(): # Verifica si es cadena de texto
            self.__titulo = nuevo_titulo
        else:
            print("El titulo no debe quedar vacio")

    def get_valor(self):
        return self.__valor
    
    def set_valor(self, nuevo_valor):
        if isinstance(nuevo_valor, (int, float)) and nuevo_valor > 0:
            self.__valor = nuevo_valor
        else:
            print("El valor no debe ser ni 0 ni negativo")

    def mostrar_info(self):
        print(f"Título: {self.__titulo}, Autor: {self.__autor}, Valor: ${self.__valor:,}, Disponibles: {self.cantidad_disponible}")

    def obtener_precio(self):
        return self.__valor

    @staticmethod
    def calcular_precio(valor):
        return valor * Libro._tasa_descuento
    
class Libreria:
    def __init__(self):
        self.catalogo = {} # Agregamos un Diccionario: la clave es el titulo y el valor es el coste del libro

    def agregar_libro(self, libro):
        titulo = libro.get_titulo()
        if titulo in self.catalogo:
            print(f"El libro ya esta")
        else:
            self.catalogo[titulo] = libro
            print(f"El libro ha sido agregado: {titulo}")

    def mostrar_catalogo(self):
        print("Catalogo de la libreria:")
        for libro in self.catalogo.values():
            libro.mostrar_info()

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.catalogo.values() if titulo.lower() in libro.get_titulo().lower()]
    
class Carrito:
    def __init__(self):
        self.items = []

    def agregar_libro(self, libro):
        self.items.append(libro)
        print(f"Libro añadido al carrito: {libro.get_titulo()}")

    def calcular_total(self):
        return sum(libro.get_valor() for libro in self.items)
    
    def calcular_total_con_descuentos(self):
        total = self.calcular_total()
        cantidad = len(self.items)

        if cantidad >= 3:
            descuento = min((cantidad - 2) * 0.05, 0.30)
            total_descuento = total * (1 - descuento)
            print(f" Descuento aplicado: {descuento*100:.0f}%")
            return total_descuento
        else:
            print(" No hay descuento aplicado.")
            return total

    def mostrar_carrito(self):
        print("Carrito de compras:")
        for libro in self.items:
            libro.mostrar_info()
        print(f"Total a pagar: ${self.calcular_total():,} Pesos")

# Creando  los objetos

categoria = Libreria()

libro1 = Libro("El cuento de Perico el conejo", "Beatrix Potter", 6990, 31)
libro2 = Libro("Juan Salvador Gaviota", "Richard Bach", 8990, 20)
libro3 = Libro("La oruga muy hambrienta", "Eric Carle", 6990, 41)
libro4 = Libro("Un mensaje a García", "Elbert Hubbard", 5990, 10)
libro5 = Libro("Matar a un ruiseñor", "Harper Lee", 9990, 40)

categoria.agregar_libro(libro1)
categoria.agregar_libro(libro2)
categoria.agregar_libro(libro3)
categoria.agregar_libro(libro4)
categoria.agregar_libro(libro5)

print("")
categoria.mostrar_catalogo()

print("")
carrito = Carrito()
carrito.agregar_libro(libro1)
carrito.agregar_libro(libro3)
carrito.agregar_libro(libro5)

print("")
carrito.mostrar_carrito()
print(f"Total con descuento: ${carrito.calcular_total_con_descuentos():,}")

# Ejemplo de búsqueda
print("")
resultados = categoria.buscar_por_titulo("gaviota")
print("Resultados de búsqueda:")
for libro in resultados:
    libro.mostrar_info()


