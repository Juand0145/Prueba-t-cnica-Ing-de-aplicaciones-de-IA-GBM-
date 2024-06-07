import unittest
from solucion import es_palindromo

class TestSolucion(unittest.TestCase):
    def test_caso_2(self):
        self.assertFalse(es_palindromo("Python"))

if __name__ == '__main__':
    unittest.main()
