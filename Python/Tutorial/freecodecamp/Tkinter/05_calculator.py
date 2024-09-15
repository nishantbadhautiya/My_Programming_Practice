from tkinter import * 

root = Tk() 
root.title('Calculator')

e = Entry(root, width=40, borderwidth=5) 
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) 

def button_clicked(number):
    # num = e.get() + str(number)
    # e.delete(0, END)
    # e.insert(0, num)
    e.insert(END, number)

def handle_clear():
    e.delete(0, END)

def handle_add():
    global first_number
    first_number = int(e.get())
    e.delete(0, END) 
    global operation 
    operation = 'addition' 

def handle_sub():
    global first_number
    first_number = int(e.get())
    e.delete(0, END) 
    global operation 
    operation = 'subtraction' 

def handle_multiply():
    global first_number 
    first_number = int(e.get())
    e.delete(0, END) 
    global operation 
    operation = 'multiplication' 

def handle_division():
    global first_number 
    first_number = int(e.get())
    e.delete(0, END) 
    global operation 
    operation = 'division' 

def handle_equal():
    second_number = int(e.get()) 
    e.delete(0, END) 
    if(operation == 'addition'):
        e.insert(0, str(first_number + second_number)) 

    if(operation == 'subtraction'):
        e.insert(0, str(first_number - second_number)) 
    
    if(operation == 'multiplication'):
        e.insert(0, str(first_number * second_number)) 
    
    if(operation == 'division'):
        e.insert(0, str(first_number / second_number)) 

# define the button 
button_1 = Button(root, text='1', padx=50, pady=50, command=lambda: button_clicked(1)) 
button_2 = Button(root, text='2', padx=50, pady=50, command=lambda: button_clicked(2)) 
button_3 = Button(root, text='3', padx=50, pady=50, command=lambda: button_clicked(3)) 
button_4 = Button(root, text='4', padx=50, pady=50, command=lambda: button_clicked(4)) 
button_5 = Button(root, text='5', padx=50, pady=50, command=lambda: button_clicked(5)) 
button_6 = Button(root, text='6', padx=50, pady=50, command=lambda: button_clicked(6)) 
button_7 = Button(root, text='7', padx=50, pady=50, command=lambda: button_clicked(7)) 
button_8 = Button(root, text='8', padx=50, pady=50, command=lambda: button_clicked(8)) 
button_9 = Button(root, text='9', padx=50, pady=50, command=lambda: button_clicked(9)) 
button_0 = Button(root, text='0', padx=50, pady=50, command=lambda: button_clicked(0)) 
button_clear= Button(root, text="Clear", padx=100, pady=50, command=handle_clear) 
button_add = Button(root, text="+", padx=50, pady=50, command=handle_add) 
button_equal = Button(root, text="=", padx=100, pady=50, command=handle_equal) 
button_sub = Button(root, text="-", padx=50, pady=50, command=handle_sub) 
button_multiply = Button(root, text="X", padx=50, pady=50, command=handle_multiply) 
button_division = Button(root, text="/", padx=50, pady=50, command=handle_division) 


# create the Button 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2) 

button_add.grid(row=5, column=0) 
button_equal.grid(row=5, column=1, columnspan=2) 

button_sub.grid(row=6, column=0) 
button_multiply.grid(row=6, column=1)
button_division.grid(row=6, column=2)

root.mainloop() 
