import unittest
from solucion import calcular_campeones

class TestSolucion(unittest.TestCase):
    def test_caso_2(self):
        prix_pilots = [2, 2]
        placements = [
            [1, 2],
            [2, 1]
        ]
        n_systems = 2
        scoring_systems = [
            [2, 10, 8],
            [2, 25, 18]
        ]
        campeones_esperados = [
            "1 2",
            "1 2"
        ]
        self.assertEqual(calcular_campeones(prix_pilots, placements, n_systems, scoring_systems), campeones_esperados)

if __name__ == '__main__':
    unittest.main()