from multimedia_LSP import Audio, Video, Imagen

class BaseDeDatos:
    def __init__(self):
        self.datos = {}

    def obtener_peso(self):
        return 1500