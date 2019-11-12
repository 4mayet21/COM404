from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gui")
        self.configure(bg= "#eee", height = 800, width = 500)
        self.add_heading_label()
        self.add_detail_fields()
        self.add_footer()  
        self.add_email_frame()
        self.add_email_entry
        self.add_email_label()
        self.add_submit_button()

    def add_heading_label(self):
    # create   
        self.heading_label = Label()
        self.heading_label.pack()
    # style
        self.heading_label.configure(font="Arial 36",
                                 text="SUSPECT HERESY?")
        self.heading_label = Label()
        self.heading_label.pack()
    # style
        self.heading_label.configure(font="Arial 20",
                                 text="Report It To Your \nRegimental Commissar")
    
    def add_detail_fields(self):
        self.heading_label = Label()
        self.heading_label.pack()
        self.heading_label.configure(font = "Arial 12", text= "Your Regiment: ")
        #
        self.heading_label = Label()
        self.heading_label.pack()
        self.heading_label.configure(font = "Arial 12", text= "Your ID Number: ")

        self.heading_label = Label()
        self.heading_label.pack()
        self.heading_label.configure(font = "Arial 12", text= "Your Contact Email: ")

        self.heading_label = Label()
        self.heading_label.pack()
        self.heading_label.configure(font = "Arial 12", text= "Suspect Regiment: ")

        self.heading_label = Label()
        self.heading_label.pack()
        self.heading_label.configure(font = "Arial 12", text= "Suspect ID Number: ")

        self.heading_label = Label()
        self.heading_label.pack()
        self.heading_label.configure(font = "Arial 12", text= "Details of Heresy: ")

    def add_submit_button(self):
        self.heading_label = Label()
        self.heading_label.pack()
        self.heading_label.configure(font = "Arial 12", text= "Submit")
        


    def add_footer(self):
        self.heading_label = Label()
        self.heading_label.pack()
        self.heading_label.configure(font = "Arial 20", text= "SUFFER NOT THE HERETIC \n TO LIVE")
        
        self.heading_label = Label()
        self.heading_label.pack()
        self.heading_label.configure(font = "Arial 8", text= "Distributed by The Astra Militarum of The Imeprium of Mankind, \n in accordance with the Officio Prefectus.")
        
    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack()
   
    def add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
 
    def add_email_entry(self):
        self.email_entry = Entry(self.email_entry)
        self.email_entry.pack(side=RIGHT)




 


#For testing
gui = Gui()
gui.mainloop()