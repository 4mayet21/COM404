<<<<<<< HEAD
from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        self.configure(bg= "#eee", height = 400, width = 400)

        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=1)
        self.heading_label.configure(font = "Arial 50", text= "Entrance ticket")
        
    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0, columnspan=1, sticky=W)
        self.instruction_label.configure(font = "Arial 20", text= "How many tickets are needed?")
        
    def __add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2, column=0, columnspan=1)
        self.tickets_entry.configure(width=40)
        

    def __add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0, columnspan=1)
        self.buy_button.configure(font = "Arial 12", text= "Buy")
        self.buy_button.bind("<ButtonRelease-1>", self.buy_button_clicked)
        
    def buy_button_clicked(self, event):
        numTickets = self.tickets_entry.get()
        if numTickets == 1:
            messagebox.showinfo("Purchased!", "You have purchased " + numTickets+" tickets")
        else:
            messagebox.showinfo("What are you Doing?!", "You have entered an Invalid number of tickets!")

#For testing
gui = Gui()
gui.mainloop() 
=======
from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        self.configure(bg= "#eee", height = 400, width = 400)

        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=1)
        self.heading_label.configure(font = "Arial 50", text= "Entrance ticket")
        
    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0, columnspan=1, sticky=W)
        self.instruction_label.configure(font = "Arial 20", text= "How many tickets are needed?")
        
    def __add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2, column=0, columnspan=1)
        self.tickets_entry.configure(width=40)
        

    def __add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0, columnspan=1)
        self.buy_button.configure(font = "Arial 12", text= "Buy")
        self.buy_button.bind("<ButtonRelease-1>", self.buy_button_clicked)
        
    def buy_button_clicked(self, event):
        numTickets = self.tickets_entry.get()
        if numTickets == 1:
            messagebox.showinfo("Purchased!", "You have purchased " + numTickets+" tickets")
        else:
            messagebox.showinfo("What are you Doing?!", "You have entered an Invalid number of tickets!")

#For testing
gui = Gui()
gui.mainloop() 
>>>>>>> 4f267e0a834c79dbcc6603e52727bc9190161607
