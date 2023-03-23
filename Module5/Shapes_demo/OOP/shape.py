class Shape:
    # Abstract constructor, cannot actually construct a Shape object
    def __init__(self, color):
        self.color = color
        # Comment out line 7 to create the shape, then try invoking the methods
        #   on Shape!
        raise NotImplementedError("How can you have *just* a SHAPE?")

    # Abstract calculateArea
    def calculateArea(self):
        raise NotImplementedError("How can a SHAPE with an UNDEFINED number of sides have an area?")

    # Abstract calculatePerimeter
    def calculatePerimeter(self):
        raise NotImplementedError("How can a SHAPE with an UNDEFINED number of sides have a perimeter?")
