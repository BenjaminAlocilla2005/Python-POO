class Pedido:
    def __init__(self, numero_mesa):
        """
        Inicializa un nuevo pedido
        :param numero_mesa: Número de la mesa
        """
        self.numero_mesa = numero_mesa
        self.platos = []  # Lista de tuplas (nombre, precio)
        self.total = 0.0
    
    def añadir_plato(self, nombre, precio):
        """
        Añade un plato al pedido
        :para nombre: Nombre del plato
        :para precio: Precio del plato
        """
        self.platos.append((nombre, precio))
        self._calcular_total()
    
    def _calcular_total(self):
        """Calcula el total sumando todos los precios de los platos"""
        self.total = sum(precio for _, precio in self.platos)
    
    def __len__(self):
        """
        Método mágico para contar el número de platos
        :return: Número de platos en el pedido
        """
        return len(self.platos)
    
    def __add__(self, otro_pedido):
        """
        Método mágico para combinar dos pedidos de la misma mesa
        :param otro_pedido: Otro objeto Pedido
        :return: Nuevo pedido combinado
        """
        if self.numero_mesa != otro_pedido.numero_mesa:
            raise ValueError("Solo se pueden combinar pedidos de la misma mesa")
        
        nuevo_pedido = Pedido(self.numero_mesa)
        nuevo_pedido.platos = self.platos + otro_pedido.platos
        nuevo_pedido._calcular_total()
        
        return nuevo_pedido
    
    def __str__(self):
        """Representación en string del pedido"""
        platos_str = "\n".join([f"  - {nombre}: ${precio:.2f}" for nombre, precio in self.platos])
        return f"Mesa {self.numero_mesa}:\n{platos_str}\nTotal: ${self.total:.2f}"
    
    def __del__(self):
        """
        Finalizador: se ejecuta cuando el objeto es eliminado
        """
        print(f"Pedido de la mesa {self.numero_mesa} ha sido completado y eliminado.")


# Ejemplo de uso y demostración
if __name__ == "__main__":
    # Crear un pedido
    pedido1 = Pedido(5)
    
    # Añadir platos
    pedido1.añadir_plato("Hamburguesa", 12.50)
    pedido1.añadir_plato("Papas fritas", 5.00)
    pedido1.añadir_plato("Refresco", 3.50)
    
    print("Pedido 1:")
    print(pedido1)
    print(f"Número de platos: {len(pedido1)}")
    print()
    
    # Crear otro pedido de la misma mesa
    pedido2 = Pedido(5)
    pedido2.añadir_plato("Postre", 6.00)
    pedido2.añadir_plato("Café", 2.50)
    
    print("Pedido 2:")
    print(pedido2)
    print()
    
    # Combinar pedidos
    pedido_combinado = pedido1 + pedido2
    print("Pedido combinado:")
    print(pedido_combinado)
    print(f"Número total de platos: {len(pedido_combinado)}")
    print()
    
    # Demostrar el finalizador
    print("Eliminando pedidos...")
    del pedido1
    del pedido2
    del pedido_combinado
