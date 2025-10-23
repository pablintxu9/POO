# Proyecto: Catapulta orientada a objetos (simulación educativa)
# Estructura del proyecto (todos los archivos están incluidos abajo):
# 
# catapulta/
#   __init__.py
#   base.py
#   arm.py
#   tension.py
#   projectile.py
#   catapult.py
# main.py
# README.md
# 
# Nota: este proyecto es una simulación educativa (no instrucciones de construcción real).
# Simula conversión de energía elástica a velocidad del proyectil y la trayectoria balística.

# -------------------------
# catapulta/__init__.py
# -------------------------

"""Paquete catapulta - contiene clases que modelan componentes de una catapulta simple."""

from .base import Base
from .arm import Arm
from .tension import Tension
from .projectile import Projectile
from .catapult import Catapult

# -------------------------
# catapulta/base.py
# -------------------------

"""Módulo Base: define la base de la catapulta."""

from dataclasses import dataclass

@dataclass
class Base:
    """Representa la base rígida donde se monta la catapulta.

    Attributes:
        width: ancho de la base (m)
        depth: profundidad de la base (m)
    """
    width: float = 0.2
    depth: float = 0.1

    def info(self) -> str:
        return f"Base(width={self.width} m, depth={self.depth} m)"

# -------------------------
# catapulta/arm.py
# -------------------------

"""Módulo Arm: define el brazo móvil de la catapulta."""

from dataclasses import dataclass
import math

@dataclass
class Arm:
    """Brazo de la catapulta.

    Attributes:
        length: longitud del brazo (m)
        fulcrum_offset: distancia desde la parte trasera del brazo al fulcro (m). Si fulcrum_offset < length/2, la parte delantera es más larga.
    """
    length: float = 0.25
    fulcrum_offset: float = 0.06  # distancia desde el extremo trasero (donde se aplica la tension) al fulcro

    def speed_multiplier(self) -> float:
        """Factor geométrico aproximado que convierte la velocidad tangencial en la parte trasera del brazo
        en velocidad de la punta donde se coloca el proyectil.

        Usamos una relación de palanca: velocidad_punta / velocidad_trasera ≈ longitud_punta / longitud_trasera
        donde:
          longitud_punta = length - fulcrum_offset
          longitud_trasera = fulcrum_offset

        Se devuelve al menos 0.1 para evitar divisiones por cero.
        """
        long_punta = max(1e-6, self.length - self.fulcrum_offset)
        long_trasera = max(1e-6, self.fulcrum_offset)
        return long_punta / long_trasera

    def info(self) -> str:
        return f"Arm(length={self.length} m, fulcrum_offset={self.fulcrum_offset} m, multiplier={self.speed_multiplier():.2f})"

# -------------------------
# catapulta/tension.py
# -------------------------

"""Módulo Tension: modela la fuente de energía elástica (p. ej. gomas)."""

from dataclasses import dataclass
import math

@dataclass
class Tension:
    """Modelo simple de tensión elástica usando constante k y estiramiento x.

    E = 1/2 * k * x^2

    Attributes:
        k: constante elástica efectiva (N/m)
        x: estiramiento (m)
    """
    k: float = 200.0
    x: float = 0.05

    def potential_energy(self) -> float:
        """Energía potencial elástica en joules."""
        return 0.5 * self.k * (self.x ** 2)

    def info(self) -> str:
        return f"Tension(k={self.k} N/m, x={self.x} m, energy={self.potential_energy():.4f} J)"

# -------------------------
# catapulta/projectile.py
# -------------------------

"""Módulo Projectile: define el proyectil lanzado."""

from dataclasses import dataclass

@dataclass
class Projectile:
    """Proyectil simple.

    Attributes:
        mass: masa en kilogramos
        radius: radio (opcional, m) para fines informativos
    """
    mass: float = 0.005  # 5 gramos por defecto (0.005 kg)
    radius: float = 0.01

    def info(self) -> str:
        return f"Projectile(mass={self.mass} kg, radius={self.radius} m)"

# -------------------------
# catapulta/catapult.py
# -------------------------

"""Módulo Catapult: clase que combina componentes y simula un lanzamiento simple."""

from dataclasses import dataclass
import math
from .base import Base
from .arm import Arm
from .tension import Tension
from .projectile import Projectile

G = 9.80665  # gravedad (m/s^2)

