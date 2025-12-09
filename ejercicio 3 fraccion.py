class Fraccion():
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominadorr no debe ser cero")
        self.numerador = numerador
        self.denominador = denominador

        # Simplificar la fracción al crearla
        mcd = self._mcd(numerador, denominador)
        self.numerador = numerador // mcd
        self.denominador = denominador // mcd
        
        # Asegurar que el signo esté en el numerador
        if self.denominador < 0:
            self.numerador = -self.numerador
            self.denominador = -self.denominador
    
    def _mcd(self, a, b):
        """Calcula el máximo común divisor usando el algoritmo de Euclides"""
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a
    
    def __str__(self):
        """Devuelve la fracción como una representación de cadena"""
        if self.denominador == 1:
            return str(self.numerador)
        return f"{self.numerador}/{self.denominador}"
    

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    def __add__(self, other):
        new_d = self.denominador * other.denominador
        new_n = (self.numerador * other.denominador +
                 other.numerador * self.denominador)
        return Fraccion(new_n, new_d)
    def __mul__(self, other):
        new_d = self.denominador * other.denominador
        new_n = (self.numerador * other.denominador +
                 other.numerador * self.denominador)
        return Fraccion(new_n, new_d)

fraccion1 = Fraccion(1,2)
fraccion2 = Fraccion(3,4)
fraccion3 = Fraccion(2,4)

suma = fraccion1 + fraccion2
multiplicacion = fraccion1 * fraccion2
