from math import pi
import shape

# From the shape module, inherit the Shape class
class Circle(shape.Shape):
    # Circle constructor, can construct a Circle object
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    # calculateArea for a Circle, returns a number that is the computed area
    def calculateArea(self):
        return self.radius * self.radius * pi

    # calculatePerimeter for a Circle, returns a number that is the perimeter
    def calculatePerimeter(self):
        return 2 * pi * self.radius
