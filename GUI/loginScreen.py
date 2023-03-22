from tkinter import *
from functools import partial
from signUpScreen import createScreen as signUpcreateScreen

def login(username, password):
    return username, password

def signup(Screen):
    Screen.destroy()
    return signUpcreateScreen(Screen)

def createScreen(Screen):
    Screen = Tk()
    Screen.geometry("400x250")
    Screen.title("Login")
    username = StringVar()
    password = StringVar()
    l1 = Label(Screen, text = "Username").place(x = 70, y = 90)
    l2 = Label(Screen, text = "Password").place(x = 70, y = 130)
    e1 = Entry(Screen, textvariable = username).place(x = 130, y = 90)
    e2 = Entry(Screen, textvariable = password, show = "*").place(x = 130, y = 130)
    Login = partial(login, username, password)
    loginButton = Button(Screen, text = "Login", command = Login).place(x = 260, y = 123)
    Signup = partial(signup, Screen)
    createAccButton = Button(Screen, text = "Sign up here", command = Signup).place(x = 130, y = 160)
    
    Screen.mainloop()  
