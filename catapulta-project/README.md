# Catapulta Project

Este proyecto es una simulación de una catapulta que permite a los usuarios seleccionar materiales para construirla y lanzar proyectiles contra enemigos. A continuación se detallan las características y la estructura del proyecto.

## Estructura del Proyecto

```
catapulta-project
├── catapulta
│   ├── __init__.py
│   ├── base.py
│   ├── materials.py
│   ├── catapult.py
│   ├── enemy.py
│   ├── simulator.py
│   └── utils.py
├── main.py
├── requirements.txt
├── setup.py
├── tests
│   ├── __init__.py
│   └── test_catapult.py
└── README.md
```

## Descripción de Archivos

- **catapulta/__init__.py**: Indica que la carpeta `catapulta` es un paquete de Python.
- **catapulta/base.py**: Contiene la clase base `CatapultBase` con métodos comunes como `build()` y `launch()`.
- **catapulta/materials.py**: Define la clase `Material` que representa los materiales disponibles para la construcción de la catapulta.
- **catapulta/catapult.py**: Implementa la clase `Catapult`, que hereda de `CatapultBase` y maneja la lógica de construcción y lanzamiento.
- **catapulta/enemy.py**: Define la clase `Enemy`, que representa a los enemigos y maneja el daño recibido.
- **catapulta/simulator.py**: Gestiona la simulación del lanzamiento y la interacción con los enemigos.
- **catapulta/utils.py**: Contiene funciones utilitarias para validar entradas y generar resultados aleatorios.
- **main.py**: Punto de entrada del programa, permite al usuario seleccionar materiales y simular lanzamientos.
- **requirements.txt**: Lista las dependencias necesarias para el proyecto.
- **setup.py**: Configura el paquete y sus dependencias.
- **tests/__init__.py**: Indica que la carpeta `tests` es un paquete de Python.
- **tests/test_catapult.py**: Contiene pruebas unitarias para asegurar el correcto funcionamiento del código.

## Instalación

Para instalar las dependencias del proyecto, ejecute el siguiente comando:

```
pip install -r requirements.txt
```

## Ejecución

Para ejecutar el programa, utilice el siguiente comando:

```
python main.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si desea contribuir, por favor haga un fork del repositorio y envíe un pull request con sus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo LICENSE para más detalles.