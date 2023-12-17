from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from Filters import LowPass, HighPass, BandBass, Homomorphic, Histogram
import matplotlib.pyplot as plt

root = Tk()
root.title("Image Processing Application")

root.minsize(1200, 800)  # width, height
root.maxsize(1200, 800)  # width, height

bg = PhotoImage(file = "bg.png")

def build_background_label():
	global background_label
	
	background_label = Label(root, image=bg)
	background_label.place(x=0, y=0)
	background_label.config(width=1200, height=800)

def build_title_frame():
	# Build cool title frame
	global title_frame
	title_frame = Frame(root)
	title_frame.pack(pady=50)
	# make style modern
	title_frame.config(
		bg="#2c3e50",
	)
	# make text title Image Processing Application and make its style modern
	global title
	title = Label(title_frame, text="Image Processing Application")
	title.config(
		bg="#2c3e50",
		fg="white",
		width=30,
		height=2,
		font=("Times", 30, "bold"),
	)
	title.pack(pady=10)
	
	


def build_image_label_result():
	global result_image_label
	result_image_label = Label(root)

def low_pass_filter():
	
	result_image = LowPass.low_pass_filter(file_path, 30)
	print('Debug here: ', result_image)

	result_image = Image.fromarray(result_image)
	result_image = result_image.resize((400, 400))
	result_image = ImageTk.PhotoImage(result_image)
	tempImg = build_image_label(result_image, "Filtered Image", 700)
	result_image_label.config(image=tempImg)
	result_image_label.image = result_image
	result_image_label.pack(pady=10)

def high_pass_filter():
	result_image = HighPass.high_pass_filter(file_path, 2)
	print('Debug here: ', result_image)

	result_image = Image.fromarray(result_image)
	result_image = result_image.resize((400, 400))
	result_image = ImageTk.PhotoImage(result_image)
	tempImg = build_image_label(result_image, "Filtered Image", 700)
	result_image_label.config(image=tempImg)
	result_image_label.image = result_image
	result_image_label.pack(pady=10)

def band_pass_filter():
	result_image = BandBass.band_pass_filter(file_path)
	
	plt.imshow(result_image)
	plt.show()
	
	result_image = Image.fromarray(result_image)
	result_image = result_image.resize((400, 400))
	result_image = ImageTk.PhotoImage(result_image)
	tempImg = build_image_label(result_image, "Filtered Image", 700)
	result_image_label.config(image=tempImg)
	result_image_label.image = result_image
	result_image_label.pack(pady=10)

def homomorphic_filter():
	result_image = Homomorphic.homomorphic_filter(file_path)
	result_image = Image.fromarray(result_image)
	result_image = result_image.resize((400, 400))
	result_image = ImageTk.PhotoImage(result_image)
	tempImg = build_image_label(result_image, "Filtered Image", 700)
	result_image_label.config(image=tempImg)
	result_image_label.image = result_image
	result_image_label.pack(pady=10)

def histogram_equalization():
	result_image = Histogram.histogram_filter(file_path)
	result_image = Image.fromarray(result_image)
	result_image = result_image.resize((400, 400))
	result_image = ImageTk.PhotoImage(result_image)
	tempImg = build_image_label(result_image, "Filtered Image", 700)
	result_image_label.config(image=tempImg)
	result_image_label.image = result_image
	result_image_label.pack(pady=10)

def build_filters_buttons():
	global filters_buttons

	# Sample button names, you can replace these with your actual button names
	button_names = [
		("Low-Pass Filter", low_pass_filter),
		("High-Pass Filter", high_pass_filter),
		("Band-Pass Filter", band_pass_filter),
		("Homomorphic Filter", homomorphic_filter),
		("Histogram Equalization", histogram_equalization)
	]

	# Create a list to store individual frames for each button
	button_frames = []

	for button_name, command_function in button_names:
		# Create a frame for each button without specifying background color
		button_frame = Frame(root)
		button_frame.pack(pady=50)

		# Create the button and add it to the frame
		button = Button(button_frame, text=button_name, command=command_function)
		# custom button with modern design and centered text
		button.config(
			bg="#2c3e50",
			fg="white",
			width=16,
			height=2,
			font=("Times", 12, "bold"),
			relief=FLAT,
			overrelief=RAISED
		)   
		button.pack(side=LEFT, padx=10)

		# Append the frame to the list
		button_frames.append(button_frame)

		# Position the frames
		for index, button_frame in enumerate(button_frames):
			button_frame.place(x=170 + index * 200, y=730)  # Adjust the positioning as needed

def build_image_label(photo, title, x):
	text = Label(root, text=title)
	text.config(
		bg="#2c3e50",
		fg="white",
		width=16,
		height=2,
		font=("Times", 12, "bold"),
	)
	text.pack(pady=10)
	text.place(x=x + 130, y=100)

	image_label = Label(root, image=photo)
	image_label.image = photo
	image_label.pack(pady=10)
	image_label.place(x=x, y=150)

	return image_label

def open_image():
	global file_path 
	file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
	if file_path:
		
		hide_ui()
		build_filters_buttons()
		image = Image.open(file_path)
		photo = ImageTk.PhotoImage(image)
		image = image.resize((400, 400))
		photo = ImageTk.PhotoImage(image)
		build_image_label(photo, "Original Image", 70)

		
def build_open_button():
	global open_button
	open_button = Button(root, text="Open Image", command=open_image)
	open_button.pack(pady=10)


def hide_ui():
	open_button.pack_forget()
	title_frame.pack_forget()
	title.pack_forget()

def setup_ui():
	build_background_label()
	build_title_frame()
	# build_image_label()
	build_image_label_result()
	build_open_button()



def main ():
	setup_ui()
	root.mainloop()
	
if __name__ == "__main__":
	main()