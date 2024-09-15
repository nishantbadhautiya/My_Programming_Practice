from tkinter import * 

root = Tk() 

def myClick():
    myLabel = Label(root, text='Hey! I got clicked') 
    myLabel.pack()


# myButton = Button(root, text='Click Me') 
# myButton = Button(root, text='Click Me', state='disabled') 
# myButton = Button(root, text='Click Me', state= DISABLED) 
# myButton = Button(root, text='Click Me', padx=64, pady=24) 
# myButton = Button(root, text='Click Me', command=myClick) 
# myButton = Button(root, text='Click Me', command=myClick()) 
myButton = Button(root, text='Click Me', command=myClick, fg='red', bg='green') 

myButton.pack() 

root.mainloop() 
