import unittest
import test

class TestTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(test.add(2,2), 4)

    def test_sub(self):
        self.assertEqual(test.subtract(3,3),0)

    def test_mult(self):
        self.assertEqual(test.multiply(3,3),9)

    def test_div(self):
        self.assertEqual(test.divide(3,3), 1.0)

if __name__ == "__main__":
    unittest.main()