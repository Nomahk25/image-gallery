import os
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

class ImageGallery:
    def __init__(self, root, img_folder):
        self.root = root
        self.root.title("Image Gallery")
        self.img_folder = img_folder
        self.images = [f for f in os.listdir(img_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        self.index = 0

        # Display first image
        self.img_label = Label(root)
        self.img_label.pack()

        # Navigation buttons
        prev_btn = Button(root, text="Previous", command=self.prev_image)
        prev_btn.pack(side="left")
        next_btn = Button(root, text="Next", command=self.next_image)
        next_btn.pack(side="right")

        self.show_image()

    def show_image(self):
        img_path = os.path.join(self.img_folder, self.images[self.index])
        img = Image.open(img_path)
        img = img.resize((400, 400))  # Resize to fit window
        self.photo = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.photo)
        self.root.title(f"Image Gallery - {self.images[self.index]}")

    def next_image(self):
        self.index = (self.index + 1) % len(self.images)
        self.show_image()

    def prev_image(self):
        self.index = (self.index - 1) % len(self.images)
        self.show_image()

if __name__ == "__main__":
    root = Tk()
    gallery = ImageGallery(root, "images")
    root.mainloop()
