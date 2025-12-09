class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        assert monto > 0, "El monto debe ser positivo"
        self.__saldo += monto

    def retirar(self, monto):
        assert monto <= self.__saldo, "Saldo insuficiente"
        self.__saldo -= monto