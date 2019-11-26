from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="ambulance.gif")
        self.map_image = PhotoImage(file="IV62p7Y.gif")
        

        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_map_frame()
        self.add_map_image_label()
        self.add_ambulance_image_label()
    
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label(self.map_frame)
        self.ambulance_image_label.place(x=10, y=10)
        self.ambulance_image_label.configure(image=self.ambulance_image)


    def add_map_image_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(image=self.map_image)
    
    def add_map_frame(self):
        self.map_frame = Frame()
        self.map_frame.configure(width=400, height=400)
    
    def bus_move(self, event):
        messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x))
        messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y))




# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
