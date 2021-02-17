import unittest
from radius import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):

    def test_area(self):
       self.assertEqual(circle_area(3), pi*3**2)
       self.assertEqual(circle_area(1), pi)
       self.assertEqual(circle_area(0), 0)
       self.assertEqual(circle_area(2.5), pi*2.5** 2)

    def test_values(self):
       self.assertRaises(ValueError, circle_area, -2)
       self.assertRaises(ValueError, circle_area, -1)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, 5+2j)
        self.assertRaises(TypeError, circle_area, [2,4])
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "QQ")