import tkinter as tk

root = tk.Tk() 

var = tk.StringVar() 

def get_state():
    print(var.get()) 


c = tk.Checkbutton(root, text='What should be state High or Low', onvalue='HIGH VALUE', offvalue='LOW VALUE', variable=var) 
c.deselect() 
c.pack() 


button = tk.Button(root, text='Get State', padx=20, pady=10, command=get_state) 
button.pack() 

root.mainloop()

