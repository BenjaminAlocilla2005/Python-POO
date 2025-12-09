# GUIA RÁPIDA DE CLASES EN PYTHON
# Docente: Victor Saldivia Vera - Institución: Universidad de Los Lagos

class Persona():
    
    # Constructor de Clase
    def __init__(self, nombre, apellido, edad, altura, peso, nota1, nota2, nota3): # este método se ejecuta automáticamente al crear un nuevo objeto
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = float(altura)
        self.peso = float(peso)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        
    # Atributos (Características compartidas por todos los objetos de la clase)
    # nombre = "Cristina"
    # apellido = "Torres"
    # edad = 23
    
    # Métodos (Comportamientos)
    
    def hablar(self):
        print(f"{self.nombre} esta hablando")
        
    def caminar(self):
        print(f"{self.nombre} esta caminando")
        
    def cal_imc(self):
        imc = (self.peso / (self.altura**2))
        if imc < 18:
            print(f"Segun su imc, {self.nombre} {self.apellido} está delgado/a")
        elif imc >= 18 and imc < 25:
            print(f"segun su imc, {self.nombre} {self.apellido} tiene peso normal")
        else:
            print(f"segun su imc {self.nombre} {self.apellido} esta obeso/a")

    def calcular_promedio(self):
        p_final = (self.nota1 + self.nota2 + self.nota3)/3
        if p_final >= 4.0:
            print(f"{self.nombre} tiene {p_final}, por lo tanto ha aprobado")
        else:
            print(f"{self.nombre} tiene {p_final}, desafortunadamente ha reprobado")

persona1 = Persona("Cristina", "Torres", 23, 1.90, 50.1, 6.2, 4.0, 5.0) # instancia de la clase Persona -> crear un objeto de la clase Persona
persona2 = Persona("Benjamin", "Gomez", 20, 1.80, 60.4, 3.9, 2.9, 5.1)


print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad}")

persona1.hablar() # equivalente a Persona.hablar(persona1)
persona1.caminar() # se puede crear múltiples objetos de la misma clase
persona1.cal_imc() # para calcular del imc
persona1.calcular_promedio() # calcular el promedio
        