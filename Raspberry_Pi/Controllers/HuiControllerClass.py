import tkinter as tk

from HuiController_libs.StartClass import start
from HuiController_libs.ChoiceClass import choice

class HuiController(tk.Tk):
     def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.tmp = None
        self.mm_bool = None
        self.mm_send_bool = None

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames['start'] = start(parent=self.container, controller=self)
        self.frames['start'].grid(row=0, column= 0, sticky= "nsew")
        # self.frames['manual'] = manual(parent=self.container, controller=self)
        # self.frames['manual'].grid(row=0,column=0,sticky="nsew")
    
     def show_frame(self, page_name, data = None):
        '''Show a frame for the given page name'''

        if page_name == 'choice':
            self.create_choice(page_name, data)
            self.frames[page_name].tkraise()
        else:
            frame = self.frames[page_name]
            frame.tkraise()

     def create_choice(self, page_name, data):
        self.frames[page_name] = choice(parent=self.container, controller=self, data=data)
        self.frames[page_name].grid(row=0, column= 0, sticky= "nsew")

     def give_bool(self, val):
        self.tmp = val
    
    #  def give_mm_bool(self, val):
    #     self.mm_bool = val

    #  def give_mm_send_bool(self, val):
    #     self.mm_send_bool = val