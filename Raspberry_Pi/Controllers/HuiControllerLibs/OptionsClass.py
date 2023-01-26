import tkinter as tk

class Options():
    
    options=[
    'hopone',
    'hoptwo',
    'hopthree',
    'hopfour',
    'hopfive',
    'hopsix',
    'hopseven',
    'hopeight',
    'hopnine',
    'hopten',
    ]
    
    def __init__(self, parent):
        userSelect = tk.StringVar()
        userSelect.set(Options.options[0])
        drop_menu = tk.OptionMenu(parent, userSelect, *Options.options)
        drop_menu.pack( anchor=tk.NW)
        amount = tk.Spinbox(parent, from_=0, to=30, font=(30))
        amount.pack( anchor=tk.NE)