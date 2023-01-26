import tkinter as tk

class choice(tk.Frame):
     def __init__(self, parent, controller, data):
        tk.Frame.__init__(self, parent, bg= "#d459de")
        self.controller = controller
        label1 = tk.Label(self, text= f"{data[2]}", bg= "#d459de", font= ("Calibri",50), height= 1)
        label1.pack(side= "top", fill= "x", pady=5)
        Label2 = tk.Label(self, text= f"{data[1]} {data[0]}",bg= "#d459de", font= ("Calibri", 50), height= 1)
        Label2.pack(side= "top", fill= "x", pady=5)
        button1 = tk.Button(self, text= "Correct Information", font= ("Copper Black", 20), fg= "green",
        command= lambda: controller.give_bool(True))
        button1.pack(side= "bottom", fill= "x", pady=5)
        button2 = tk.Button(self, text= "Incorrect Information", font= ("Copper Black", 20), fg= "red",
        command= lambda: controller.give_bool(False))
        button2.pack(side= "bottom", fill= "x", pady=5)
        button3 = tk.Button(self, text= "Manual Entry Mode", font=("lato",20),
        command= lambda: controller.show_frame("mm"))
        button3.pack(side= "bottom", fill= "x", pady=5)