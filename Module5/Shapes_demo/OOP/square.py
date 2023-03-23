import rectangle

# From the rectangle module, inherit the Rectangle class
class Square(rectangle.Rectangle):
    # Square constructor, can construct a Square object
    def __init__(self, color, side):
        self.color = color
        self.side = side

    # calculateArea for a Square, returns a number that is the computed area
    def calculateArea(self):
        return self.side * self.side

    # calculatePerimeter for a Square, returns a number that is the perimeter
    def calculatePerimeter(self):
        return 4 * self.side
