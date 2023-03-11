# Import the tkinter GUI framework
from tkinter import *
    

class TkinterDemo:
    def __init__(self):
        self.window = Tk() # Create a window
        self.window.title("Widgets Demo") # Set a title
        
        # make this demo readable on a 4k display
        self.window.call('tk', 'scaling', 1)

        # Add a button, a check button, and a radio button to frame1
        frame1 = Frame(self.window) # Create and add a frame to window
        frame1.pack()      
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = "Bold", 
            variable = self.v1, command = self.processCheckbutton) 
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = "Red", bg = "red",
                variable = self.v2, value = 1, 
                command = self.processRadiobutton) 
        rbYellow = Radiobutton(frame1, text = "Yellow", 
                bg = "yellow", variable = self.v2, value = 2, 
                command = self.processRadiobutton) 
        cbtBold.grid(row = 1, column = 1)
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)
        
        # Add a label, an entry, and a button to frame 2
        frame2 = Frame(self.window) # Create and add a frame to window
        frame2.pack()
        label = Label(frame2, text = "Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name) 
        btGetName = Button(frame2, text = "Get Name", 
            command = self.processButton)
        message = Message(frame2, text = "It is a widgets demo")
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)
        
        # Add a text window to the window
        text = Text(self.window) # Create a text add to the window
        text.pack()
        text.insert(END, 
            "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END, 
            "these carefully designed examples and use them ")
        text.insert(END, "to create your applications.")

        # Add a button to destroy the window, thus quitting this application
        btDestroy = Button(self.window, text="Exit this program", command=self.window.destroy)
        btDestroy.pack()


    def processCheckbutton(self):
        print("check button is " 
            + ("checked " if self.v1.get() == 1 else "unchecked"))
        
    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") 
            + " is selected " )
    
    def processButton(self):
        print("Your name is " + self.name.get())


    def mainloop(self):
        print("Starting the main loop now")
        self.window.mainloop() # Create an event loop
        print("The main loop has returned")



if __name__ == '__main__':
    # Create & run the GUI
    TkinterDemo().mainloop()
