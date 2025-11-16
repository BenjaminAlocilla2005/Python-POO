class CuentaBancaria:
    def __init__(self, titular:str, saldo:float = 0):
        self.saldo = saldo
        self.titular = titular

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Has depositado {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("la cantidad debe ser mayor a 0")
    def retirar(self, cantidad):
            if cantidad > self.saldo:
                print(f"No tienes dinero suficiente, saldo disponible {self.saldo}")
            else:
                self.saldo -= cantidad
                print(f"Retiro exitoso, saldo disponible {self.saldo}")

    def mostrar(self):
        print(f"Saldo disponible {self.saldo}")


persona = input("Ingresa tu nombre: ")
titular = CuentaBancaria(persona)

while True:
    print("//MENU//")
    print("1. Depositar 2. Retirar 3. Mostrar 4. Salir")
    opcion = input("Elije una opcion (número): ")

    if opcion == 1:
        cantidad = float(input("Cuanto dinero deseas depositar?: "))
        titular.depositar(cantidad)

    elif opcion == 2:
        cantidad = float(input("Que cantidad deseas retirar?: "))
    
    elif opcion == 3:
        titular.mostrar()

    if opcion == 4:
        print(f"{persona} Gracias por usar nuestro sistema.")
        break