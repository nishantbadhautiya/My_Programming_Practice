import tkinter as tk 

root = tk.Tk() 
root.title("Radio Button in tkinter")
def clicked(value):
    label = tk.Label(root, text=value, padx=20, pady=10) 
    label.pack() 

# var = tk.IntVar() 
# var.set(2) '

Food_items = [
    ('Pizza','Pizza'), 
    ('Burger','Burger'), 
    ('Cheese', 'Cheese'), 
    ('Samosa', 'Samosa') 
]


var = tk.StringVar() 
var.set('Burger') 

for text, value in Food_items:
    button = tk.Radiobutton(root, text=text, value=value, variable=var)
    button.pack() 


# button1 = tk.Radiobutton(root, text='Option 1', value=1, command=lambda: clicked(var.get()), variable=var).pack()
# button2 = tk.Radiobutton(root, text='Option 2', value=2, command=lambda: clicked(var.get()), variable=var).pack() 

label = tk.Label(root, text= "Initial Value is " + str(var.get()), padx=20, pady=10) 
label.pack() 

get_item = tk.Button(root, text='Get Food Item' , padx=20, pady=10, command=lambda:clicked(var.get()))
get_item.pack() 


root.mainloop() 
