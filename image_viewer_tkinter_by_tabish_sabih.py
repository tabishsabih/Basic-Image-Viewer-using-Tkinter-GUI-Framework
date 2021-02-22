from tkinter import *
from PIL import ImageTk, Image #pip install Pillow is required for this to be imported

root = Tk()
root.title('Image Viewer by Tabish Sabih') #title
root.iconbitmap('ac.ico') #favicon

#images to display
my_img1 = ImageTk.PhotoImage(Image.open('ac1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('ac2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('ac3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('ac4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('ac5.jpg'))

my_label = Label(root, image=my_img1) #image that is opened when the prog starts
my_label.grid(row=0, column=0, columnspan=3)

#images into a list to use index numbers
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

def forward(image_number):
	global my_label
	global button_forward
	global button_back
	#We want to get rid of image that is already open before opening the next one to avoid overlapping
	my_label.grid_forget() #this is how to get rid of the opened grid

	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text='>>', command=lambda:forward(image_number+1))
	button_back = Button(root, text='<<', command=lambda:back(image_number-1))

	if image_number == 5:
		button_forward = Button(root, text='>>', state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text='>>', command=lambda:forward(image_number+1))
	button_back = Button(root, text='<<', command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = Button(root, text='<<', state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()