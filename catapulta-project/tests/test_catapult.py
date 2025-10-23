# filepath: catapulta-project/tests/test_catapult.py

import unittest
from catapulta.catapult import Catapult
from catapulta.materials import Material
from catapulta.enemy import Enemy

class TestCatapult(unittest.TestCase):

    def setUp(self):
        self.catapult = Catapult()
        self.materials = [
            Material("palo", 1),
            Material("goma", 2),
            Material("tapón", 1),
            Material("corcho", 1),
            Material("pegamento", 1)
        ]
        for material in self.materials:
            self.catapult.add_material(material)

    def test_build_catapult(self):
        self.catapult.build()
        self.assertTrue(self.catapult.is_built)

    def test_launch_catapult(self):
        enemy = Enemy(health=10)
        self.catapult.build()
        damage = self.catapult.launch()
        enemy.take_damage(damage)
        self.assertEqual(enemy.health, 10 - damage)

    def test_materials_count(self):
        self.assertEqual(len(self.catapult.materials), 5)

    def test_invalid_material(self):
        with self.assertRaises(ValueError):
            self.catapult.add_material(Material("invalid_material", 1))

if __name__ == '__main__':
    unittest.main()