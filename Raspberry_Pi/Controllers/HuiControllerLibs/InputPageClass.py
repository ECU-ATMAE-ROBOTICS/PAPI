import tkinter as tk

class InputPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        message = tk.Label(self, text= "Welcome to PAPI, Please Scan QR", font= ("Comic Sans Ms",50)) 
        message.grid()

        manual_button = tk.Button(self, text="Manual Mode")
        manual_button.grid(column=0, row=5)

        # button1 = tk.Button(self, text= "Manual Mode", font= ("Copper Black", 20), fg= "green",
        # command= lambda: controller.give_mm_bool(True))
        # button1.pack(side= "bottom", fill= "x", pady=5)

