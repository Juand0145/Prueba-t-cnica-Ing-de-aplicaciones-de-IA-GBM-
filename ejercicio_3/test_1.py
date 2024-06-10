import unittest
from solution import process_input

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        input_data = "1\n1"
        expected_output = [1]
        self.assertEqual(process_input(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()
