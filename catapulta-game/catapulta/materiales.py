class Material:
    def __init__(self, nombre, resistencia, peso):
        self.nombre = nombre
        self.resistencia = resistencia
        self.peso = peso

    def obtener_informacion(self):
        return f"Material: {self.nombre}, Resistencia: {self.resistencia}, Peso: {self.peso}"

# Definición de materiales disponibles
palos = Material("Palos", resistencia=5, peso=2)
gomas = Material("Gomas", resistencia=3, peso=1)
tapones = Material("Tapones", resistencia=2, peso=0.5)
corchos = Material("Corchos", resistencia=1, peso=0.2)
pegamento = Material("Pegamento", resistencia=4, peso=0.1)

materiales_disponibles = [palos, gomas, tapones, corchos, pegamento]