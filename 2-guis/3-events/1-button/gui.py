from tkinter import *
from tkinter import messagebox
class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gui")
        self.configure(bg= "#eee", height = 800, width = 500)
        self.add_heading_label()
        self.add_detail_fields()
        self.add_footer()
        self.add_submit_button()
        self.field_entries()
        


    def add_heading_label(self):
    # create   
        self.heading_label = Label()
        self.heading_label.place(x=10, y=40)
    # style
        self.heading_label.configure(font="Arial 36",
                                 text="SUSPECT HERESY?")
        self.subheading_label = Label()
        self.subheading_label.place(x=110, y=110)
    # style
        self.subheading_label.configure(font="Arial 20",
                                 text="Report It To Your \nRegimental Commissar")
    
    def add_detail_fields(self):
        self.detail_fields_yr = Label()
        self.detail_fields_yr.place(x=10, y=260)
        self.detail_fields_yr.configure(font = "Arial 12", text= "Your Regiment: ")
        #
        self.detail_fields_yi = Label()
        self.detail_fields_yi.place(x=10, y=300)
        self.detail_fields_yi.configure(font = "Arial 12", text= "Your ID Number: ")

        self.detail_fields_yc = Label()
        self.detail_fields_yc.place(x=10, y=340)
        self.detail_fields_yc.configure(font = "Arial 12", text= "Your Contact Email: ")

        self.detail_fields_sr = Label()
        self.detail_fields_sr.place(x=10, y=380)
        self.detail_fields_sr.configure(font = "Arial 12", text= "Suspect Regiment: ")

        self.detail_fields_si = Label()
        self.detail_fields_si.place(x=10, y=420)
        self.detail_fields_si.configure(font = "Arial 12", text= "Suspect ID Number: ")

        self.detail_fields_dh = Label()
        self.detail_fields_dh.place(x=10, y=460)
        self.detail_fields_dh.configure(font = "Arial 12", text= "Details of Heresy: ")


    def field_entries(self):
        self.field_entries_yr = Entry()
        self.field_entries_yr.place(x=160, y=260)
        self.field_entries_yr.configure(width=30)

        self.field_entries_yi = Entry()
        self.field_entries_yi.place(x=160, y=300)
        self.field_entries_yi.configure(width=30)

        self.field_entries_yc = Entry()
        self.field_entries_yc.place(x=160, y=340)
        self.field_entries_yc.configure(width=30)

        self.field_entries_sr = Entry()
        self.field_entries_sr.place(x=160, y=380)
        self.field_entries_sr.configure(width=30)

        self.field_entries_si = Entry()
        self.field_entries_si.place(x=160, y=420)
        self.field_entries_si.configure(width=30)

        self.field_entries_dh = Text()
        self.field_entries_dh.place(x=160, y=460)
        self.field_entries_dh.configure(font = "Arial 8", height= 3, width=30)

    def add_submit_button(self):
        #self.heading_label = Label()
        #self.heading_label.place(x=220, y=550)
        #self.heading_label.configure(font = "Arial 12", text= "Submit")
        self.submit_button = Button()
        self.submit_button.place(x=220, y=550)

        # style
        self.submit_button.configure(text="Submit")
            # events
        self.submit_button.bind("<ButtonRelease-1>", self.submit_button_clicked)
        
    def submit_button_clicked(self, event):
        messagebox.showinfo("Submitted!", "The Heretic will be purged in the name of the God-Emperor!")




    def add_footer(self):
        self.footer = Label()
        self.footer.place(x=60, y=630)
        self.footer.configure(font = "Arial 20", text= "SUFFER NOT THE HERETIC \n TO LIVE")
        
        self.footer2 = Label()
        self.footer2.place(x=90, y=710)
        self.footer2.configure(font = "Arial 8", text= "Distributed by The Astra Militarum of The Imeprium of Mankind, \n in accordance with the Officio Prefectus.")
    
    



def submit_button_clicked(self, event):
    messagebox.showinfo("Submitted!", "The Heretic will be purged in the name of the God-Emperor!")


#For testing
gui = Gui()
gui.mainloop() 