from tkinter import *

root = Tk()
root.title("LabelFrame Example")

frame = LabelFrame(root, text="This is a LabelFrame", padx=100, pady=100, relief=RIDGE, background='yellow', foreground='blue', font=('Arial', 16), labelanchor='nw') 
frame.pack(padx=10, pady=20, expand=True) 

label = Label(frame, text="Inside the LabelFrame", fg='grey')
label.pack()

button = Button(frame, text="A Button", bg='purple', fg='white')
button.pack()

root.mainloop()
