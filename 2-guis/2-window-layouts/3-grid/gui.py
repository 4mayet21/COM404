from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gui")
        self.configure(bg= "#eee", height = 800, width = 500)
        self.add_heading_label()
        self.add_detail_fields()
        self.add_footer()
        self.add_submit_button()


    def add_heading_label(self):
    # create   
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)
    # style
        self.heading_label.configure(font="Arial 36",
                                 text="SUSPECT HERESY?")
        self.heading_label = Label()
        self.heading_label.grid(row=1, column=0, columnspan=2)
    # style
        self.heading_label.configure(font="Arial 20",
                                 text="Report It To Your \nRegimental Commissar")
    
    def add_detail_fields(self):
        self.heading_label = Label()
        self.heading_label.grid(row=2, column=0, columnspan=1)
        self.heading_label.configure(font = "Arial 12", text= "Your Regiment: ")
        #
        self.heading_label = Label()
        self.heading_label.grid(row=3, column=0, columnspan=1)
        self.heading_label.configure(font = "Arial 12", text= "Your ID Number: ")

        self.heading_label = Label()
        self.heading_label.grid(row=4, column=0, columnspan=1)
        self.heading_label.configure(font = "Arial 12", text= "Your Contact Email: ")

        self.heading_label = Label()
        self.heading_label.grid(row=5, column=0, columnspan=1)
        self.heading_label.configure(font = "Arial 12", text= "Suspect Regiment: ")

        self.heading_label = Label()
        self.heading_label.grid(row=6, column=0, columnspan=1)
        self.heading_label.configure(font = "Arial 12", text= "Suspect ID Number: ")

        self.heading_label = Label()
        self.heading_label.grid(row=7, column=0, columnspan=1)
        self.heading_label.configure(font = "Arial 12", text= "Details of Heresy: ")

    def add_submit_button(self):
        self.heading_label = Label()
        self.heading_label.grid(row=11, column=0, columnspan=2)
        self.heading_label.configure(font = "Arial 12", text= "Submit")
        


    def add_footer(self):
        self.heading_label = Label()
        self.heading_label.grid(row=9, column=0, columnspan=2)
        self.heading_label.configure(font = "Arial 20", text= "SUFFER NOT THE HERETIC \n TO LIVE")
        
        self.heading_label = Label()
        self.heading_label.grid(row=10, column=0, columnspan=2)
        self.heading_label.configure(font = "Arial 8", text= "Distributed by The Astra Militarum of The Imeprium of Mankind, \n in accordance with the Officio Prefectus.")





#For testing
gui = Gui()
gui.mainloop() 