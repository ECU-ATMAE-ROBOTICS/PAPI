import tkinter as tk

class mm(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "#d459de")
        self.controller = controller
        #label1 = tk.Label