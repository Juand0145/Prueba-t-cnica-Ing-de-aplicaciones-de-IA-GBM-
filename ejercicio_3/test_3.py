import unittest
from solution import process_input

class TestSolution(unittest.TestCase):
    def test_case_3(self):
        input_data = "1\n3"
        expected_output = [2]
        self.assertEqual(process_input(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()
