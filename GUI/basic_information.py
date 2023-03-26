import tkinter as tk
import textwrap
from functools import partial
from tkinter import *
# from database_controller import insert_info

def continue_click(input_height, input_weight, root):
    he = input_height.get()
    we = input_weight.get()
    


def Basic_Infor():
    root = tk.Tk()
    root.title("Basic Information")

    root.geometry('1280x720')
    root.resizable(width=False, height=False)
    background = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/back_ground_basic_information.png")
    education_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/education_img.png")
    continue_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/continue.png")


    label_background = tk.Label(root, image = background)
    label_background.pack()
    # SKIP img of WorkOut,Smoke,Drink
    wo_smoke_drink_skip_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/wo_smoke_drink_skip.png")
    wo_smoke_drink_skip_push__img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/wo_smoke_drink_skip_push.png")




    #---------------------------------------------------------------------------------------------------------------------------------
    # Workout NO PUSH
    wo_active_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/wo_img/wo_no_push/wo_active.png")
    wo_active = tk.Button(label_background, image=wo_active_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    wo_active.place(x=171,y=475)

    wo_sometimes_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/WO_img/wo_no_push/wo_sometimes.png")
    wo_sometimes = tk.Button(label_background, image=wo_sometimes_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    wo_sometimes.place(x=171,y=525)


    wo_almost_never_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/wo_img/wo_no_push/wo_almost_never.png")
    wo_almost_never = tk.Button(label_background, image=wo_almost_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    wo_almost_never.place(x=171,y=575)

    wo_skip_no_push = tk.Button(label_background, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    wo_skip_no_push.place(x=171,y=625)

    # Workout PUSH
    wo_active_push_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/wo_img/wo_push/wo_active_push.png")
    wo_active_push = tk.Button(label_background, image=wo_active_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    wo_active_push.place(x=171,y=475)

    wo_sometimes_push_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/wo_img/wo_push/wo_sometimes_push.png")
    wo_sometimes_push = tk.Button(label_background, image=wo_sometimes_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    wo_sometimes_push.place(x=171,y=525)

    wo_almost_push_never_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/wo_img/wo_push/wo_almost_never_push.png")
    wo_almost_push_never = tk.Button(label_background, image=wo_almost_push_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    wo_almost_push_never.place(x=171,y=575)

    wo_skip_push = tk.Button(label_background, image=wo_smoke_drink_skip_push__img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    wo_skip_push.place(x=171,y=625)
    #---------------------------------------------------------------------------------------------------------------------------------






    #---------------------------------------------------------------------------------------------------------------------------------
    # Smoke NO PUSH
    smoke_socially_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Smoke_img/smoke_no_push/smoke_socially.png")
    smoke_socially = tk.Button(label_background, image=smoke_socially_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    smoke_socially.place(x=485,y=475)

    smoke_never_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Smoke_img/smoke_no_push/never.png")
    smoke_never = tk.Button(label_background, image=smoke_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    smoke_never.place(x=485,y=525)

    smoke_regularly_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Smoke_img/smoke_no_push/smoke_regularly.png")
    smoke_regularly = tk.Button(label_background, image=smoke_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    smoke_regularly.place(x=485,y=575)

    smoke_skip_no_push = tk.Button(label_background, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    smoke_skip_no_push.place(x=485,y=625)


    # Smoke PUSH
    smoke_socially_push_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Smoke_img/smoke_push/smoke_socially_push.png")
    smoke_socially_push = tk.Button(label_background, image=smoke_socially_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    smoke_socially_push.place(x=485,y=475)

    smoke_never_push_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Smoke_img/smoke_push/never_push.png")
    smoke_never_push = tk.Button(label_background, image=smoke_never_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    smoke_never_push.place(x=485,y=525)

    smoke_regularly_push_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Smoke_img/smoke_push/regularly_push.png")
    smoke_regularly_push = tk.Button(label_background, image=smoke_regularly_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    smoke_regularly_push.place(x=485,y=575)

    smoke_skip_push = tk.Button(label_background, image=wo_smoke_drink_skip_push__img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    smoke_skip_push.place(x=485,y=625)
    #---------------------------------------------------------------------------------------------------------------------------------




    #---------------------------------------------------------------------------------------------------------------------------------
    # Drink NO PUSH
    drink_frequently_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Drink_img/drink_no_push_img/drink_frequently.png")
    drink_frequently = tk.Button(label_background, image=drink_frequently_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    drink_frequently.place(x=805,y=475)

    drink_rarely_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Drink_img/drink_no_push_img/drink_rarely.png")
    drink_rarely = tk.Button(label_background, image=drink_rarely_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    drink_rarely.place(x=805,y=525)

    drink_regularly_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Drink_img/drink_no_push_img/drink_regularly.png")
    drink_regularly = tk.Button(label_background, image=drink_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    drink_regularly.place(x=805,y=575)

    drink_skip_no_push = tk.Button(label_background, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    drink_skip_no_push.place(x=805,y=625)


    # Drink PUSH
    drink_frequently_push_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Drink_img/drink_push_img/drink_frequently_push.png")
    drink_frequently_push = tk.Button(label_background, image=drink_frequently_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    drink_frequently_push.place(x=805,y=475)

    drink_rarely_push_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Drink_img/drink_push_img/drink_rarely_push.png")
    drink_rarely_push = tk.Button(label_background, image=drink_rarely_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    drink_rarely_push.place(x=805,y=525)

    drink_regularly_push_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Drink_img/drink_push_img/drink_regularly_push.png")
    drink_regularly_push = tk.Button(label_background, image=drink_regularly_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    drink_regularly_push.place(x=805,y=575)

    drink_skip_no_push = tk.Button(label_background, image=wo_smoke_drink_skip_push__img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    drink_skip_no_push.place(x=805,y=625)
    #---------------------------------------------------------------------------------------------------------------------------------

    








    #----------------------------------------------------------------------------------------------------------------------------
    education = tk.Button(label_background, image =education_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    education.place(x=645,y=180)
    
    #Continue Button
    continue_button = tk.Button(label_background, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    continue_button.place(x = 1050, y = 500)

    #----------------------------------------------------------------------------------------------------------------------------
    def Input_Height(event):
        if  input_height.get() == "1m??":
            input_height.delete(0, "end") # Remove blurry text
            input_height.configure(fg="#000000")
    def Input_Height_Focus_Out(event):
        if not input_height.get():
            input_height.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
            input_height.insert(0, "1m??")

    height = StringVar()
    input_height = tk.Entry(label_background, textvariable = height,width=18,bg="#FFFFFF", fg="#A9A9A9", font=("Arial", 14))
    input_height.insert(0, "1m??") # Insert opaque text into input_height
    input_height.bind("<FocusIn>", Input_Height) # Attach event on click on input_height
    input_height.bind("<FocusOut>", Input_Height_Focus_Out) # Hook event on hover out of input_height
    input_height.place(x=230, y=170)
    input_height.configure(borderwidth=0, highlightthickness=0)
    #----------------------------------------------------------------------------------------------------------------------------
    def Input_Weight(event):
        if  input_weight.get() == " ?kg":
            input_weight.delete(0, "end") # Remove blurry text
            input_weight.configure(fg="#000000")
    def Input_Weight_Focus_Out(event):
        if not input_weight.get():
            input_weight.configure(fg="#A9A9A9") # Restore the color of the input box's watermark
            input_weight.insert(0, " ?kg")

    height = StringVar()
    input_weight = tk.Entry(label_background, textvariable = height,width=18,bg="#FFFFFF", fg="#A9A9A9", font=("Arial", 14))
    input_weight.insert(0, " ?kg") # Insert opaque text into input_weight
    input_weight.bind("<FocusIn>", Input_Weight) # Attach event on click on input_weight
    input_weight.bind("<FocusOut>", Input_Weight_Focus_Out) # Hook event on hover out of input_weight
    input_weight.place(x=230, y=253)
    input_weight.configure(borderwidth=0, highlightthickness=0)
    root.mainloop()
    



if __name__ == '__main__':
    Basic_Infor()