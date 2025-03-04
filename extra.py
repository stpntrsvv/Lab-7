import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_fox_image():
    response = requests.get("https://randomfox.ca/floof/")
    data = response.json()
    image_url = data['image']
    image_response = requests.get(image_url, stream=True)
    image_data = image_response.content
    image = Image.open(BytesIO(image_data))
    image = image.resize((400, 300))
    return ImageTk.PhotoImage(image)


def update_image():
    new_image = load_fox_image()
    image_label.configure(image=new_image)
    image_label.image = new_image


root = tk.Tk()
root.title("Генератор случайных лис")
root.resizable(False, False)

image_label = tk.Label(root)
image_label.pack(padx=10, pady=10)

update_button = tk.Button(
    root,
    text="Еще одну!",
    command=update_image,
    font=('Arial', 14),
    bg='orange'
)
update_button.pack(pady=10)

update_image()
root.mainloop()