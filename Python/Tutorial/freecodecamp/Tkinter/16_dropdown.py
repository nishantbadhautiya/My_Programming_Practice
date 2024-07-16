import tkinter as tk 
root = tk.Tk() 

values = [
    'Sunday',
    'Monday', 
    'Tuesday', 
    'Friday', 
    'Saturday'
]

def get_value():
    print(var.get()) 

var = tk.StringVar() 
var.set(values[0]) 

options = tk.OptionMenu(root, var, *values) 
options.pack() 

button = tk.Button(root, text="Get Selection", padx=20, pady=10, command=get_value) 
button.pack() 


root.mainloop() 

