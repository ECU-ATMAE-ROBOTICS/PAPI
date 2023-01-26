import tkinter as tk

from .HuiControllerLibs.InputPageClass import InputPage
from .HuiControllerLibs.ManualModePageClass import ManualModePage

class HuiController(tk.Tk):
   def __init__(self):
      super().__init__()
      self.title("HuiController")
      self.geometry("800x800")

      # Create a container frame
      self.container = tk.Frame(self)
      self.container.pack(fill='both', expand=True)

      # Create a dictionary to hold other frame objects
      self.frames = {}

      # Initialize the Input Page
      self.frames["InputPage"] = InputPage(self.container, self)

      # Show the Input Page by default
      self.show_frame("InputPage")



   def create_page(self, page_name, *args, **kwargs):
      if page_name in self.frames:
         self.frames[page_name].destroy()
      page_class = globals()[page_name]
      self.frames[page_name] = page_class(self.container, self, *args, **kwargs)
      self.show_frame(page_name)

   def show_frame(self, page_name):
      frame = self.frames.get(page_name)
      frame.tkraise()