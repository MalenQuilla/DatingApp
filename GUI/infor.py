import tkinter as tk
import textwrap
from functools import partial
from tkinter import *
from database_controller import insert_info
from GUI import basic_information


def continue_click(input_name, input_dob, input_location, input_bio, gender, root):
    na = input_name.get()
    dob = input_dob.get()
    loca = input_location.get()
    bi = input_bio.get()
    if bi == "Tell something in your Bio..." or bi == '':
        bi = "Looking for short/long-term dating and new friends."
    gen = gender[0]
    insert_info(na, dob, gen, loca, bi)
    print("set info success")
    root.destroy()
    basic_information.Basic_Infor()


def Infor_screen():
    root = tk.Tk()
    root.title("Profile Information")
    root.geometry('900x500')
    root.resizable(width=False, height=False)

    background_img = tk.PhotoImage(file = "GUI/sign_up_img/profile_information_img/new_bg.png")
    continue_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/continue.png")
    male_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/male.png")
    female_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/female.png")
    les_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/les.png")
    gay_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/gay.png")
    bi_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/bi.png")
    
    male_click_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/male_click.png")
    female_click_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/female_click.png")
    les_click_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/les_click.png")
    gay_click_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/gay_click.png")
    bi_click_img = tk.PhotoImage(file="GUI/sign_up_img/profile_information_img/bi_click.png")

    

    label_background = tk.Label(root, image=background_img)
    label_background.pack()
    #--------------------------------------------------------------------------------------------------------------------

    gender = ['None']
    
    def MALE():
        gender[0] = "male"
        Label(root, image=male_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0).place(x = 718, y= 250)
    def FEMALE():
        gender[0] = "female"
        Label(root, image=female_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0).place(x = 718, y= 250)
    def LES():
        gender[0] = "les"
        Label(root, image=les_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0).place(x = 720, y= 251)
    def GAY():
        gender[0] = "gay"
        Label(root, image=gay_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0).place(x = 719, y= 250)
    def BI():
        gender[0] = "bi-sexual"
        Label(root, image=bi_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0).place(x = 720, y= 250)
    

    male_button = tk.Button(label_background, image=male_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command = MALE)
    male_button.place(x = 480, y= 177)

    female_button = tk.Button(label_background, image=female_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= FEMALE)
    female_button.place(x = 600, y= 180)

    les_button = tk.Button(label_background, image=les_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= LES)
    les_button.place(x = 720, y= 179)

    gay_button = tk.Button(label_background, image=gay_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= GAY)
    gay_button.place(x = 485, y= 250)

    bi_button = tk.Button(label_background, image=bi_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= BI)
    bi_button.place(x = 598, y= 250)


    #--------------------------------------------------------------------------------------------------------------------
    def Input_Name(event):
        if  input_name.get() == "Full Name":
            input_name.delete(0, "end") # Remove blurry text
            input_name.configure(fg="#000000")
    def Input_Name_Focus_Out(event):
        if not input_name.get():
            input_name.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
            input_name.insert(0, "Full Name")
    name = tk.StringVar()
    input_name = tk.Entry(label_background, textvariable = name, width=29,bg="#FFFDFC", fg="#A9A9A9", font=("Arial", 14))  
    input_name.insert(0, "Full Name") # Insert opaque text into input_name
    input_name.bind("<FocusIn>", Input_Name) # Attach event on click on input_name
    input_name.bind("<FocusOut>", Input_Name_Focus_Out) # Hook event on hover out of input_user_name
    input_name.place(x=73, y=195)
    input_name.configure(borderwidth=0, highlightthickness=0)

    #--------------------------------------------------------------------------------------------------------------------
    def Input_dob(event):
        if  input_dob.get() == "DOB (YYYY-MM-DD)":
            input_dob.delete(0, "end")
            input_dob.configure(fg="#000000")
    def Input_dob_Focus_Out(event):
        if not input_dob.get():
            input_dob.configure(fg="#A9A9A9")
            input_dob.insert(0, "DOB (YYYY-MM-DD)")
    dob = tk.StringVar()
 
    input_dob = tk.Entry(label_background, textvariable=dob, width=29, bg="#FFFDFC", fg ="#A9A9A9", font=("Arial, 14"))
    input_dob.insert(0, "DOB (YYYY-MM-DD)")
    input_dob.bind("<FocusIn>", Input_dob)
    input_dob.bind("<FocusOut>", Input_dob_Focus_Out)
    input_dob.place(x = 73, y = 268)
    input_dob.configure(borderwidth=0, highlightthickness=0)
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



    conti_button = partial(continue_click, name, dob, location, bio, gender, root)
    
    continue_button = tk.Button(label_background, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command = conti_button)
    continue_button.place(x=150, y=395)

    root.mainloop()
