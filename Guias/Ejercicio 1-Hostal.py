class ReservaHostal:
    def __init__(self, n_cliente, f_entrada, f_salida, N_habitacion):
        self.n_cliente = n_cliente
        self.N_habitacion = N_habitacion
        self.f_entrada = f_entrada
        self.f_salida = f_salida

    def calcular_duracion_estadia(self):
        entrada = list(map(int, self.f_entrada.split("-")))
        salida = list(map(int, self.f_salida.split("-")))
        dias = (salida[0] - entrada[0]) * 365 + (salida[1] - entrada[1]) * 30 + (salida[2] - entrada[2])
        return dias

    def cambiar_fecha_salida(self, nueva_fecha):
        self.f_entrada = nueva_fecha
        print(f"Nueva fecha de salida: {self.f_salida}")

    def __str__(self):
        return (f"Reserva de: {self.n_cliente} - "
                f"Habitacion: {self.N_habitacion} - "
                f"Entrada: {self.f_entrada} - "
                f"Salida: {self.f_salida} - "
                f"Duración: {self.calcular_duracion_estadia()} noches.")

    def __del__(self):
        print(f"La reserva de {self.n_cliente} para la habitación {self.N_habitacion} fue cancelada")
        print("")

reserva1 = ReservaHostal("Jennifer", "2024-03-21", "2024-04-26", 102)
reserva2 = ReservaHostal("Billy", "2024-06-12", "2024-06-15", 105)
print(reserva1)
reserva1.cambiar_fecha_salida("2024-08-20")
print(reserva1)
del reserva1