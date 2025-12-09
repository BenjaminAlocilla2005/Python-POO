class ArchivosMultimedia:
    def __init__(self, nombre, tamaño_mb):
        self.nombre = nombre
        self.tamaño_mb = tamaño_mb

    def obtener_peso(self):
        return self.tamaño_mb

class Reproducible(ArchivosMultimedia):
    def reproducir(self):
        pass

class Audio(Reproducible):
    def reproducir(self):
        print(f"Reproduciendo audio: {self.nombre}")

class Video(Reproducible):
    def reproducir(self):
        print(f"Reproduciendo video: {self.nombre}")

class Imagen(Reproducible):
    def reproducir(self):
        print(f"Mostrando imagen: {self.nombre}")

def reproductor_seguro(medio: Reproducible):
    medio.reproducir()

audio = Audio("Cancion.mp3", 5)
video = Video("video.mp4", 200)
imagen = Imagen("imagen.png", 2)

lista_reproducible = [audio, video]

for item in lista_reproducible:
    reproductor_seguro(item)