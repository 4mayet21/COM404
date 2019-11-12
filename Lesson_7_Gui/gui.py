from tkinter import *

class Gui(Tk):
  def __init__(self):
    super().__init__()
    
    #self.geometry("500x500")
    self.title("Gui")
    self.configure(bg= "#eee", height = 500, width = 500)
    self.add_heading_label()


  def add_heading_label(self):
    # create   
    self.heading_label = Label()
    self.heading_label.place(x=0, y=0)
    
    # style
    self.heading_label.configure(font="Arial 24",
                                 text="This is a heading.")
