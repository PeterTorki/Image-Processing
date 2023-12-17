from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from Filters import LowPass, HighPass, BandBass, Homomorphic, Histogram
import matplotlib.pyplot as plt

root = Tk()  # create a root widget
root.title("Image Processing Application")

root.minsize(1900, 1200)  # width, height
root.maxsize(1300, 800)  # width, height

bg = PhotoImage(file = "bg.png")

def build_background_label():
	global background_label
	background_label = Label(root, image=bg)
	background_label.place(x=0, y=0)

def build_title_frame():
	global title_frame
	title_frame = Frame(root)
	title_frame.pack(pady=0)
	
	global title
	title = Canvas(title_frame, width=600, height=100)
	title.pack()
	title.create_text(300, 50, text="Image Processing Application", font=("Times", 30, "bold"))

def build_image_label():
	global image_label

	image_label = Label(root)
	image_label.config(width=400, height=400)
	

def build_image_label_result():
	global result_image_label
	result_image_label = Label(root)
	result_image_label.config(width=400, height=400)

	result_image_label.pack_forget()

def low_pass_filter():
	
	result_image = LowPass.low_pass_filter(file_path, 30)
	print('Debug here: ', result_image)

	result_image = Image.fromarray(result_image)
	result_image = result_image.resize((400, 400))
	result_image = ImageTk.PhotoImage(result_image)
	result_image_label.config(image=result_image)
	result_image_label.image = result_image
	result_image_label.pack(pady=10)

def high_pass_filter():
	result_image = HighPass.high_pass_filter(file_path, 2)
	print('Debug here: ', result_image)

	result_image = Image.fromarray(result_image)
	result_image = result_image.resize((400, 400))
	result_image = ImageTk.PhotoImage(result_image)
	
	result_image_label.config(image=result_image)
	result_image_label.image = result_image
	result_image_label.pack(pady=10)

def band_pass_filter():
	result_image = BandBass.band_pass_filter(file_path)
	
	plt.imshow(result_image)
	plt.show()
	
	result_image = Image.fromarray(result_image)
	result_image = result_image.resize((400, 400))
	result_image = ImageTk.PhotoImage(result_image)
	result_image_label.config(image=result_image)
	result_image_label.image = result_image
	result_image_label.pack(pady=10)

def homomorphic_filter():
	result_image = Homomorphic.homomorphic_filter(file_path)
	result_image = Image.fromarray(result_image)
	result_image = result_image.resize((400, 400))
	result_image = ImageTk.PhotoImage(result_image)
	result_image_label.config(image=result_image)
	result_image_label.image = result_image
	result_image_label.pack(pady=10)

def histogram_equalization():
	result_image = Histogram.histogram_filter(file_path)
	result_image = Image.fromarray(result_image)
	result_image = result_image.resize((400, 400))
	result_image = ImageTk.PhotoImage(result_image)
	result_image_label.config(image=result_image)
	result_image_label.image = result_image
	result_image_label.pack(pady=10)

def build_filters_buttons():
	global filters_buttons
	filters_buttons = Frame(root)
	filters_buttons.pack(pady=10)
	
	global low_pass_button
	low_pass_button = Button(filters_buttons, text="Low-Pass Filter", command=low_pass_filter)
	low_pass_button.pack(side=LEFT, padx=10)
	
	global high_pass_button
	high_pass_button = Button(filters_buttons, text="High-Pass Filter", command=high_pass_filter)
	high_pass_button.pack(side=LEFT, padx=10)
	
	global band_pass_button
	band_pass_button = Button(filters_buttons, text="Band-Pass Filter", command=band_pass_filter)
	band_pass_button.pack(side=LEFT, padx=10)
	
	global homomorphic_button
	homomorphic_button = Button(filters_buttons, text="Homomorphic Filter", command=homomorphic_filter)
	homomorphic_button.pack(side=LEFT, padx=10)
	
	global blur_button
	blur_button = Button(filters_buttons, text="Histogram Equalization", command=histogram_equalization)
	blur_button.pack(side=LEFT, padx=10)
	

def open_image():
	global file_path 
	file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
	if file_path:
		image = Image.open(file_path)
		photo = ImageTk.PhotoImage(image)
		image = image.resize((400, 400))
		photo = ImageTk.PhotoImage(image)
		image_label.config(image=photo)
		image_label.image = photo
		image_label.pack(pady=50)
		
		hide_ui()
		image_label.pack()
		build_filters_buttons()

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
	build_image_label()
	build_image_label_result()
	build_open_button()



def main ():
	setup_ui()
	root.mainloop()
	
if __name__ == "__main__":
	main()