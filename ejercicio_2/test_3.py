import unittest
from solucion import calcular_campeones

class TestSolucion(unittest.TestCase):
    def test_caso_3(self):
        prix_pilots = [1, 5]
        placements = [
            [1, 2, 3, 4, 5]
        ]
        n_systems = 2
        scoring_systems = [
            [3, 10, 8, 6],
            [5, 25, 18, 15, 12, 10]
        ]
        campeones_esperados = [
            "1",
            "1"
        ]
        self.assertEqual(calcular_campeones(prix_pilots, placements, n_systems, scoring_systems), campeones_esperados)

if __name__ == '__main__':
    unittest.main()
