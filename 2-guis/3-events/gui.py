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
        self.__add_lyric_to_add_label()
        self.__add_lyric_add_frame()
        self.__add_lyric_entry()
        self.__add_lyrics_label()
        self.__add_lyric_button()
        self.__add_lyricsbox_listbox()
    
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(font = "Arial 50", text= "Song Maker")
    
    def __add_lyric_to_add_label(self):
        self.lyric_to_add_label = Label()
        self.lyric_to_add_label.grid(row=1, column=0, sticky=W)
        self.lyric_to_add_label.configure(font = "Arial 20", text= "Lyric to add:")
    
    def __add_lyric_add_frame(self):
        self.lyric_add_frame = Frame()
        self.lyric_add_frame.grid(row=2, column=0, sticky=W)

    def __add_lyric_entry(self):
        self.lyric_entry = Entry(self.lyric_add_frame)
        self.lyric_entry.pack(side=LEFT)
        #self.lyric_button.configure(width=30)

    def __add_lyric_button(self):
        self.lyric_button = Button(self.lyric_add_frame)
        self.lyric_button.pack(side=RIGHT)
        self.lyric_button.configure(font = "Arial 10", text= "Add")
        self.lyric_button.bind("<ButtonRelease-1>", self.lyric_button_clicked)

    def __add_lyrics_label(self):
        self.lyrics_label = Label()
        self.lyrics_label.grid(row=3, column=0, sticky=W)
        self.lyrics_label.configure(font = "Arial 20", text= "Lyrics:")
    
    def __add_lyricsbox_listbox(self):
        self.lyricsbox_listbox = Listbox()
        self.lyricsbox_listbox.grid(row=4, column=0)
    
    def lyric_button_clicked(self, event):
        lyric = self.lyric_entry.get()
        self.lyricsbox_listbox.insert(1,lyric)
    

gui = Gui()
gui.mainloop()