@dataclass
class Catapult:
    base: Base
    arm: Arm
    tension: Tension
    projectile: Projectile
    launch_angle_deg: float = 45.0  # ángulo aproximado de la punta respecto a la horizontal (grados)

    def simulate_launch(self) -> dict:
        """Simula el lanzamiento devolviendo un diccionario con resultados.

        Modelo simplificado:
          1) La energía potencial elástica E = 1/2 k x^2
          2) Toda la energía se convierte en energía cinética del proyectil: 1/2 m v^2 = E_eff
             (E_eff toma en cuenta pérdidas por eficiencia)
          3) La velocidad inicial se multiplica por un factor geométrico de brazo
          4) Se calcula el alcance horizontal usando movimiento balístico sin resistencia del aire
             R = v0^2 * sin(2*theta) / g

        Este modelo es didáctico y no pretende precisión experimental.
        """
        results = {}

        # energía disponible
        E = self.tension.potential_energy()
        results['elastic_energy_J'] = E

        # eficiencia estimada (pérdidas mecánicas). La dejamos en 0.6 por defecto.
        efficiency = 0.6
        E_eff = E * efficiency
        results['efficiency'] = efficiency
        results['effective_energy_J'] = E_eff

        # velocidad del proyectil (si toda E_eff se convierte en energía cinética translacional)
        m = max(1e-9, self.projectile.mass)
        v_linear = math.sqrt(2.0 * E_eff / m)
        results['v_linear_m_per_s'] = v_linear

        # factor geométrico del brazo (convierte velocidad en la parte trasera en velocidad de la punta)
        mult = self.arm.speed_multiplier()
        v_tip = v_linear * mult
        results['speed_multiplier'] = mult
        results['v_tip_m_per_s'] = v_tip

        # ángulo
        theta = math.radians(self.launch_angle_deg)
        results['launch_angle_deg'] = self.launch_angle_deg

        # alcance ideal en suelo al mismo nivel (sin resistencia del aire)
        range_m = (v_tip ** 2) * math.sin(2 * theta) / G
        results['range_m'] = max(0.0, range_m)

        # tiempo de vuelo
        t_flight = (2 * v_tip * math.sin(theta)) / G
        results['time_of_flight_s'] = max(0.0, t_flight)

        # velocidad inicial vertical/horizontal
        results['v0x_m_per_s'] = v_tip * math.cos(theta)
        results['v0y_m_per_s'] = v_tip * math.sin(theta)

        return results

    def info(self) -> str:
        parts = [self.base.info(), self.arm.info(), self.tension.info(), self.projectile.info()]
        return " | ".join(parts)

# -------------------------
# main.py
# -------------------------

"""Archivo principal: crea una catapulta, la simula y muestra resultados.

Ejecución:
    python main.py

Este script muestra cómo usar las clases definidas en el paquete catapulta.
"""

if __name__ == "__main__":
    # importar clases del paquete local
    from catapulta.base import Base
    from catapulta.arm import Arm
    from catapulta.tension import Tension
    from catapulta.projectile import Projectile
    from catapulta.catapult import Catapult
    import json

    # Crear componentes con parámetros predeterminados (puedes modificar aquí)
    base = Base(width=0.25, depth=0.12)
    arm = Arm(length=0.30, fulcrum_offset=0.07)
    tension = Tension(k=250.0, x=0.06)
    projectile = Projectile(mass=0.007)  # 7 gramos

    cat = Catapult(base=base, arm=arm, tension=tension, projectile=projectile, launch_angle_deg=45.0)

    print("Catapulta (configuración):")
    print(cat.info())
    print('\nSimulación de lanzamiento...')

    results = cat.simulate_launch()

    print('\nResultados:')
    print(json.dumps(results, indent=2))

    # Ejemplo de interpretación rápida
    print(f"\nAlcance estimado: {results['range_m']:.2f} m")
    print(f"Tiempo de vuelo estimado: {results['time_of_flight_s']:.2f} s")

# -------------------------
# README.md
# -------------------------

"""
Proyecto: Simulación de catapulta (educativo)

Estructura:
  - catapulta/: paquete con clases
  - main.py: script de ejemplo

Cómo usar:
  1. Coloca la carpeta "catapulta" y el archivo main.py en el mismo directorio.
  2. Ejecuta: python main.py

Notas y supuestos:
  - Este es un modelo muy simplificado (no hay resistencia del aire ni fricciones complejas).
  - Se supone que parte de la energía elástica se pierde (eficiencia por defecto 0.6).
  - Las constantes usadas son meramente ilustrativas; ajústalas para experimentar.

Seguridad:
  - Es una simulación informática. No contiene instrucciones de construcción peligrosas.

"""
