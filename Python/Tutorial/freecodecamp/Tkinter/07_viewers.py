from tkinter import * 
from PIL import Image, ImageTk 
root = Tk() 
root.title("Image Viewer") 
root.resizable(False, False) 
root.geometry('500x500') 


image_1 = ImageTk.PhotoImage(Image.open('images/aspen.png')) 
image_2 = ImageTk.PhotoImage(Image.open('images/aspen2.png'))
image_3 = ImageTk.PhotoImage(Image.open('images/me1.png'))
image_4 = ImageTk.PhotoImage(Image.open('images/me2.png'))
image_5 = ImageTk.PhotoImage(Image.open('images/me3.png'))

image_list = [image_1, image_3, image_2, image_4, image_5] 

def handle_left_button(image_number):
    global image_widget 
    global left_button 
    global right_button 
    image_widget.grid_forget()
    image_widget = Label(image=image_list[image_number - 1]) 
    left_button = Button(root, text="<<", padx=20, pady=10, command=lambda: handle_left_button(image_number - 1)) 
    right_button = Button(root, text=">>", padx=20, pady=10, command=lambda:handle_right_button(image_number + 1)) 
    if(image_number == 1):
        left_button = Button(root, text="<<", padx=20, pady=10, state=DISABLED) 
    
    image_widget.grid(row=0, column=0, columnspan=3)
    left_button.grid(row=1, column=0) 
    right_button.grid(row=1, column=2) 


def handle_right_button(image_number):
    global image_widget 
    global left_button 
    global right_button 
    image_widget.grid_forget() 
    image_widget = Label(image= image_list[image_number - 1]) 
    left_button = Button(root, text="<<", padx=20, pady=10, command=lambda: handle_left_button(image_number - 1)) 
    right_button = Button(root, text=">>", padx=20, pady=10, command=lambda: handle_right_button(image_number + 1)) 
    if (image_number == 5): 
        right_button = Button(root, text=">>", padx=20, pady=10, state=DISABLED) 

    image_widget.grid(row=0, column=0, columnspan=3) 
    left_button.grid(row=1, column=0) 
    right_button.grid(row=1, column=2) 

image_number = 1
image_widget = Label(image=image_list[image_number - 1]) 
left_button = Button(root, text="<<", padx=20, pady=10, command=handle_left_button, state=DISABLED)
right_button = Button(root, text=">>", padx=20, pady=10, command=lambda:handle_right_button(2)) 
exit_button = Button(root, text="Exit Program", padx=20, pady=10, command=root.quit) 

image_widget.grid(row=0, column=0, columnspan=3) 
left_button.grid(row=1, column=0) 
exit_button.grid(row=1, column=1)
right_button.grid(row=1, column=2) 


root.mainloop() 



