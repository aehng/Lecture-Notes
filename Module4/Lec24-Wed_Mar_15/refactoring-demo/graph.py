from tkinter import Tk, Canvas, PhotoImage, mainloop

class Graph:
    def __init__(self, axis=(-5.0, 5.0), pixels=1024):
        self.axis = axis
        self.pixels = pixels
        self.half_pixels = pixels / 2
        self.pixel_size = (axis[1] - axis[0]) / pixels
        self.win = Tk()
        self.canvas = Canvas(self.win, width=pixels, height=pixels, bg="#000000")
        self.canvas.pack()
        self.img = PhotoImage(width=pixels, height=pixels)
        self.canvas.create_image((self.half_pixels, self.half_pixels), image=self.img, state="normal")

    def plot(self, plotter):
        print(f"Plotting {plotter.name}...")
        for x_px in range(self.pixels + 1):
            x = self.axis[0] + (x_px * self.pixel_size)
            y = plotter.fn(x)
            # convert this Y value back to a Y pixel coordinate
            y_px = int(self.half_pixels - (y / self.pixel_size))
            if 0 <= y_px <= self.pixels:
                self.img.put(plotter.color, (x_px, y_px))
                self.win.update()

    def mainloop(self):
        mainloop()
