from tkinter import *
from functools import partial

def createScreen():
    Screen = Tk()
    Screen.geometry("900x500")
    Screen.resizable(width=False, height=False)
    Screen.title("Create Account")
    bg = PhotoImage(file = "GUI/Login/login_screen.png")
    Label(Screen, image = bg).place(x=0, y=0, relwidth = 1, relheight = 1)
    
    Screen.mainloop()