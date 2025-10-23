class Catapulta:
    def __init__(self):
        self.materiales = []
        self.proyectil = None

    def construir(self, materiales):
        self.materiales = materiales
        print("Catapulta construida con los siguientes materiales:")
        for material in self.materiales:
            print(f"- {material}")

    def disparar(self):
        if self.proyectil:
            print(f"Disparando el proyectil de tipo {self.proyectil.tipo} con peso {self.proyectil.peso}.")
        else:
            print("No hay proyectil para disparar.")

    def mostrar_materiales(self):
        if self.materiales:
            print("Materiales utilizados en la catapulta:")
            for material in self.materiales:
                print(f"- {material}")
        else:
            print("No se han utilizado materiales para construir la catapulta.")