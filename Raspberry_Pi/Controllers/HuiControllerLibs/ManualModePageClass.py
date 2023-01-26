import tkinter as tk

class ManualModePage(tk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller
        tk.Label(self, text="This is my custom frame").grid(row=0, column=0, sticky='nsew')
        