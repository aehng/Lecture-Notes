#!/usr/bin/python3

from math import sin, cos
from graph import Graph
from plotter import Plotter


def square(x):
    return x * x

def cube(x):
    return x * x * x

def cosx2(x):
    return cos(square(x))

g = Graph()
g.plot(Plotter())
g.plot(Plotter(name="sine(x)", color='#ff0000', fn=sin))
g.plot(Plotter(name="cosine(x)", color='#00ff00', fn=cos))
g.plot(Plotter(name="abs(x)", color='#0000ff', fn=abs))
g.plot(Plotter(name="square(x)", color='#ffff00', fn=square))
g.plot(Plotter(name="cube(x)", color='#ff00ff', fn=cube))
g.plot(Plotter(name="cos(x^2)", color='#00ffff', fn=cosx2))
g.mainloop()
