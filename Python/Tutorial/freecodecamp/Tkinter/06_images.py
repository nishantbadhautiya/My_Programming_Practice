from tkinter import * 
from PIL import Image, ImageTk

root = Tk() 
root.title('Nishant Badhautiya') 
# root.iconbitmap('/home/nishant/Desktop/Machine Learning/Intro-To-TKinter-Youtube-Course/codemy.ico')

img = Image.open('aspen.png')
my_img = ImageTk.PhotoImage(img)
label = Label(root, image=my_img)
label.pack() 


exit_button = Button(root, text="Exit Program", command=root.quit) 
exit_button.pack() 

root.mainloop() 
