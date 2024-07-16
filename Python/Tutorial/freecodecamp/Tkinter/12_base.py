import tkinter as tk 
from PIL import Image, ImageTk 

root = tk.Tk()  
root.title("Root Window")
def  more_new_window():
    global img 
    window = tk.Toplevel() 
    window.title('Last Window') 
    img = ImageTk.PhotoImage(Image.open('images/me1.png')) 
    label = tk.Label(window, image=img) 
    label.pack() 


def new_window():
    global my_img
    top_window = tk.Toplevel() 
    top_window.title("Top Window") 

    my_img = ImageTk.PhotoImage(Image.open('images/aspen.png'))
    top_window_label = tk.Label(top_window, image= my_img) 
    top_window_label.grid(row=0, column=0) 
    button = tk.Button(top_window, text='Open More New Window', padx=20, pady=10, command=more_new_window) 
    button.grid(row=1, column=0) 
    

button = tk.Button(root, text='Open Window', padx=20, pady=10, command=new_window) 
button.pack()

root.mainloop() 

