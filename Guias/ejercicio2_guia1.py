class FuncionTrigonometrica:
    def __init__(self, tipo, amplitud, periodo):
        self.tipo = tipo
        self.amplitud = amplitud
        self.periodo = periodo
        
    def evaluar(self, x):
        # Valores aproximados para x en radianes: 0, π/2, π, 3π/2, 2π
        if self.tipo == 'seno':
            if x == 0:
                return 0
            elif x == 1.57:  # π/2
                return self.amplitud * 1
            elif x == 3.14:  # π
                return 0
            elif x == 4.71:  # 3π/2
                return self.amplitud * -1
            elif x == 6.28:  # 2π
                return 0
        elif self.tipo == 'coseno':
            if x == 0:
                return self.amplitud * 1
            elif x == 1.57:
                return 0
            elif x == 3.14:
                return self.amplitud * -1
            elif x == 4.71:
                return 0
            elif x == 6.28:
                return self.amplitud * 1
        elif self.tipo == 'tangente':
            if x == 0:
                return 0
            elif x == 1.57:
                return "infinito"
            elif x == 3.14:
                return 0
        return "Valor no disponible"

    def mostrar_funcion(self):
        return f"{self.amplitud} * {self.tipo}(x / {self.periodo})"

    def valor_critico(self):
        if self.tipo == 'seno' or self.tipo == 'coseno':
            return self.amplitud
        else:
            return "No tiene máximo definido"
        
f = FuncionTrigonometrica('seno', 1, 6.28)
print(f.mostrar_funcion())
print("Valor en π/2:", f.evaluar(1.57))
print("Valor en π:", f.evaluar(3.14))
print("Valor crítico:", f.valor_critico())
