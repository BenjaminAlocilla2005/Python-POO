# La primera clase que se usa de base principal
class Contenido:
    def __init__(self, titulo=str, año=int):
        self.titulo = titulo
        self.año = año

    # Metodo generico que muestra el titulo y el año
    def mostar_detalle(self):
        print(f"Titulo: {self.titulo}")
        print(f"Año: {self.año}")

# Segunda clase que sera una normal y define la interfaz para reproducir
class Reproducible:
    # Metodo generico que servira para reproducir
    def reproducir():
        pass

class Calificable:
    def __init__(self, rating=float):
        self.rating = rating

    # Metodo generico que servira para actualizar el rating e imprime la nueva calificación
    def calificar_puntuacion(self):
        return self.rating
    
# Dependiendo de lo que se pida se empieza a usar la herencia simple o multiple
class Pelicula(Contenido, Reproducible):
    def __init__(self, titulo=str, año=int, duracion_min=int):
        super().__init__(titulo, año)
        self.duracion = duracion_min

    def mostar_detalle(self):
        print(f"Titulo: {self.titulo}")
        print(f"Año: {self.año}")
        print(f"Duracion en minutos: {self.duracion}")


    def reproducir(self):
        print(f"La pelicula de nombre {self.titulo} se esta reproduciendo")

class Documental(Contenido):
    def __init__(self, titulo=str, año=int, tema=str):
        super().__init__(titulo, año)
        self.tema = tema

    def mostar_detalle(self):
        print(f"Titulo: {self.titulo}")
        print(f"Año: {self.año}")
        print(f"Tema: {self.tema}")

class Miniserie(Contenido, Reproducible, Calificable):
    def __init__(self, titulo=str, año=int, rating=float, num_capitulos=int):
        super().__init__(titulo, año, rating)
        self.N_capitulos = num_capitulos

    def reproducir(self):
        print(f"La miniserie {self.titulo} se está transmitiendo")

    def mostar_detalle(self):
        print(f"Titulo: {self.titulo}")
        print(f"Año: {self.año}")
        print(f"Numero de capitulos: {self.N_capitulos}")

def lista_de_reproduccion(lista_contenidos):
    # funcion que sera importante para el uso de reproducir
    try:
        reproduccion = lista_contenidos.reproducir()
        nombre_contenido = lista_contenidos.__class__.__name__
        print(f"")
    # por sea caso carece de reproducir
    except AttributeError:
        print("Error: el contenido no tiene la funcion reproducir()")

if __name__ == "__main__":
    # Crear instancias 
    movie = Pelicula("Sonic 3", 2024, 120)
    document = Documental("Gatos", 1992, "Animales")
    miniserie = Miniserie("Jojo's Bizarre Adventure: Stardust Crusaders", 2014, 8.9, 26)
    
    # Lista con todas las figuras
    contenidos = [movie, document, miniserie] 
    # Poniendo la funcion a prueba
    for lista_contenidos in contenidos:
        lista_de_reproduccion(lista_contenidos)

    print("=== Probando funciones de las clases ===\n")
    # Pelicula
    movie.mostar_detalle()
    movie.reproducir()

    # Documental
    document.mostar_detalle()

    # Miniserie
    miniserie.mostar_detalle()
    miniserie.reproducir()
    miniserie.calificar_puntuacion(9.1)

    # Probando de forma individual la funcion lista_de_reproduccion(lista_contenidos)
    print("=== Uso individual de la funcion ===\n")
    lista_de_reproduccion(movie)
    lista_de_reproduccion(miniserie)