'''Desarrollar un sistema de gestión de una biblioteca donde se pueda agregar y administrar 
libros. Cada libro tiene un título, autor, año de publicación, y cantidad disponible del libro. La 
biblioteca es responsable de gestionar los libros y permitir la búsqueda de libros por título. 
Considerar crear la clase Biblioteca que debe manejar múltiples instancias de la clase Libro 
utilizando un diccionario. Los libros se pueden agregar, buscar y actualizar '''

#crear 2 clase, una para Libro y otra para Biblioteca
 #crear contructor de clase Libro
class Libro:
    def __init__ (self, título, autor, año, cantidad):
        self.título = título
        self.autor = autor
        self.año = int(año) 
        self.cantidad = cantidad

    #crea los métodos de la clase
    def actulizar_cantidad (self,cambio): # agregar libro 
        self.cantidad += cambio

    def __str__(self): #mostrar que libro tengo y sus caracteristicas
        return f"{self.título} por {self.autor}, ({self.año}) - Disponible: {self.cantidad}"
    

#crear segundo contructor de clase
class Biblioteca:

    def __init__(self):
        self.libros = {} #diccionario para guardar los libros 

    def agregar_libro (self,libro): #agregar un libro a mi diccionario de biblioteca
        self.libros[libro,"título"] = libro

    def buscar_libro(self,titulo):
        return self.libros.get(titulo,"libro no encontrado") #get(rerorre el dic{} y busca la claves(1985))
    
    def mostrar_libros(self): 
        for libro in self.libros.values(): #Para(for) buscar libro in (en)mi dic{} libros. values(muestra el
            # valor de mi dicionario)

          print(libro)

#mis objetos 
libro1=Libro("El Quijote de la Mancha", "Miguel de Cervantes",1603,3) #titulo de mi libro, autor, año y cantidad disponible
libro2=Libro("1984", "George Orwell", 1949,5)

biblio = Biblioteca ()
biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)

biblio.mostrar_libros()
print(biblio.buscar_libro("1984"))
