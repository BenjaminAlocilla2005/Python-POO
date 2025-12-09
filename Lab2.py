class Productos:
    # Variables Globales
    IVA = 0.19

    PRODUCTOS_CREADOS += 0
    Categorias_validas = {"Abarrotes","Bebidas","Carnes"}

    def __init__(self, nombre:str, categoria:str, precio_base:float):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio_base = precio_base
        self.descuento = 0.0

        Productos.PRODUCTOS_CREADOS +=1

    def __str__(self) -> str:
        return f"Nombre = {self.__nombre} Categoria = {self.__categoria} Precio Base = {self.__precio_base} Descuento = {self.descuento}"
    
    @staticmethod
    def es_categoria_valida(categoria:str):
        return categoria in Productos.Categorias_validas
    
    @classmethod
    def total_Productos_Creados(cls):
        return cls.PRODUCTOS_CREADOS
    
    def aplicar_descuento(self, porcentaje:float):
        porcentaje = self.precio_base * IVA
        print(porcentaje)

producto1 = Productos("Sprite", "Bebidas", 200)
producto2 = Productos("Chuleta", "Carnes", 600)
producto1.es_categoria_valida()
producto1.total_Productos_Creados()
producto1.aplicar_descuento(10)
print(producto1)
