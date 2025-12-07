class FuncionTrigonometrica:
    def __init__(self, seno, coseno, tangente, amplitud, periodo):
        self.seno = seno
        self.coseno = coseno
        self.tangente = tangente
        self.amplitud = amplitud
        self.periodo = periodo
    
    def evaluar(self,x):
        argumento = ()

""""
● Atributos:

○ Tipo de función (seno, coseno, tangente)

○ Amplitud y periodo de la función.

● Métodos:

○ Crear un método que evalúe la función trigonométrica en un valor x (en
radianes)

○ Crear un método que grafique la función en un intervalo de valores.

○ Crear un método mágico que devuelva una representación de texto de la
función trigonométrica.

○ Crear un método que devuelva un valor crítico de la función (por ejemplo, los
máximos o mínimos para seno y coseno).
"""