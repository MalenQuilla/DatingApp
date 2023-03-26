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

    



    #Education NO PUSH
    hight_school_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/no_push/high_school.png")
    hight_school = tk.Button(label_background, image=hight_school_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    hight_school.place(x=519,y=261)

    professional_college_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/no_push/professional_college.png")
    professional_college = tk.Button(label_background, image=professional_college_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    professional_college.place(x=518,y=260)

    university_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/no_push/university.png")
    university = tk.Button(label_background, image=university_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    university.place(x=519,y=263)

    master_degree_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/no_push/master_degree.png")
    master_degree = tk.Button(label_background, image=master_degree_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    master_degree.place(x=518,y=261)

    professor_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/no_push/professor.png")
    professor = tk.Button(label_background, image=professor_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    professor.place(x=520,y=260)

    vocational_school_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/no_push/vocational_school.png")
    vocational_school = tk.Button(label_background, image=vocational_school_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    vocational_school.place(x=517,y=260)

    education_skip_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/skip.png")
    education_skip = tk.Button(label_background, image=education_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    education_skip.place(x=520,y=260)









    #Education PUSH
    hight_school_img_push = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/push/high_school_push.png")
    hight_school_img = tk.Button(label_background, image=hight_school_img_push, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    hight_school_img.place(x=519,y=261)

    professional_college_img_push = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/push/professional_college_push.png")
    professional_college_img = tk.Button(label_background, image=professional_college_img_push, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    professional_college_img.place(x=518,y=261)

    university_img_push = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/push/university_push.png")
    university_img = tk.Button(label_background, image=university_img_push, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    university_img.place(x=518,y=261)

    master_degree_img_push = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/push/master_degree_put.png")
    master_degree_img = tk.Button(label_background, image=master_degree_img_push, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    master_degree_img.place(x=518,y=261)

    professor_img_push = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/push/professor_push.png")
    professor_img = tk.Button(label_background, image=professor_img_push, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    professor_img.place(x=519,y=261)

    vocational_school_img_push = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Education_img/push/vocational_school_push.png")
    vocational_school_img = tk.Button(label_background, image=vocational_school_img_push, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    vocational_school_img.place(x=519,y=260)

    education_skip_push_img_push = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/skip_push.png")
    education_skip_push_img = tk.Button(label_background, image=education_skip_push_img_push, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    education_skip_push_img.place(x=519,y=261)

















    #Zodiac
    aries_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/aries.png")
    aries = tk.Label(label_background, image=aries_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    aries.place(x=861,y=260)

    taurus_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/taurus.png")
    taurus = tk.Label(label_background, image=taurus_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    taurus.place(x=859,y=260)

    gemini_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/gemini.png")
    gemini = tk.Label(label_background, image=gemini_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    gemini.place(x=861,y=260)

    cancer_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/cancer.png")
    cancer = tk.Label(label_background, image=cancer_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    cancer.place(x=859,y=260)

    leo_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/leo.png")
    leo = tk.Label(label_background, image=leo_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    leo.place(x=861,y=260)

    virgo_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/virgo.png")
    virgo = tk.Label(label_background, image=virgo_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    virgo.place(x=860,y=260)

    libra_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/libra.png")
    libra = tk.Label(label_background, image=libra_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    libra.place(x=859,y=260)

    scorpio_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/scorpio.png")
    scorpio = tk.Label(label_background, image=scorpio_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    scorpio.place(x=861,y=260)

    sagittarius_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/sagittarius.png")
    sagittarius = tk.Label(label_background, image=sagittarius_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    sagittarius.place(x=861,y=260)

    capricorn_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/capricorn.png")
    capricorn = tk.Label(label_background, image=capricorn_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    capricorn.place(x=861,y=260)

    aquarius_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/aquarius.png")
    aquarius = tk.Label(label_background, image=aquarius_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    aquarius.place(x=860,y=260)

    pisces_img = tk.PhotoImage(file="DatingAppProject/GUI/basic_information_img/Zodiac/pisces.png")
    pisces = tk.Label(label_background, image=pisces_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    pisces.place(x=859,y=260)
    







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