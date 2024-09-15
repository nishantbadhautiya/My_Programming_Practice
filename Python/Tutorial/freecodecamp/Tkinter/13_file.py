import tkinter as tk 
from PIL import Image, ImageTk 
from tkinter import filedialog 

root = tk.Tk() 

def open_file():
    global img
    filename = filedialog.askopenfilename(initialdir='./images/', title='Select Your File', filetypes=(('All File', '*.*'), ('JPG File', '*.jpg'), ('PNG File', '*.png'))) 
    label = tk.Label(root, text=filename)
    label.pack() 
    print(filename)
    img = ImageTk.PhotoImage(Image.open(filename))
    my_image = tk.Label(root, image=img) 
    my_image.pack() 


button = tk.Button(root, text='Select File', command=open_file) 
button.pack() 

root.mainloop() 
