class Producto:
    def __init__(self, nombre, precio, cantidad, codigo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo
        self.historial_stock = [f"Creación: {cantidad} unidades"]
    
    def actualizar_stock(self, cambio, motivo=""):
        if self.cantidad + cambio < 0:
            print(f"Error: No hay suficiente stock de {self.nombre}")
            return False
        
        self.cantidad += cambio
        registro = f"Cambio: {cambio:+d} | Nuevo stock: {self.cantidad}"
        if motivo:
            registro += f" | Motivo: {motivo}"
        self.historial_stock.append(registro)
        return True
    
    def valor_total(self):
        return self.precio * self.cantidad
    
    def __str__(self):
        """Representación en texto del producto"""
        return (f"Producto: {self.nombre} | "
                f"Código: {self.codigo} | "
                f"Precio: ${self.precio:.2f} | "
                f"Stock: {self.cantidad} | "
                f"Valor: ${self.valor_total():.2f}")

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario: {codigo: producto}
    
    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print(f"Error: El código {producto.codigo} ya existe")
            return False
        
        self.productos[producto.codigo] = producto
        print(f"Producto '{producto.nombre}' agregado al inventario")
        return True
    
    def actualizar_stock(self, codigo, cambio, motivo=""):
        if codigo not in self.productos:
            print(f"Error: Producto con código {codigo} no encontrado")
            return False
        
        return self.productos[codigo].actualizar_stock(cambio, motivo)
    
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío")
            return
        
        print("\n" + "="*60)
        print("INVENTARIO COMPLETO")
        print("="*60)
        for producto in self.productos.values():
            print(producto)
        print("="*60)
    
    def valor_total_inventario(self):
        total = sum(producto.valor_total() for producto in self.productos.values())
        return total
    
    def mostrar_historial_producto(self, codigo):
        if codigo not in self.productos:
            print(f"Error: Producto con código {codigo} no encontrado")
            return
        
        producto = self.productos[codigo]
        print(f"\nHistorial de '{producto.nombre}' ({codigo}):")
        print("-" * 40)
        for registro in producto.historial_stock:
            print(f"• {registro}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear inventario
    mi_inventario = Inventario()
    
    # Crear productos
    producto1 = Producto("Laptop HP", 1200.00, 10, "LP001")
    producto2 = Producto("Mouse Inalámbrico", 25.50, 50, "MS002")
    producto3 = Producto("Teclado Mecánico", 89.99, 15, "TK003")
    
    # Agregar productos al inventario
    mi_inventario.agregar_producto(producto1)
    mi_inventario.agregar_producto(producto2)
    mi_inventario.agregar_producto(producto3)
    
    # Actualizar stocks
    mi_inventario.actualizar_stock("LP001", -2, "Venta a cliente")
    mi_inventario.actualizar_stock("MS002", 10, "Compra a proveedor")
    mi_inventario.actualizar_stock("MS002", -5, "Venta minorista")
    mi_inventario.actualizar_stock("TK003", -3, "Venta online")
    
    # Mostrar inventario completo
    mi_inventario.mostrar_inventario()
    
    # Mostrar valor total del inventario
    total = mi_inventario.valor_total_inventario()
    print(f"\nValor total del inventario: ${total:.2f}")
    
    # Mostrar historial de un producto
    mi_inventario.mostrar_historial_producto("MS002")