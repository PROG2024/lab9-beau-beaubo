"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
import math

class CircleTest(unittest.TestCase):

    def setUp(self) -> None:
        """Setup"""
        self.circle1 = Circle(1)
        self.circle2 = Circle(3)
        self.circle_radius_zero = Circle(0)

    def test_positive_rad(self):
        self.assertEqual(self.circle1.get_area(), math.pi * 1 * 1)
        self.circle3 = self.circle1.add_area(self.circle2)
        self.assertEqual(self.circle3.get_radius(), math.hypot(self.circle1.get_radius(), (self.circle2.get_radius())))
        new_radius = math.hypot(self.circle1.get_radius(), (self.circle2.get_radius()))
        self.assertEqual(self.circle3.get_area(), math.pi * new_radius * new_radius)

    def test_edge_case(self):
        new_radius = math.hypot(self.circle_radius_zero.get_radius(), (self.circle2.get_radius()))
        self.assertEqual(new_radius, self.circle2.add_area(self.circle_radius_zero).get_radius())
        self.assertEqual(Circle(new_radius).get_area(), self.circle2.add_area(self.circle_radius_zero).get_area())

    def test_raise_exception(self):
        with self.assertRaises(ValueError):
            Circle(-1)



