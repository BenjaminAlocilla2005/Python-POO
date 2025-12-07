class Libro:
    def __init__(self, titulo, autor, año_publicacion, cantidad_disponible):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.cantidad_disponible = cantidad_disponible

    def __str__(self):
        return(f"'{self.titulo}' por {self.autor} ({self.año_publicacion}) - "
               f"Disponibles: {self.cantidad_disponible}")
    
    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.cantidad_disponible = nueva_cantidad
            return True
        return False
    
    def prestar_libro(self):
        if self.cantidad_disponible > 0:
            self.cantidad_disponible -=1
            return True
        return False
    
    def devolver_libro(self):
        self.cantidad_disponible += 1
        return True
    
    def agregar_libro(self, libro):
        if libro.titulo in self.libros:
            print(f"❌ El libro '{libro.titulo}' ya existe.")
            return False
        
        self.libros[libro.titulo] = libro
        print(f"✅ El libro '{libro.titulo}' ha sido agregado con exito.")
        return True
    
    def buscar_libro_por_titulo(self, titulo):
        return self.libros.get(titulo)
    
    def buscar_libros_por_palabra_clave(self, palabra_clave):
        resultados = []
        palabra_clave = palabra_clave.lower()  # Búsqueda insensible a mayúsculas
    
        for titulo, libro in self.libros.items():
            if palabra_clave in titulo.lower():
                resultados.append(libro)
    
        return resultados
    
    def actualizar_libro(self, titulo, nuevo_autor=None, nuevo_año=None, nueva_cantidad=None):
        libro = self.buscar_libro_por_titulo(titulo)
    
        if not libro:
            print(f"❌ Libro '{titulo}' no encontrado.")
            return False
    
        if nuevo_autor:
            libro.autor = nuevo_autor
    
        if nuevo_año:
            libro.año_publicacion = nuevo_año
    
        if nueva_cantidad is not None:  # Puede ser 0, por eso verifica None
            if libro.actualizar_cantidad(nueva_cantidad):
                print(f"📊 Cantidad actualizada para '{titulo}'.")
            else:
                print("❌ Cantidad no válida.")
    
        print(f"✅ Libro '{titulo}' actualizado exitosamente.")
        return True
    
    def eliminar_libro(self, titulo):

        if titulo in self.libros:
            del self.libros[titulo]  # Elimina la entrada del diccionario
            print(f"✅ Libro '{titulo}' eliminado exitosamente.")
            return True
        else:
            print(f"❌ Libro '{titulo}' no encontrado.")
            return False
        
    def listar_libros(self):

        if not self.libros:
            print("📭 La biblioteca está vacía.")
            return
    
        print("\n=== 📚 LIBROS EN LA BIBLIOTECA ===")
        for i, (titulo, libro) in enumerate(self.libros.items(), 1):
            print(f"{i}. {libro}")  # Llama automáticamente a libro.__str__()

    def prestar_libro(self, titulo):
        libro = self.buscar_libro_por_titulo(titulo)
    
        if not libro:
            print(f"❌ Libro '{titulo}' no encontrado.")
            return False
    
        if libro.prestar_libro():
            print(f"📖 Libro '{titulo}' prestado exitosamente.")
            return True
        else:
            print(f"⏳ No hay ejemplares disponibles de '{titulo}'.")
            return False
        
    def prestar_libro(self, titulo):
        libro = self.buscar_libro_por_titulo(titulo)
    
        if not libro:
            print(f"❌ Libro '{titulo}' no encontrado.")
            return False
    
        if libro.prestar_libro():
            print(f"📖 Libro '{titulo}' prestado exitosamente.")
            return True
        else:
            print(f"⏳ No hay ejemplares disponibles de '{titulo}'.")
            return False

    def devolver_libro(self, titulo):
        libro = self.buscar_libro_por_titulo(titulo)
    
        if not libro:
            print(f"❌ Libro '{titulo}' no encontrado.")
            return False
    
        libro.devolver_libro()
        print(f"📗 Libro '{titulo}' devuelto exitosamente.")
        return True
    
    
    def obtener_cantidad_total_libros(self):
 
        total = sum(libro.cantidad_disponible for libro in self.libros.values())
        return total
    
