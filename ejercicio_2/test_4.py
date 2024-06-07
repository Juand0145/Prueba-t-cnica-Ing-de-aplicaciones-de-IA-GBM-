import unittest
from solucion import calcular_campeones

class TestSolucion(unittest.TestCase):
    def test_caso_4(self):
        prix_pilots = [4, 4]
        placements = [
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [2, 3, 4, 1],
            [1, 4, 3, 2]
        ]
        n_systems = 1
        scoring_systems = [
            [4, 10, 8, 6, 4]
        ]
        campeones_esperados = [
            "1 2 3 4"
        ]
        self.assertEqual(calcular_campeones(prix_pilots, placements, n_systems, scoring_systems), campeones_esperados)

if __name__ == '__main__':
    unittest.main()
