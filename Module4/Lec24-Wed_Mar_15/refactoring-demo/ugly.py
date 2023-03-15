#!/usr/bin/python3

from math import sin, cos
from tkinter import Tk, Canvas, PhotoImage, mainloop


colors=['#ffffff','#ff0000','#00ff00','#0000ff','#ffff00','#ff00ff','#00ffff']

xax = (-5.0, 5.0)  # x axis
w = Tk()  # create a Tk Window object, save it into w
pixels = 1024 / 2  # the number of pixels
c = Canvas(w, width=1024, height=1024, bg="#000000")
half_pixels = 1024 / 2  # the number of pixels divided by two
c.pack()  # pack the Canvas into the window
yax = (-5.0, 5.0)  # the Y axis
i = PhotoImage(width=1024, height=1024)  # create a PhotoImage object
c.create_image((1024/2, 1024/2), image=i, state="normal")
c.pack()  # pack the Canvas into the window

print(f"Plotting the identity function...")
c = colors[0:1][0] # get the next color
del colors[0]
for p in range(1024 + 1):  # for i in pixels...
    v = (xax[0] + (p * ((xax[1] - xax[0]) / 1024.0)))
    # Identity function
    val = v
    # convert this value back to a Y pixel
    y=int((512-(val/ ((xax[1]-xax[0]) /1024.0))))
    i.put(c,(p,y))
    w.update()

print(f"Plotting sine(x)...")
c = colors[0]  # get the next color
colors.remove(c)
for p in range(1025):  # for i in pixels...
    v=xax[0]+(p*((xax[1]-xax[0])/1024.0))
    # y = sin(x)
    # val = v
    val=sin(v)
    # convert this value back to a Y pixel
    y=int((1024/2-(val/((xax[1]-xax[0])/1024.0))))
    i.put(c,(p,y))
    w.update()

print(f"Plotting cosine(x)...")
# c = colors.pop(0)
colors.reverse()
c = colors.pop()
colors.reverse()
for p in range(1025):  # for i in pixels...
    v=xax[0]+(p*((xax[1]-xax[0])
        /1024.0))
    #val=v
    val=cos(v)
    # convert this value back to a Y pixel
    y=int((1024/2
        -
        (val/((xax[1]-xax[0])
            /
            1024.0))))

    i.put(c,(p,y))
    w.update()

print(f"Plotting absolute_value(x)...")
c = colors[0:1][0] # get the next color
del colors[0]
for p in range(1025):  # for i in pixels...
    v=xax[0]+(p*((xax[1]-xax[0])/1024.0))

    val=v
    # the absolute v of x
    val=abs(v)

    # convert this value back to a Y pixel
    y=int((1024/2-(val/((xax[1]-xax[0])/1024.0))))

    i.put(c,(p,y))
    w.update()

print(f"Plotting square(x)...")
c = colors.pop(0)  # get the next color
for p in range(285, 741):  # for i in pixels...
    v=xax[0]+(p*((xax[1]-xax[0])/1024.0))

    # X squared
    val=v*v
    # val=v

    # convert this value back to a Y pixel
    y=int((512-(val/((xax[1]-xax[0])/1024.0))))

    i.put(c,(p,y))
    w.update()

print(f"Plotting cube(x)...")
# c = colors[0]  # get the next color
# colors.remove(c)
colors.reverse()
c = colors.pop()
colors.reverse()
for p in range(285, 687):  # for i in pixels...
    v=xax[0]+(p*((xax[1]-xax[0])/1024.0))
    val=v*v*v
    # convert this value back to a Y pixel
    y=int((512-(val/((xax[1]-xax[0])/1024.0))))
    i.put(c,(p,y))
    w.update()

print(f"Plotting cosine(x^2)...")
c = colors[0]  # get the next color
colors = colors[1:]
for p in range(1024 + 1):  # for i in pixels...
    v=xax[0]+(p*((xax[1]-xax[0])/1024.0))
    # Identity function
    val = v
    val=cos(v*v)
    y=int((1024/2-(val
        /((xax[1]-xax[0])/1024.0))))
    i.put(c,(p,y))
    w.update()
mainloop()

