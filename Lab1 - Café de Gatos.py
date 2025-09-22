class Gato:
    ESTADOS_SALUD = ["Saludable", "En observación", "Enfermo"]
    
    def __init__(self, nombre, edad, id_mascota):
        # Atributos privados (encapsulación)
        self.nombre = nombre
        self.edad = int(edad)
        self.id_mascota = id_mascota  # Nuevo: ID de registro oficial
        self.nivel_energia = 100  # De 0 a 100 (numérico ahora)
        self.nivel_hambre = 0     # De 0 a 100 (numérico ahora)
        self.estado_salud = "Saludable"  # Nuevo: estado de salud
        self.historial_medico = []  # Nuevo: historial médico privado
        
        # Registrar en el historial
        self.__actualizar_historial(f"Gato creado: {nombre}, ID: {id_mascota}")

    def gato_jugando(self, minutos):
        if self.nivel_energia is self.nivel_energia >= 20:
            self.nivel_energia -= minutos * 0.5
            self.nivel_hambre += minutos * 0.8
            self.__actualizar_historial(f"Jugó por {minutos} minutos")
            self.__actualizar_estado_salud()  # Actualizar estado después de jugar
            return f"{self.nombre} jugó felizmente por {minutos} minutos"
        else:
            return f"{self.nombre} está muy cansado para jugar"
 
    def alimentar_gato(self, comida):
        """Alimenta al gato, reduciendo hambre y aumentando energía"""
        if self.nivel_hambre > 0:
            self.nivel_hambre = max(0, self.nivel_hambre - 30)
            self.nivel_energia = min(100, self.nivel_energia + 15)
            self.__actualizar_historial(f"Se alimentó con {comida}")
            self.__actualizar_estado_salud()  # Actualizar estado después de comer
            return f"{self.nombre} comió {comida}"
        else:
            return f"{self.nombre} no tiene hambre"
    
    def mostrar_info(self):
        """Muestra información básica del gato"""
        return (f"Gato: {self.nombre} - "
                f"Edad: {self.edad} años - "
                f"Energía: {self.__obtener_nivel_energia_texto()} - "
                f"Hambre: {self.__obtener_nivel_hambre_texto()} - "
                f"Salud: {self.estado_salud}")
    
    def mostrar_historial_medico(self):
        """Muestra el historial médico del gato"""
        historial = f"Historial médico de {self.nombre}:\n"
        for evento in self.historial_medico:
            historial += f"- {evento}\n"
        return historial
    
    # Getters públicos para acceder a atributos privados
    def get_nombre(self):
        return self.nombre
        
    def get_id_mascota(self):
        return self.id_mascota
        
    def get_estado_salud(self):
        return self.estado_salud
    
    # Métodos privados (encapsulación)
    def __actualizar_estado_salud(self):
        """Actualiza automáticamente el estado de salud basado en energía y hambre"""
        estado_anterior = self.estado_salud
        
        if self.nivel_energia < 20 or self.nivel_hambre > 80:
            self.estado_salud = "Enfermo"
        elif self.nivel_energia < 50 or self.nivel_hambre > 50:
            self.estado_salud = "En observación"
        else:
            self.estado_salud = "Saludable"
        
        if estado_anterior != self.estado_salud:
            self.__actualizar_historial(f"Estado de salud cambiado: {estado_anterior} -> {self.estado_salud}")

    
    def __actualizar_historial(self, evento):
        """Agrega un evento al historial médico con timestamp"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.historial_medico.append(f"[{timestamp}] {evento}")
    

    def __obtener_nivel_energia_texto(self):
        """Convierte el nivel numérico de energía a texto"""
        if self.nivel_energia >= 80:
            return "Muy Alto"
        elif self.nivel_energia >= 60:
            return "Alto"
        elif self.nivel_energia >= 40:
            return "Normal"
        elif self.nivel_energia >= 20:
            return "Bajo"
        else:
            return "Cansado"

    def __del__(self):
        print(f"El gato de nombre {self.nombre} se ha retirado del café")

    
    def __obtener_nivel_hambre_texto(self):
        """Convierte el nivel numérico de hambre a texto"""
        if self.nivel_hambre >= 80:
            return "Muy hambriento"
        elif self.nivel_hambre >= 60:
            return "Hambriento"
        elif self.nivel_hambre >= 40:
            return "Regular"
        elif self.nivel_hambre >= 20:
            return "Poco hambre"
        else:
            return "Lleno"
    
    def __str__(self):
        return self.mostrar_info()
    
    def __del__(self):
        print(f"El gato {self.nombre} se ha retirado del café")

class Espacio:
    def __init__(self, nombre, espacio, capacidad):
        # Atributos públicos
        self.nombre = nombre
        self.tipo_espacio = espacio
        
        # Atributos privados (encapsulación)
        self.capacidad = capacidad
        self.gatos_presentes = []
        self.contador_gatos = 0
    

    # Métodos públicos
    def agregar_gato(self, gato):
        """Agrega un gato al espacio si hay capacidad y está saludable"""
        if not isinstance(gato, Gato):
            return "Error: Solo se pueden agregar objetos Gato"
        
        # Verificar si el gato está inscrito (tiene ID) y está saludable
        if gato.get_id_mascota() is None:
            return f"{gato.get_nombre()} no está inscrito en el registro de mascotas"
        
        if gato.get_estado_salud() == "Enfermo":
            return f"No se puede agregar {gato.get_nombre()} porque está enfermo"
        
        if self.contador_gatos < self.capacidad:
            self.gatos_presentes.append(gato)
            self.contador_gatos += 1
            self.__actualizar_contador()
            return f"{gato.get_nombre()} agregado al espacio {self.nombre}"
        else:
            return f"Espacio {self.nombre} lleno. No se puede agregar más gatos"
        

    def remover_gato(self, id_mascota):
    #Remueve un gato del espacio por su ID
        for i, gato in enumerate(self.gatos_presentes):
            if gato.get_id_mascota() == id_mascota:
                gato_removido = self.gatos_presentes.pop(i)
                self.contador_gatos -= 1
                self.__actualizar_contador()
                return f"{gato_removido.get_nombre()} removido del espacio {self.nombre}"
        return "Gato no encontrado en este espacio"
    
    
    def generar_reporte(self):
        """Genera un reporte del espacio con información de los gatos"""
        reporte = f"=== REPORTE DEL ESPACIO: {self.nombre} ===\n"
        reporte += f"Tipo: {self.tipo_espacio}\n"
        reporte += f"Capacidad: {self.__contador_gatos}/{self.capacidad}\n"
        reporte += "Gatos presentes:\n"
        
        for gato in self.gatos_presentes:
            reporte += f"- {gato.mostrar_info()}\n"
        
        return reporte

    # Métodos privados
    def __actualizar_contador(self):
        """Actualiza el contador interno de gatos"""
        self.__contador_gatos = len(self.gatos_presentes)
    
    def __str__(self):
        return f"Espacio: {self.nombre} - Gatos: {self.__contador_gatos}/{self.capacidad}"


# Demostración del sistema
if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN - CAFÉ DE GATOS ===\n")
    
    # Crear espacios
    salon_principal = Espacio("Salón Principal", "Mediano", 10)
    area_juegos = Espacio("Área de Juegos", "Grande", 20)
    comedor = Espacio("Comedor", "Pequeño", 4)
    
    # Crear gatos (ahora con ID de registro)
    gato1 = Gato("Jeremy", 10, "M001")
    gato2 = Gato("Alice", 6, "M002")
    gato3 = Gato("William", 8, "M003")

    print("1. Información de gatos creados:")
    print(gato1.mostrar_info())
    print(gato2.mostrar_info())
    print(gato3.mostrar_info())
    print()
    
    print("2. Interacciones con los gatos:")
    print(gato1.gato_jugando(30))
    print(gato2.alimentar_gato("atún"))
    print(gato3.gato_jugando(45))
    print()
    
    print("3. Agregando gatos a espacios:")
    print(salon_principal.agregar_gato(gato1))
    print(salon_principal.agregar_gato(gato2))
    print(area_juegos.agregar_gato(gato3))
    print()

    print("4. Reportes de espacios:")
    print(salon_principal.generar_reporte())
    print(area_juegos.generar_reporte())
    print()
    
    print("5. Historial médico de Jeremy:")
    print(gato1.mostrar_historial_medico())
    
    # Simular cambio de estado de salud por agotamiento
    print("6. Simulando cambio de estado por agotamiento:")
    for _ in range(4):
        gato1.gato_jugando(30)
    print(f"Estado de salud actual: {gato1.get_estado_salud()}")
    print(gato1.mostrar_historial_medico())