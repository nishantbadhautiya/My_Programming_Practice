from tkinter import * 

root = Tk() 

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello) 
    # print(e.get())
    myLabel.pack()

# e = Entry() # entry widget 
# e = Entry(root, width=50, bg='red', fg='white')
# e = Entry(root, width=50, borderwidth=8)
e = Entry(root, width=50) 
e.pack() 
e.insert(0, 'Enter text here! ') 

myButton = Button(root, text="Enter you name", command=myClick) 
myButton.pack()

root.mainloop() 
