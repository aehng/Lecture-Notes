from math import pi

# construct a Circle object
def Circle(color, radius):
    return {
            'color': color,
            'radius': radius,
    }

# return the area of a circle
def area(self):
    return self['radius'] * self['radius'] * pi

# return the perimeter of a circle
def perimeter(self):
    return 2 * pi * self['radius']

# pretty print a circle
def pretty(self):
    return f"{self['color']} circle of radius {self['radius']}"
