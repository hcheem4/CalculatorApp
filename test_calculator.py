import unittest 
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(0,0),0)

    def test_subtract(self):
        self.assertEqual(subtract(10,5),5)
        self.assertEqual(subtract(0,7),-7)
        self.assertEqual(subtract(-1,1),0)

    def test_multiply(self):
        self.assertEqual(multiply(3,5), 15)
        self.assertEqual(multiply(-1,3),-3)
        self.assertEqual(multiply(0,5),0)

    def test_divide(self):
        self.assertEqual(divide(10,2),5)
        self.assertEqual(divide(-6, 3), -2)
        with self.assertRaises(ValueError):  # Test for division by zero
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
