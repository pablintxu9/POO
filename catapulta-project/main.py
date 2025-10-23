# filepath: catapulta-project/main.py

from catapulta.catapult import Catapult
from catapulta.materials import Material
from catapulta.simulator import Simulator

def main():
    print("Bienvenido al simulador de catapultas!")
    
    # Selección de materiales
    materials = []
    available_materials = ["palos", "gomas", "tapones", "corchos", "pegamento"]
    
    print("Materiales disponibles:")
    for i, material in enumerate(available_materials, start=1):
        print(f"{i}. {material}")
    
    while True:
        choice = input("Seleccione un material para agregar a la catapulta (o 'fin' para terminar): ")
        if choice.lower() == 'fin':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(available_materials):
            materials.append(available_materials[int(choice) - 1])
            print(f"Material '{available_materials[int(choice) - 1]}' agregado.")
        else:
            print("Selección inválida. Intente de nuevo.")
    
    # Construcción de la catapulta
    catapult = Catapult(materials)
    catapult.build()
    
    # Simulación de lanzamiento
    simulator = Simulator(catapult)
    simulator.start_simulation()

if __name__ == "__main__":
    main()