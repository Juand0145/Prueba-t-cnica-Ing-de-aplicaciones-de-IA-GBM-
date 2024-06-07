import unittest
from solucion import es_palindromo

class TestSolucion(unittest.TestCase):
    def test_caso_3(self):
        self.assertTrue(es_palindromo("A MAN A PLAN A CANAL PANAMA".replace(" ", "").upper()))

if __name__ == '__main__':
    unittest.main()
