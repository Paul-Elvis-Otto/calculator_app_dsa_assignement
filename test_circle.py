import unittest
import math
from circle import Circle


class TestCircle(unittest.TestCase):
    def test_calculate_perimeter(self):
        """Test that the perimeter calculation is correct."""
        # Test with radius = 5
        circle = Circle(5)
        expected_perimeter = 2 * math.pi * 5
        self.assertAlmostEqual(circle.calculate_perimeter(), expected_perimeter)

        # Test with radius = 0
        circle = Circle(0)
        self.assertEqual(circle.calculate_perimeter(), 0)

        # Test with radius = 7.5
        circle = Circle(7.5)
        expected_perimeter = 2 * math.pi * 7.5
        self.assertAlmostEqual(circle.calculate_perimeter(), expected_perimeter)

    def test_calculate_area(self):
        """Test that the area calculation is correct."""
        # Test with radius = 5
        circle = Circle(5)
        expected_area = math.pi * (5**2)
        self.assertAlmostEqual(circle.calculate_area(), expected_area)

        # Test with radius = 0
        circle = Circle(0)
        self.assertEqual(circle.calculate_area(), 0)

        # Test with radius = 7.5
        circle = Circle(7.5)
        expected_area = math.pi * (7.5**2)
        self.assertAlmostEqual(circle.calculate_area(), expected_area)


if __name__ == "__main__":
    unittest.main()
