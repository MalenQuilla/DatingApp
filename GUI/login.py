import tkinter as tk
from functools import partial
from database_controller import show_account

def confirm_click(username, password, root):
    un = username.get()
    pw = password.get()
    accounts = show_account()
    for account in accounts:
        if un != account[0] or pw != account[1]:
            confirm_error(root)
        else:
            print("login success")
    
def confirm_error(root):
    error = tk.PhotoImage(file = "GUI/login_img/Error_message.png")
    Error = tk.Label(root, image = error, borderwidth = 0, highlightthickness = 0).place(x = 80, y = 140)
    Error.image = error
    
def sign_up_click():
    # Registration processing
    pass

def forgot_password_click():
    # Registration processing
    pass

def login_screen():
    root = tk.Tk()  # Create new window
    root.title('Sign In')
    root.geometry('900x500')
    root.resizable(width=False, height=False)


    background = tk.PhotoImage(file="GUI/login_img/Background.png")                 # Export Background image from available photo library
    sign_up = tk.PhotoImage(file="GUI/login_img/Sign_up_button.png")                     # Export Sign image from available photo library
    confirm = tk.PhotoImage(file="GUI/login_img/Confirm_button.png")                     # Export Confirm image from available photo library
    forgot_password = tk.PhotoImage(file="GUI/login_img/Forgot_password_button.png")    # Export Forgot Password image from available photo library


    #------------------------------------------------------
    label_background = tk.Label(root, image=background)
    label_background.pack()
    
    #------------------------------------------------------
    
    def InputUserName(event):
        if input_user_name.get() == "User Name":
            input_user_name.delete(0, "end") # Remove blurry text
            input_user_name.configure(fg="#000000")
    def InputUserNameFocusOut(event):
        if not input_user_name.get():
            input_user_name.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
            input_user_name.insert(0, "User Name")

    username = tk.StringVar()

    input_user_name = tk.Entry(label_background, textvariable = username, width=25, fg="#A9A9A9", font=("Arial", 14))
    input_user_name.insert(0, "User Name") # Insert opaque text into input_user_name
    input_user_name.bind("<FocusIn>", InputUserName) # Attach event on click on input_user_name
    input_user_name.bind("<FocusOut>", InputUserNameFocusOut) # Hook event on hover out of input_user_name
    input_user_name.place(x=95, y=175)
    input_user_name.configure(borderwidth=0, highlightthickness=0)

    #------------------------------------------------------
    
    def InputPassword(event):
        if input_password.get() == "Password":
            input_password.delete(0, "end") # Remove blurry text
            input_password.configure(fg="#000000", show = "*")
    def InputPasswordFocusOut(event):
        if not input_password.get():
            input_password.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
            input_password.insert(0, "Password")

    password = tk.StringVar()

    input_password = tk.Entry(label_background, textvariable = password, width=25, fg="#A9A9A9", font=("Arial", 14))
    input_password.insert(0, "Password") # Insert opaque text into input_password
    input_password.bind("<FocusIn>", InputPassword) # Attach event on click on input_password
    input_password.bind("<FocusOut>", InputPasswordFocusOut) # Hook event on hover out of input_password
    input_password.place(x=95, y=260)
    input_password.configure(borderwidth=0, highlightthickness=0)

    #------------------------------------------------------

    sign_up_button = tk.Button(label_background, image=sign_up, borderwidth=0, highlightthickness=0, command = sign_up_click)
    sign_up_button.place(x=291, y=462)
    sign_up_button.configure(highlightthickness=0)

    con_button = partial(confirm_click, username, password, root)
    confirm_button = tk.Button(label_background, image=confirm, borderwidth=0, highlightthickness=0, command = con_button)
    confirm_button.place(x=230, y=330)
    confirm_button.configure(highlightthickness=0)

    forgot_password_button = tk.Button(label_background, image=forgot_password, bg = "#F4E0EA",  borderwidth=0, highlightthickness=0, command = forgot_password_click, activebackground="#F4E0EA")
    forgot_password_button.place(x=89, y=348)
    forgot_password_button.configure(highlightthickness=0)

    root.mainloop()
    