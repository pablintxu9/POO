class CatapultBase:
    def __init__(self):
        self.materials = []

    def build(self):
        if not self.materials:
            raise ValueError("No materials have been added to build the catapult.")
        return "Catapult built with materials: " + ", ".join(self.materials)

    def launch(self):
        if not self.materials:
            raise ValueError("Cannot launch. The catapult is not built.")
        return "Catapult launched!"