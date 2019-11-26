from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cactus_image = PhotoImage(file="tenor.gif")
        self.cacti_with_name_image = PhotoImage(file="templar40k.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_heading_label()
        self.add_cactus_image_label()
        self.add_submit_button()
        #self.submit_button_clicked_L()
        #self.submit_button_clicked_R()
       

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(font = "Arial 16", text= "Cactus")

    def add_cactus_image_label(self):
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1, column=0)
        self.cactus_image_label.configure(image=self.cactus_image, height=500,
                                             width=400)

    def add_cactus_names_image_label(self):
        self.cactus_names_image_label = Label()
        self.cactus_names_image_label.grid(row=1, column=0)
        self.cactus_names_image_label.configure(image=self.cacti_with_name_image, height=500,
                                             width=400)

    def add_submit_button(self):
        self.submit_button = Button()
        self.submit_button.grid(row=2, column=0)

        self.submit_button.configure(text="Flip")
            
        self.submit_button.bind("<ButtonRelease-1>", self.submit_button_clicked_L)
        self.submit_button.bind("<ButtonRelease-3>", self.submit_button_clicked_R)

    def submit_button_clicked_L(self, event):
        self.add_cactus_image_label()
        #self.cactus_image_label.configure(image=self.cactus_image)
    
    def submit_button_clicked_R(self, event):
        self.add_cactus_names_image_label()
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
