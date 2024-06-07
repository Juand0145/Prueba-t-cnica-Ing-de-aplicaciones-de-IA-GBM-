import unittest
from solucion import es_palindromo

class TestSolucion(unittest.TestCase):
    def test_caso_4(self):
        self.assertFalse(es_palindromo("Hello"))

if __name__ == '__main__':
    unittest.main()
