import tkinter as tk

from OptionsClass import Options

class manual(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "#d459de")
        self.controller = controller

        entrys = []
        for i in range(10):
            entrys.append(Options(self))

        button1 = tk.Button(self, text= "Simulate Data", font= ("Copper Black", 17), fg= "green",
        command= lambda: controller.give_mm_send_bool(True))
        button1.pack(anchor=tk.N,  side='top')
        button2 = tk.Button(self, text= "Cancel", font= ("Copper Black", 20), fg= "red",
        command= lambda: controller.give_mm_send_bool(False))
        button2.pack( anchor=tk.N,side='top')