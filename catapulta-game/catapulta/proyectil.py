class Proyectil:
    def __init__(self, peso, tipo):
        self.peso = peso
        self.tipo = tipo

    def calcular_trayectoria(self, angulo, velocidad):
        # Método para calcular la trayectoria del proyectil
        # Aquí se puede implementar la fórmula de la física para la trayectoria
        # Por simplicidad, solo se devuelve un valor ficticio
        return (angulo, velocidad)

    def __str__(self):
        return f"Proyectil de tipo {self.tipo} con peso {self.peso} kg"