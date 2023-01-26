import tkinter as tk
from tkinter import PhotoImage # Will use later for making a nice background

from .HuiControllerLibs.StartClass import start
from .HuiControllerLibs.ChoiceClass import choice

class HuiController(tk.Tk):
   def __init__(self, *args, **kwargs):
      tk.Tk.__init__(self, *args, **kwargs)

      # self.background_color = "#8647c9" Background color, for ease in downstream use

      self.tmp = None
      self.mm_bool = None
      self.mm_send_bool = None

      self.container = tk.Frame(self) # Get dynamic full size frame
      self.attributes('-fullscreen', True) # Makes the page fullscreen

      self.container.pack()
      # self.container.pack_propagate(True)

      self.frames = {}
      self.frames['start'] = start(parent=self.container, controller=self)
      self.frames['start'].pack(fill='both')
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