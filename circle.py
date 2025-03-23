import math


class Circle:
    """
    A class to represent a circle and calculate its properties.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with the given radius.

        Parameters:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def calculate_perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

    def calculate_area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius**2)
