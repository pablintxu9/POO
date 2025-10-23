def validate_material_selection(selected_materials, available_materials):
    for material in selected_materials:
        if material not in available_materials:
            return False
    return True

def generate_random_result():
    import random
    return random.randint(1, 100)

def display_message(message):
    print(message)