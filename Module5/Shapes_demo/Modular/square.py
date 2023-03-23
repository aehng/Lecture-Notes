import rectangle

# construct a Square object
def Square(color, side):
    return rectangle.Rectangle(color, side, side)

# return the area of a square
def area(self):
    return rectangle.area(self)

# return the perimeter of a square
def perimeter(self):
    return rectangle.perimeter(self)

# pretty print a square
def pretty(self):
    return f"{self['color']} {self['height']} Square"
