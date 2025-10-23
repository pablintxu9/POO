class Material:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

class Materials:
    def __init__(self):
        self.available_materials = {
            'palos': Material('palos', 5),
            'gomas': Material('gomas', 3),
            'tapones': Material('tapones', 2),
            'corchos': Material('corchos', 1),
            'pegamento': Material('pegamento', 4)
        }
        self.selected_materials = []

    def add_material(self, material_name):
        if material_name in self.available_materials:
            self.selected_materials.append(self.available_materials[material_name])
            return True
        return False

    def check_material(self, material_name):
        return material_name in self.available_materials

    def get_selected_materials(self):
        return self.selected_materials

    def total_strength(self):
        return sum(material.strength for material in self.selected_materials)