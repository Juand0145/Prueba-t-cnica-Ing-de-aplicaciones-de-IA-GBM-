import unittest
from solucion import es_palindromo

class TestSolucion(unittest.TestCase):
    def test_caso_1(self):
        self.assertFalse(es_palindromo("GBM"))

if __name__ == '__main__':
    unittest.main()