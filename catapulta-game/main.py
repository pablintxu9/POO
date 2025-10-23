# ...existing code...
from catapulta.interfaz import seleccionar_materiales
from catapulta.catapulta import Catapulta

def main():
    print("Bienvenido al juego de la Catapulta!")
    catapulta = None

    while True:
        print("\nMenú:")
        print("0) Crear / Reconstruir catapulta")
        print("1) Disparar")
        print("2) Mostrar materiales de la catapulta")
        print("3) Salir")

        accion = input("Elige una opción: ").strip()

        if accion == '0':
            if catapulta is not None:
                resp = input("Ya existe una catapulta. ¿Reconstruirla? (s/n): ").strip().lower()
                if not resp.startswith('s'):
                    print("Se mantiene la catapulta actual.")
                    continue
            materiales_seleccionados = seleccionar_materiales()
            catapulta = Catapulta(materiales_seleccionados)
            catapulta.construir()
        elif accion == '1':
            if catapulta is None:
                print("No hay una catapulta construida. Elige la opción 0 para crearla.")
            else:
                catapulta.disparar()
        elif accion == '2':
            if catapulta is None:
                print("No hay una catapulta construida.")
            else:
                catapulta.mostrar_materiales()
        elif accion == '3':
            print("Saliendo del juego. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
# ...existing code...