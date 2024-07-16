import tkinter as tk 
from tkinter import messagebox 

root = tk.Tk() 
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    # root.attributes('-topmost', True) 
    messagebox.askquestion("INFORMATION", "This is a important Message") 
    # root.attributes('-topmost', False) 

button = tk.Button(root, text='Click Here', command=popup).pack()

root.mainloop() 



