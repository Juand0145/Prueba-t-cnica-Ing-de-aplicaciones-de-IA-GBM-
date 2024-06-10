import unittest
import numpy as np

from keras.models import load_model

# Load model
model = load_model('costumer_clasifciation.h5')

class TestCustomerClassification(unittest.TestCase):
    def test_low_value_customer(self):
        # Customer with low total spending
        customer_data = np.array([[1012, 105, 15]])
        category = np.argmax(model.predict(customer_data))
        self.assertEqual(category, 2)  # High value category

    def test_medium_value_customer(self):
        # Customer with medium total spending
        customer_data = np.array([[-0.57816154,  0.74636952, -0.60779349]])
        category = np.argmax(model.predict(customer_data))
        self.assertEqual(category, 1)  # Medium value category

    def test_high_value_customer(self):
        # Customer with high total spending
        customer_data = np.array([[-1.68238784, -1.18531062, -1.95546849]])
        category = np.argmax(model.predict(customer_data))
        self.assertEqual(category, 1)  # Medium value category

if __name__ == '__main__':
    unittest.main()
