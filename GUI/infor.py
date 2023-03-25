import tkinter as tk
import textwrap
from functools import partial
from tkinter import *


def continue_click(input_name, input_age, input_location, input_bio, root):
    na = input_name.get()
    ag = input_age.get()
    loca = input_location.get()
    bi = input_bio.get()


def Infor_screen():
    root = tk.Tk()
    root.title("Profile Information")
    root.geometry('900x500')
    root.resizable(width=False, height=False)

    background_img = tk.PhotoImage(file = "DatingAppProject/GUI/profile_information_img/new_bg.png")
    continue_img = tk.PhotoImage(file="DatingAppProject/GUI/profile_information_img/continue.png")
    male_img = tk.PhotoImage(file="DatingAppProject/GUI/profile_information_img/male.png")
    female_img = tk.PhotoImage(file="DatingAppProject/GUI/profile_information_img/female.png")
    les_img = tk.PhotoImage(file="DatingAppProject/GUI/profile_information_img/les.png")
    gay_img = tk.PhotoImage(file="DatingAppProject/GUI/profile_information_img/gay.png")
    bi_img = tk.PhotoImage(file="DatingAppProject/GUI/profile_information_img/bi.png")

    

    label_background = tk.Label(root, image=background_img)
    label_background.pack()
    #--------------------------------------------------------------------------------------------------------------------

    button_number = 0


    male_button = tk.Button(label_background, image=male_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    male_button.place(x = 480, y= 180)

    female_button = tk.Button(label_background, image=female_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    female_button.place(x = 600, y= 180)

    les_button = tk.Button(label_background, image=les_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    les_button.place(x = 720, y= 179)

    gay_button = tk.Button(label_background, image=gay_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    gay_button.place(x = 485, y= 250)

    bi_button = tk.Button(label_background, image=bi_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    bi_button.place(x = 598, y= 250)





    #--------------------------------------------------------------------------------------------------------------------
    def Input_Name(event):
        if  input_name.get() == "Name":
            input_name.delete(0, "end") # Remove blurry text
            input_name.configure(fg="#000000")
    def Input_Name_Focus_Out(event):
        if not input_name.get():
            input_name.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
            input_name.insert(0, "Name")
    name = tk.StringVar()
    input_name = tk.Entry(label_background, textvariable = name, width=29,bg="#FFFDFC", fg="#A9A9A9", font=("Arial", 14))  
    input_name.insert(0, "Name") # Insert opaque text into input_name
    input_name.bind("<FocusIn>", Input_Name) # Attach event on click on input_name
    input_name.bind("<FocusOut>", Input_Name_Focus_Out) # Hook event on hover out of input_user_name
    input_name.place(x=73, y=195)
    input_name.configure(borderwidth=0, highlightthickness=0)

    #--------------------------------------------------------------------------------------------------------------------
    def Input_Age(event):
        if  input_age.get() == "Age":
            input_age.delete(0, "end")
            input_age.configure(fg="#000000")
    def Input_Age_Focus_Out(event):
        if not input_age.get():
            input_age.configure(fg="#A9A9A9")
            input_age.insert(0, "Age")
    age = tk.StringVar()
 
    input_age = tk.Entry(label_background, textvariable=age, width=29, bg="#FFFDFC", fg ="#A9A9A9", font=("Arial, 14"))
    input_age.insert(0, "Age")
    input_age.bind("<FocusIn>", Input_Age)
    input_age.bind("<FocusOut>", Input_Age_Focus_Out)
    input_age.place(x = 73, y = 268)
    input_age.configure(borderwidth=0, highlightthickness=0)
    #--------------------------------------------------------------------------------------------------------------------
    def Input_Location(event):
        if input_location.get() == "Location":
            input_location.delete(0, "end")
            input_location.configure(fg = "#000000")
    def Input_Location_Focus_Out(event):
        if not input_location.get():
            input_location.configure(fg="#A9A9A9")
            input_location.insert(0,"Location")
    location = tk.StringVar()

    input_location = tk.Entry(label_background, textvariable=location, width=29,bg ="#FFFDFC", fg= "#A9A9A9", font=("Arial", 14))
    input_location.insert(0, "Location")
    input_location.bind("<FocusIn>", Input_Location)
    input_location.bind("<FocusOut>", Input_Location_Focus_Out)
    input_location.place(x = 73, y= 343)
    input_location.configure(borderwidth=0, highlightthickness=0)

    #--------------------------------------------------------------------------------------------------------------------
    
    def Input_Some_Thing_Bio(event):
        if input_bio.get() == "Tell something in your Bio...":
            input_bio.delete(0, "end")
            input_bio.configure(fg = "#000000")
    def Input_Some_Thing_Bio_Focus_Out(event):
        if not input_bio.get():
            input_bio.configure(fg="#A9A9A9")
            input_bio.insert(0,"Tell something in your Bio...")
    bio = tk.StringVar()

    input_bio = tk.Entry(label_background, textvariable = bio, width=28,bg ="#FFF3EC", fg= "#A9A9A9", font=("Arial", 14))
    input_bio.insert(0, "Tell something in your Bio...")
    input_bio.bind("<FocusIn>", Input_Some_Thing_Bio)
    input_bio.bind("<FocusOut>", Input_Some_Thing_Bio_Focus_Out)
    input_bio.place(x = 500, y= 355)
    input_bio.configure(borderwidth=0, highlightthickness=0)



    conti_button = partial(continue_click, name, age, location, bio, root)
    
    continue_button = tk.Button(label_background, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command = conti_button)
    continue_button.place(x=150, y=395)

    root.mainloop()

   


if __name__ == '__main__':
    Infor_screen()
