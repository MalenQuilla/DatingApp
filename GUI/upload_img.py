import tkinter as tk
import textwrap
from functools import partial
from tkinter import *


def Upload_Screen():
    root = tk.Tk()
    root.title("Profile Information")
    root.geometry('1440x900')
    root.resizable(width=False, height=False)



    background_img = tk.PhotoImage(file="GUI/upload_img/background_upload_img.png")
    continue_img = tk.PhotoImage(file="GUI/upload_img/continue_img.png")
    upload_img = tk.PhotoImage(file="GUI/upload_img/upload_button_img.png")

    label_background = tk.Label(root, image=background_img)
    label_background.pack()

    # continue_clickk = partial(root)
    
    upload_button= tk.Button(label_background, image=upload_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    upload_button.place(x = 220, y = 610)


    continue_button = tk.Button(label_background, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    continue_button.place(x = 1050, y = 500)



    
    root.mainloop()
if __name__ == "__main__":
    Upload_Screen()