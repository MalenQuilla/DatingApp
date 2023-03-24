import tkinter as tk
import re

root = tk.Tk() # Create new window
root.geometry('900x500')
root.resizable(width=False, height=False)

# Export Background Sign up image from available photo library
background = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/background_sign_up.png")    

# Export User Name of Password image from available photo library                         
special_character = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/user_name_or_password__special_character.png")

# Export Password not Match from available photo library   
incorrect_password = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/password_not_match.png")

# Export Continue image from available photo library   
continue_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/continue.png")



label_background = tk.Label(root, image=background)
label_background.pack()






# Input User Name Sign up
def Input_User_Name_Sign_Up(event):
    if  input_user_name_sign_up.get() == "User Name":
        input_user_name_sign_up.delete(0, "end") # Remove blurry text
        input_user_name_sign_up.configure(fg="#000000")
        
# def Input_User_Name_Sign_Up_FocusOut(event):
#     if not  input_user_name_sign_up.get():
#             input_user_name_sign_up.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
#             input_user_name_sign_up.insert(0, "User Name")
#     else:
#             Notification_Special_Character(user_name_sign_up.get())

user_name_sign_up = tk.StringVar()

input_user_name_sign_up = tk.Entry(label_background, textvariable = user_name_sign_up, width=32,bg="#FFF9F5", fg="#A9A9A9", font=("Arial", 14))
input_user_name_sign_up.insert(0, "User Name") # Insert opaque text into input_user_name_sign_up
input_user_name_sign_up.bind("<FocusIn>", Input_User_Name_Sign_Up) # Attach event on click on input_user_name_sign_up
# input_user_name_sign_up.bind("<FocusOut>", Input_User_Name_Sign_Up_FocusOut) # Hook event on hover out of input_user_name_sign_up
input_user_name_sign_up.place(x=290, y=210)
input_user_name_sign_up.configure(borderwidth=0, highlightthickness=0)





# Input Password Sign Up
def Input_Password_Sign_Up(event):
    if  input_password.get() == "Password":
        input_password.delete(0, "end") # Remove blurry text
        input_password.configure(fg="#000000")
        input_password.configure(show="*")

# def Input_Password_Sign_Up_FocusOut(event):
#     if not input_password.get():
#         input_password.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
#         input_password.insert(0, "Password")
#         input_password.configure(show = "")
#     else:
#         Notification_not_Match_Password(password_sign_up.get())

password_sign_up = tk.StringVar()

input_password = tk.Entry(label_background, textvariable = password_sign_up,width=32,bg="#FFF9F5", fg="#A9A9A9", font=("Arial", 14))
input_password.insert(0, "Password") # Insert opaque text into input_password
input_password.bind("<FocusIn>", Input_Password_Sign_Up) # Attach event on click on input_password
# input_password.bind("<FocusOut>", Input_Password_Sign_Up_FocusOut) # Hook event on hover out of input_password
input_password.place(x=290, y=285)
input_password.configure(borderwidth=0, highlightthickness=0)



# Input Confirm Password Sign Up
def Input_Confirm_Password_Sign_Up(event):
    if  input_cofirm_password_sign_up.get() == "Confirm Password":
        input_cofirm_password_sign_up.delete(0, "end") # Remove blurry text
        input_cofirm_password_sign_up.configure(fg="#000000")
        input_cofirm_password_sign_up.configure(show="*")

# def Input_Cofirm_Password_Sign_Up_FocusOut(event):
#     if not input_cofirm_password_sign_up.get():
#         input_cofirm_password_sign_up.configure(fg="#A9A9A9")
#         input_cofirm_password_sign_up.insert(0, "Confirm Password")
#         input_cofirm_password_sign_up.configure(show = "")
#     elif input_cofirm_password_sign_up.get() != input_password.get():
#         Incorrect_Notification()



confirm_password_sign_up = tk.StringVar()

input_cofirm_password_sign_up = tk.Entry(label_background, textvariable = confirm_password_sign_up,width=32,bg="#FFF9F5", fg="#A9A9A9", font=("Arial", 14))
input_cofirm_password_sign_up.insert(0, "Confirm Password") # Insert opaque text into input_cofirm_password_sign_up
input_cofirm_password_sign_up.bind("<FocusIn>", Input_Confirm_Password_Sign_Up) # Attach event on click on input_cofirm_password_sign_up
# input_cofirm_password_sign_up.bind("<FocusOut>", Input_Cofirm_Password_Sign_Up_FocusOut) # Hook event on hover out of input_cofirm_password_sign_up
input_cofirm_password_sign_up.place(x=290, y=360)
input_cofirm_password_sign_up.configure(borderwidth=0, highlightthickness=0)



def Incorrect_Notification():
    incorrect_password_Notification = tk.Label(label_background, image=incorrect_password)
    incorrect_password_Notification.configure(bg ="#FFF7F3")
    incorrect_password_Notification.place(x=273, y=325)
    incorrect_password_Notification.configure(borderwidth=0, highlightthickness=0)



def Notification_Special_Character(user_name_sign_up, password_sign_up,confirm_password_sign_up):
    if not (user_name_sign_up.isalnum() and password_sign_up.isalnum() and confirm_password_sign_up.isalnum()):
        Incorrect_Notification()
        return True
    return False
def Notification_not_Match_Password():
    if password_sign_up.get() != confirm_password_sign_up.get():
        Incorrect_Notification()
        # Delete anything input
        input_user_name_sign_up.delete(0, tk.END)
        input_password.delete(0, tk.END)
        input_cofirm_password_sign_up.delete(0, tk.END)
        return True
    elif user_name_sign_up.get() == password_sign_up.get():
        Incorrect_Notification()
        # Delete anything input
        input_user_name_sign_up.delete(0, tk.END)
        input_password.delete(0, tk.END)
        input_cofirm_password_sign_up.delete(0, tk.END)
        return True
    elif user_name_sign_up.get() == confirm_password_sign_up.get():
        Incorrect_Notification()
        # Delete anything input
        input_user_name_sign_up.delete(0, tk.END)
        input_password.delete(0, tk.END)
        input_cofirm_password_sign_up.delete(0, tk.END)
        return True              
    return False
def Right_Input():
    if user_name_sign_up.get() != confirm_password_sign_up.get() and user_name_sign_up.get() != password_sign_up.get() and password_sign_up.get() == confirm_password_sign_up.get(): 
        if re.search(r'[\\|/\'"<>.?{}[\];]', user_name_sign_up):
            return False
        else:
            return True
    return False


def Button_Continue():
    if Notification_not_Match_Password():
        return False
    if Right_Input():
        return True

continue_button = tk.Button(label_background, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command=Button_Continue)
continue_button.place(x=375, y=415)



root.mainloop()
