from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Codemy.com - Learn To Code!')
root.geometry("400x200")

def graph():
    arr = np.random.normal(200000, 25000, 1000)
    plt.polar(arr) 
    plt.show() 

my_button = Button(root, text="Graph It!", command=graph, padx=30, pady=10)
my_button.pack()

root.mainloop()

