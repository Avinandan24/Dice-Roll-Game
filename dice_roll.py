import tkinter as tk
from PIL import Image, ImageTk
import random 

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")

dice = ["disc-1.png","disc-2.png","disc-3.png","disc-4.png","disc-5.png","disc-6.png"]

# Resize the images
size = (80, 80)  # Set the size you want (width, height)
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize(size))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize(size))

label1 = tk.Label(window, image=image1)
label2 = tk.Label(window, image=image2)

label1.image = image1
label2.image = image2

label1.place(x=60, y=240)  # Left side
label2.place(x=340, y=240) # Right side

def dice_roll():
    random_num1 = random.randint(1, 6)  # Generate random number for dice 1
    random_num2 = random.randint(1, 6)  # Generate random number for dice 2

    image1 = ImageTk.PhotoImage(Image.open(dice[random_num1-1]).resize(size))
    label1.configure(image=image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(dice[random_num2-1]).resize(size))
    label2.configure(image=image2)
    label2.image = image2

    # Update the sum label
    total = random_num1 + random_num2
    sum_label.config(text=str(total))

# Create a rectangle box around the sum
sum_label = tk.Label(window, text="0", font="Times 20 bold", bd=4, relief="solid", width=3, height=1)
sum_label.place(x=200, y=150)  # Position of the sum label

button = tk.Button(window, text="ROLL", bg="green", fg="white", font="Times 20 bold", command=dice_roll)
button.place(x=180, y=0)  # Centered above the dice

window.mainloop()
