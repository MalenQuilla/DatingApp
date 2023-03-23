from tkinter import *
from functools import partial
import os
import time
from signUpScreen import createScreen as signUpcreateScreen

def noUser(Screen):
    error = PhotoImage(file = "GUI/Login/error_screen.png")
    Error = Label(Screen, image = error).place(x = 700, y = 450) 
    Error.image = error

def login(username, password, Screen):
    un = username.get() 
    print(un)
    pw = password.get()
    try:
        path = os.path.realpath('DatingAppProject/Data/Users/' + str(un)) 
        with open(path + "/Password.txt", "r+") as f:
            print("done")
            true_pw = f.readline()
            print(true_pw)
            if pw != true_pw:
                return noUser(Screen)
    except IOError:
        return noUser(Screen)

def signup(Screen):
    Screen.destroy()
    return signUpcreateScreen()

def createScreen():
    
    Screen = Tk()
    Screen.geometry("900x500")
    Screen.resizable(width=False, height=False)
    Screen.title("Login")
    bg = PhotoImage(file = "GUI/Login/login_screen.png")
    Confirm = PhotoImage(file = "GUI/Login/Confirm_button.png")
    Signup = PhotoImage(file = "GUI/Login/Sign_up.png")
    Label(Screen, image = bg).place(x=0, y=0, relwidth = 1, relheight = 1)
    
    username = StringVar()
    password = StringVar()
    Entry(Screen, textvariable = username, width = 30, borderwidth = 0, highlightthickness = 0).place(x = 160, y = 210)
    Entry(Screen, textvariable = password, show = "*", width = 30, borderwidth = 0, highlightthickness = 0).place(x = 160, y = 265)
    
    Login = partial(login, username, password, Screen)
    Sign_up = partial(signup, Screen)
    Button(Screen, image = Confirm, command = Login, borderwidth = 0, highlightthickness = 0).place(x = 125, y = 310)
    Button(Screen, image = Signup, command = Sign_up, borderwidth = 0, highlightthickness = 0).place(x = 125, y = 370)
    
    Screen.mainloop()  


createScreen()