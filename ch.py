import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageFilter, ImageTk

class ImageProcessor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")

        # Background Image
        bg_image = Image.open("images/a.jpg")# Replace with your image path
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Select Image Button
        select_button = tk.Button(root, text="Select Image", command=self.select_image)
        select_button.pack(pady=20)

        # Apply Low Pass Filter Button
        filter_button = tk.Button(root, text="Apply Low Pass Filter", command=self.apply_low_pass_filter)
        filter_button.pack(pady=20)

    def select_image(self):
        image_path = filedialog.askopenfilename(initialdir="images", title="Select Image", filetypes=(("JPG Files", "*.jpeg"),))
        if image_path:
            self.original_image = Image.open(image_path)
            self.display_image(self.original_image)

    def apply_low_pass_filter(self):
        if hasattr(self, 'original_image'):
            filtered_image = self.original_image.filter(ImageFilter.BLUR)
            self.display_image(filtered_image)

    def display_image(self, image):
        # Destroy previous image labels
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) and widget != 'bg_label':
                widget.destroy()

        # Display the image
        photo = ImageTk.PhotoImage(image)
        img_label = tk.Label(self.root, image=photo)
        img_label.image = photo
        img_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessor(root)
    root.mainloop()