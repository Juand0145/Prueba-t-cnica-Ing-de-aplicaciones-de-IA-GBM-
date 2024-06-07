import unittest
from solucion import calcular_campeones

class TestSolucion(unittest.TestCase):
    def test_caso_5(self):
        prix_pilots = [3, 3]
        placements = [
            [1, 2, 3],
            [3, 1, 2],
            [2, 3, 1]
        ]
        n_systems = 1
        scoring_systems = [
            [3, 10, 8, 6]
        ]
        campeones_esperados = [
            "1 2 3"
        ]
        self.assertEqual(calcular_campeones(prix_pilots, placements, n_systems, scoring_systems), campeones_esperados)

if __name__ == '__main__':
    unittest.main()
