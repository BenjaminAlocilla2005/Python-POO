class Animal:
    def walk(self):
        print("El animal esta caminando")

class LightWeightAnimal(Animal):
    def jump(self):
        print("El animal esta saltando")

class Dog(LightWeightAnimal):
    pass

class Elephant(Animal):
    pass

def jump_hole(animal: LightWeightAnimal):
    animal.walk()
    animal.jump()
    animal.walk()

perro = Dog()
elefante = Elephant()

elefante.walk()
perro.jump()