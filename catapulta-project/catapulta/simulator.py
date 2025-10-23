class Simulator:
    def __init__(self, catapult, enemies):
        self.catapult = catapult
        self.enemies = enemies

    def start_simulation(self):
        print("Iniciando la simulación...")
        for enemy in self.enemies:
            self.launch_at_enemy(enemy)

    def launch_at_enemy(self, enemy):
        damage = self.catapult.launch()
        enemy.take_damage(damage)
        print(f"Lanzamiento realizado! Daño infligido a {enemy.name}: {damage}")
        if enemy.is_destroyed():
            print(f"{enemy.name} ha sido eliminado!")

    def check_enemies_status(self):
        for enemy in self.enemies:
            if enemy.is_destroyed():
                print(f"{enemy.name} está fuera de combate.")
            else:
                print(f"{enemy.name} sigue en pie con {enemy.health} de salud.")