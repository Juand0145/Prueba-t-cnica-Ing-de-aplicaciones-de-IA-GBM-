import unittest
from solucion import es_palindromo

class TestSolucion(unittest.TestCase):
    def test_caso_1(self):
        self.assertTrue(es_palindromo("ANA"))

if __name__ == '__main__':
    unittest.main()