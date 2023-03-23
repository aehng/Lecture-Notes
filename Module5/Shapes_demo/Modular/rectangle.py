# construct a Rectangle object
def Rectangle(color, width, height):
    return {
            'color': color,
            'width': width,
            'height': height,
    }

# return the area of a rectangle
def area(self):
    return self['width'] * self['height']

# return the perimeter of a rectangle
def perimeter(self):
    return 2 * self['width'] + 2 * self['height']

# pretty print a rectangle
def pretty(self):
    return f"{self['color']} {self['width']}x{self['height']} rectangle"
