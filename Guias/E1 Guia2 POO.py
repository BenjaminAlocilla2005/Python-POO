class AgendaTareas:
    __tareas = []        # Privado: para evitar modificación directa desde fuera
    __contador = 0       # Privado: variable de clase, control interno

    def agregar(self, titulo: str) -> int:
        # Incrementa contador, agrega tarea con ID = contador, devuelve ID
        return titulo

    def marcar_hecha(self, id: int) -> None:
        # Busca tarea por ID y cambia estado a True
        id
    def listar_pendientes(self) -> list:
        # Retorna títulos de tareas no hechas

    def __len__(self) -> int:
        # Retorna cantidad total de tareas

    @classmethod
    def total_creadas(cls) -> int:
        # Retorna el valor de __contador


agenda = AgendaTareas()
id1 = agenda.agregar("Estudiar POO")
id2 = agenda.agregar("Hacer ejercicio")
agenda.marcar_hecha(id1)
print(agenda.listar_pendientes())  # Salida: ['Hacer ejercicio']
print(len(agenda))                 # Salida: 2