import tkinter as tk
from functools import partial
from tkinter import *
from GUI import login


def next_click(root):
    root.destroy()
    login.login_screen()

def Letter_Thanks_Screen():
    root = tk.Tk()
    root.title("Basics Information")

    root.geometry('900x500')
    root.resizable(width=False, height=False)
    background = tk.PhotoImage(file="GUI/letter_thanks_img/background.png")
    next_img = tk.PhotoImage(file="GUI/letter_thanks_img/next.png")


    label_background = tk.Label(root, image = background)
    label_background.pack()

    #----------------------------------------------------------------------------------------------------------------------------
    
    #Continue Button
    
    
    next_button = tk.Button(label_background, image=next_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(next_click, root))
    next_button.place(x = 370, y = 400)
    
    
    root.mainloop()