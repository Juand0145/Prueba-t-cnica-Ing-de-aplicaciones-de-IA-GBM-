import unittest
from solucion import es_palindromo

class TestSolucion(unittest.TestCase):
    def test_caso_5(self):
        self.assertTrue(es_palindromo("radar"))

if __name__ == '__main__':
    unittest.main()
