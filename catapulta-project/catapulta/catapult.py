class Catapult(CatapultBase):
    def __init__(self):
        super().__init__()
        self.materials = []

    def build(self, materials):
        self.materials = materials
        print(f"Catapult built with materials: {', '.join(materials)}")

    def launch(self, enemy):
        if not self.materials:
            print("Catapult is not built yet!")
            return
        
        damage = len(self.materials) * 10  # Example damage calculation
        enemy.take_damage(damage)
        print(f"Launched at enemy! Damage dealt: {damage}")

    def get_materials(self):
        return self.materials