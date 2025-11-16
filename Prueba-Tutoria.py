class Canciones:
    total_playlist = 0

    def __init__(self, usuario: str) -> None: # Crear una playlist vacia para el usuario y suma 1 a total_playlist
        self.usuario = usuario
        self.__canciones = []
        self.playlist = {}

        def agregar_cancion(self, nombre: str) -> None: # agregar
            nombre = self.__canciones
            dict.append(nombre)

        def eliminar_cancion(self, nombre: str) -> None: # elimina la cancion si existe
            if not nombre == "":
                raise ValueError("No puede borrarse una cancion que no este en la playlist")
            dict.remove(nombre)
            
        def __len__(self) -> int: # Devuelve la cantidad de canciones en la playlist
            return len(self.playlist)
        
        def __str__(self) -> int: # Devuelve una cadena con el formato "Playist de <usuario>"
            return f"Playlist de <{self.usuario}>: <> canciones"

# Instancias para probar el codigo
Usuario1 = Canciones("Jeremy", "The End")
Usuario2 = Canciones("Alice", "Du hast")

Usuario1.agregar_cancion()
Usuario1.eliminar_cancion()
Usuario1.__len__()
Usuario1.__str__()