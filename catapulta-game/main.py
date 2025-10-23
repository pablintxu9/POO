# Contenido del archivo main.py

from catapulta.interfaz import mostrar_menu, seleccionar_materiales
from catapulta.catapulta import Catapulta

def main():
    print("Bienvenido al juego de la Catapulta!")
    
    materiales_seleccionados = seleccionar_materiales()
    
    catapulta = Catapulta(materiales_seleccionados)
    catapulta.construir()
    
    while True:
        accion = mostrar_menu()
        
        if accion == '1':
            catapulta.disparar()
        elif accion == '2':
            catapulta.mostrar_materiales()
        elif accion == '3':
            print("Saliendo del juego. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()