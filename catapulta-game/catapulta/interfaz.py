def mostrar_menu():
    print("Bienvenido a la Catapulta Game!")
    print("1. Construir catapulta")
    print("2. Disparar proyectil")
    print("3. Mostrar resultados")
    print("4. Salir")

def seleccionar_materiales():
    materiales_disponibles = ["Palos", "Gomas", "Tapones", "Corchos", "Pegamento"]
    seleccionados = []
    
    print("Selecciona los materiales para construir la catapulta:")
    for i, material in enumerate(materiales_disponibles, start=1):
        print(f"{i}. {material}")
    
    while True:
        eleccion = input("Ingresa el número del material que deseas seleccionar (o 'fin' para terminar): ")
        if eleccion.lower() == 'fin':
            break
        try:
            index = int(eleccion) - 1
            if 0 <= index < len(materiales_disponibles):
                seleccionados.append(materiales_disponibles[index])
                print(f"{materiales_disponibles[index]} añadido.")
            else:
                print("Selección inválida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    return seleccionados

def mostrar_resultados(resultados):
    print("Resultados del disparo:")
    for resultado in resultados:
        print(resultado)