import shape

# From the shape module, inherit the Shape class
class Rectangle(shape.Shape):
    # Rectangle constructor, can construct a Rectangle object
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    # calculateArea for a Rectangle, returns a number that is the computed area
    def calculateArea(self):
        return self.width * self.height

    # calculatePerimeter for a Rectangle, returns a number that is the perimeter
    def calculatePerimeter(self):
        return 2 * self.width + 2 * self.height
