import tkinter as tk
from functools import partial
from database_controller import show_account, insert_account

def continue_click(username, password, confirm_password, root):
    un = username.get()
    pw = password.get()
    cpw = confirm_password.get()
    accounts = show_account()
    for account in accounts:
        if account[0] == un or un == "User Name":
            Error1(root)
    if un == pw:
        Error2(root)
    elif pw != cpw:
        Error3(root)
    else:
        print("sign up successful")
        insert_account(un, pw)
        
def Error1(root):
    error = tk.PhotoImage(file = "GUI/sign_up_img/username_already_exist.png")
    Error = tk.Label(root, image = error, borderwidth=0, highlightthickness=0).place(x = 276, y = 178)      
    Error.image = error

def Error2(root):   
    error = tk.PhotoImage(file = "GUI/sign_up_img/cannot_match.png")
    Error = tk.Label(root, image = error, borderwidth=0, highlightthickness=0).place(x = 273, y = 253)      
    Error.image = error
    
def Error3(root):  
    password_unmatch = tk.PhotoImage(file="GUI/sign_up_img/doesnt_match.png")
    password_unmatch_Notification = tk.Label(root, image = password_unmatch)
    password_unmatch_Notification.configure(bg ="#FFF7F3")
    password_unmatch_Notification.place(x=273, y=325)
    password_unmatch_Notification.configure(borderwidth=0, highlightthickness=0)
    password_unmatch_Notification.image = password_unmatch
    
    

def sign_up_screen():
    root = tk.Tk() # Create new window
    root.title("Sign Up")
    root.geometry('900x500')
    root.resizable(width=False, height=False)

    #import picture
    background = tk.PhotoImage(file="GUI/sign_up_img/background_sign_up.png")    
    continue_img = tk.PhotoImage(file="GUI/sign_up_img/continue.png")


    label_background = tk.Label(root, image=background)
    label_background.pack()

    #---------------------------------------------------------------------------------------------------------------------
    # Input User Name Sign up
    def Input_User_Name_Sign_Up(event):
        if  input_user_name_sign_up.get() == "User Name":
            input_user_name_sign_up.delete(0, "end") # Remove blurry text
            input_user_name_sign_up.configure(fg="#000000")
    def InputUserNameFocusOut(event):
        if not input_user_name_sign_up.get():
            input_user_name_sign_up.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
            input_user_name_sign_up.insert(0, "User Name")
            
    user_name_sign_up = tk.StringVar()

    input_user_name_sign_up = tk.Entry(label_background, textvariable = user_name_sign_up, width=32,bg="#FFF9F5", fg="#A9A9A9", font=("Arial", 14))
    input_user_name_sign_up.insert(0, "User Name") # Insert opaque text into input_user_name_sign_up
    input_user_name_sign_up.bind("<FocusIn>", Input_User_Name_Sign_Up) # Attach event on click on input_user_name_sign_up
    input_user_name_sign_up.bind("<FocusOut>", InputUserNameFocusOut) # Hook event on hover out of input_user_name
    input_user_name_sign_up.place(x=290, y=210)
    input_user_name_sign_up.configure(borderwidth=0, highlightthickness=0)

    #---------------------------------------------------------------------------------------------------------------------
    # Input Password Sign Up
    def Input_Password_Sign_Up(event):
        if  input_password.get() == "Password":
            input_password.delete(0, "end") # Remove blurry text
            input_password.configure(fg="#000000")
            input_password.configure(show="*")
    def InputPasswordFocusOut(event):
        if not input_password.get():
            input_password.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
            input_password.insert(0, "Password")
            input_password.configure(show="")

    password_sign_up = tk.StringVar()

    input_password = tk.Entry(label_background, textvariable = password_sign_up,width=32,bg="#FFF9F5", fg="#A9A9A9", font=("Arial", 14))
    input_password.insert(0, "Password") # Insert opaque text into input_password
    input_password.bind("<FocusIn>", Input_Password_Sign_Up) # Attach event on click on input_password
    input_password.bind("<FocusOut>", InputPasswordFocusOut) # Hook event on hover out of input_password
    input_password.place(x=290, y=285)
    input_password.configure(borderwidth=0, highlightthickness=0)

    #---------------------------------------------------------------------------------------------------------------------
    # Input Confirm Password Sign Up
    def Input_Confirm_Password_Sign_Up(event):
        if  input_cofirm_password_sign_up.get() == "Confirm Password":
            input_cofirm_password_sign_up.delete(0, "end") # Remove blurry text
            input_cofirm_password_sign_up.configure(fg="#000000")
            input_cofirm_password_sign_up.configure(show="*")
    def Input_Cofirm_Password_Sign_Up_FocusOut(event):
        if not input_cofirm_password_sign_up.get():
            input_cofirm_password_sign_up.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
            input_cofirm_password_sign_up.insert(0, "Confirm Password")
            input_cofirm_password_sign_up.configure(show="")

    confirm_password_sign_up = tk.StringVar()

    input_cofirm_password_sign_up = tk.Entry(label_background, textvariable = confirm_password_sign_up,width=32,bg="#FFF9F5", fg="#A9A9A9", font=("Arial", 14))
    input_cofirm_password_sign_up.insert(0, "Confirm Password") # Insert opaque text into input_cofirm_password_sign_up
    input_cofirm_password_sign_up.bind("<FocusIn>", Input_Confirm_Password_Sign_Up) # Attach event on click on input_cofirm_password_sign_up
    input_cofirm_password_sign_up.bind("<FocusOut>", Input_Cofirm_Password_Sign_Up_FocusOut) # Hook event on hover out of input_cofirm_password_sign_up
    input_cofirm_password_sign_up.place(x=290, y=360)
    input_cofirm_password_sign_up.configure(borderwidth=0, highlightthickness=0)


    #---------------------------------------------------------------------------------------------------------------------

    con_button = partial(continue_click, user_name_sign_up, password_sign_up, confirm_password_sign_up, root)
    
    continue_button = tk.Button(label_background, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command = con_button)
    continue_button.place(x=375, y=415)


    root.mainloop()
