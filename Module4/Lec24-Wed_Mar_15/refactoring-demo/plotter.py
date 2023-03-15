def identity(x):
    return x

class Plotter:
    def __init__(self, name="identity", color="#ffffff", fn=identity):
        self.name = name
        self.color = color
        self.fn = fn
