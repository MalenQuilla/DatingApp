import tkinter as tk
import textwrap
from functools import partial
from tkinter import *


def Letter_Thanks_Screen():
    root = tk.Tk()
    root.title("Basics Information")

    root.geometry('900x500')
    root.resizable(width=False, height=False)
    background = tk.PhotoImage(file="DatingAppProject/GUI/letter_thanks_img/background.png")
    next_img = tk.PhotoImage(file="DatingAppProject/GUI/letter_thanks_img/next.png")


    label_background = tk.Label(root, image = background)
    label_background.pack()
    # SKIP img of WorkOut,Smoke,Drink

    #----------------------------------------------------------------------------------------------------------------------------
    #Continue Button
    
    
    next_button = tk.Button(label_background, image=next_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    next_button.place(x = 100, y = 50)
    
    
    
    
    
    root.mainloop()
if __name__ == "__main__":
    Letter_Thanks_Screen()