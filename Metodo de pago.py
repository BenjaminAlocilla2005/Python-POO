"""
Contexto

Una empresa está desarrollando un sistema de gestión de pagos para su plataforma
de comercio electrónico. La plataforma admite diferentes métodos de pago, como
tarjetas de crédito, transferencias bancarias y pagos en efectivo. 

Cada método de pago tiene un comportamiento diferente. Por ejemplo:

1.Las tarjetas de crédito necesitan ser validadas antes de procesar el pago.

2.Las transferencias bancarias requieren un código de confirmación antes de
completar la transacción.

3.Los pagos en efectivo no necesitan validación ni confirmación, solo deben registrar
el monto recibido.

Actualmente, la clase base MetodoDePago() incluye un método procesar_pago() que
asume que todos los métodos de pago deben validarse antes de procesarse. 

Sin embargo, este diseño está causando problemas, ya que los pagos en efectivo no
necesitan validación, y algunos métodos de pago están lanzando excepciones
inesperadas
"""

class MetodoDePago():
    def __init__(self, credito, transferencias, efectivo):
        self.credito = credito
        self.validacion_tarjeta = True
        self.transferencias = transferencias
        self.efectivo = efectivo



        
    def procesar_pago(self):
        if self.validacion_tarjeta == True:
            print("La tarjeta es valida, puede comprar")
        else:
            print("La tarjeta no es valida")


comprador1 = MetodoDePago(4000, 5000, 2000)