import tkinter as tk

class InputPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        message = tk.Label(self, text= "Welcome to PAPI, Please Scan QR", font= ("Comic Sans Ms",50)) 
        message.pack()

        manual_button = tk.Button(self, text="Manual Mode")
        manual_button.pack()


