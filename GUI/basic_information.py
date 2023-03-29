import tkinter as tk
import textwrap
from functools import partial
from tkinter import *
from database_controller import show_info, insert_baiscs

def continue_click(input_height, input_weight, zodiac, workout, smoke, drink, education, root):
    he = input_height.get()
    we = input_weight.get()
    wo = workout[0]
    smo = smoke[0]
    dri = drink[0]
    edu = education[0]
    print(he, we, zodiac, wo, smo, dri, edu)
    


def Basic_Infor():
    root = tk.Tk()
    root.title("Basics Information")

    root.geometry('1280x720')
    root.resizable(width=False, height=False)
    background = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/back_ground_basic_information.png")
    education_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/education_img.png")
    continue_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/continue.png")


    label_background = tk.Label(root, image = background)
    label_background.pack()
    # SKIP img of WorkOut,Smoke,Drink
    wo_smoke_drink_skip_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_smoke_drink_skip.png")
    wo_smoke_drink_skip_push__img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_smoke_drink_skip_push.png")




    #---------------------------------------------------------------------------------------------------------------------------------
    # Workout NO PUSH
    wo_active_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_img/wo_no_push/wo_active.png")
    wo_sometimes_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/WO_img/wo_no_push/wo_sometimes.png")
    wo_almost_never_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_img/wo_no_push/wo_almost_never.png")
    
    # Workout PUSH
    wo_active_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_img/wo_push/wo_active_push.png")
    wo_sometimes_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_img/wo_push/wo_sometimes_push.png")
    wo_almost_push_never_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/wo_img/wo_push/wo_almost_never_push.png")
    
    workout = ['None']
    
    def wo_active_click():
        wo_active_push = tk.Button(root, image=wo_active_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        wo_active_push.place(x=171,y=475)
        
        wo_sometimes = tk.Button(root, image=wo_sometimes_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_sometimes_clickk)
        wo_sometimes.place(x=171,y=525)
    
        wo_almost_never = tk.Button(root, image=wo_almost_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_never_clickk)
        wo_almost_never.place(x=171,y=575)

        wo_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_skip_clickk)
        wo_skip_no_push.place(x=171,y=625)
        
        workout[0] = "active"
    wo_active_clickk = partial(wo_active_click)
    wo_active = tk.Button(root, image=wo_active_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_active_clickk)
    wo_active.place(x=171,y=475)

    def wo_sometimes_click():
        wo_active = tk.Button(root, image=wo_active_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_active_clickk)
        wo_active.place(x=171,y=475)
        
        wo_sometimes_push = tk.Button(root, image=wo_sometimes_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        wo_sometimes_push.place(x=171,y=525)
    
        wo_almost_never = tk.Button(root, image=wo_almost_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_never_clickk)
        wo_almost_never.place(x=171,y=575)

        wo_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_skip_clickk)
        wo_skip_no_push.place(x=171,y=625)
        
        workout[0] = "sometimes"
    wo_sometimes_clickk = partial(wo_sometimes_click)
    wo_sometimes = tk.Button(root, image=wo_sometimes_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_sometimes_clickk)
    wo_sometimes.place(x=171,y=525)
    
    def wo_never_click():
        wo_active = tk.Button(root, image=wo_active_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_active_clickk)
        wo_active.place(x=171,y=475)
        
        wo_sometimes = tk.Button(root, image=wo_sometimes_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_sometimes_clickk)
        wo_sometimes.place(x=171,y=525)
    
        wo_almost_push_never = tk.Button(root, image=wo_almost_push_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        wo_almost_push_never.place(x=171,y=575)

        wo_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_skip_clickk)
        wo_skip_no_push.place(x=171,y=625)
        
        workout[0] = "almost never"
    wo_never_clickk = partial(wo_never_click)
    wo_almost_never = tk.Button(root, image=wo_almost_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_never_clickk)
    wo_almost_never.place(x=171,y=575)
    
    def wo_skip_click():
        wo_active = tk.Button(root, image=wo_active_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_active_clickk)
        wo_active.place(x=171,y=475)
        
        wo_sometimes = tk.Button(root, image=wo_sometimes_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_sometimes_clickk)
        wo_sometimes.place(x=171,y=525)
    
        wo_almost_never = tk.Button(root, image=wo_almost_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_never_clickk)
        wo_almost_never.place(x=171,y=575)

        wo_skip_push = tk.Button(root, image=wo_smoke_drink_skip_push__img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        wo_skip_push.place(x=171,y=625)
        
        workout[0] = "None"
    wo_skip_clickk = partial(wo_skip_click)
    wo_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= wo_skip_clickk)
    wo_skip_no_push.place(x=171,y=625)



    #---------------------------------------------------------------------------------------------------------------------------------
    # Smoke NO PUSH
    smoke_socially_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_no_push/smoke_socially.png")
    smoke_never_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_no_push/never.png")
    smoke_regularly_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_no_push/smoke_regularly.png")
    
    # Smoke PUSH
    smoke_socially_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_push/smoke_socially_push.png")
    smoke_never_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_push/never_push.png")
    smoke_regularly_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Smoke_img/smoke_push/regularly_push.png")
    
    
    smoke = ["None"]
    
    def smoke_social_click():
        smoke_socially_push = tk.Button(root, image=smoke_socially_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        smoke_socially_push.place(x=485,y=475)

        smoke_never = tk.Button(root, image=smoke_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_never_clickk)
        smoke_never.place(x=485,y=525)

        smoke_regularly = tk.Button(root, image=smoke_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_regu_clickk)
        smoke_regularly.place(x=485,y=575)

        smoke_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_skip_clickk)
        smoke_skip_no_push.place(x=485,y=625)
        
        smoke[0] = "socially"
    smoke_social_clickk = partial(smoke_social_click)
    smoke_socially = tk.Button(root, image=smoke_socially_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_social_clickk)
    smoke_socially.place(x=485,y=475)

    def smoke_never_click():
        smoke_socially = tk.Button(root, image=smoke_socially_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_social_clickk)
        smoke_socially.place(x=485,y=475)

        smoke_never_push = tk.Button(root, image=smoke_never_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        smoke_never_push.place(x=485,y=525)

        smoke_regularly = tk.Button(root, image=smoke_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_regu_clickk)
        smoke_regularly.place(x=485,y=575)

        smoke_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_skip_clickk)
        smoke_skip_no_push.place(x=485,y=625)
        
        smoke[0] = "never"
    smoke_never_clickk = partial(smoke_never_click)
    smoke_never = tk.Button(root, image=smoke_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_never_clickk)
    smoke_never.place(x=485,y=525)

    def smoke_regu_click():
        smoke_socially = tk.Button(root, image=smoke_socially_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_social_clickk)
        smoke_socially.place(x=485,y=475)

        smoke_never = tk.Button(root, image=smoke_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_never_clickk)
        smoke_never.place(x=485,y=525)

        smoke_regularly_push = tk.Button(root, image=smoke_regularly_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        smoke_regularly_push.place(x=485,y=575)

        smoke_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_skip_clickk)
        smoke_skip_no_push.place(x=485,y=625)
        
        smoke[0] = "regularly"
    smoke_regu_clickk = partial(smoke_regu_click)
    smoke_regularly = tk.Button(root, image=smoke_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_regu_clickk)
    smoke_regularly.place(x=485,y=575)
    
    def smoke_skip_click():
        smoke_socially = tk.Button(root, image=smoke_socially_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_social_clickk)
        smoke_socially.place(x=485,y=475)

        smoke_never = tk.Button(root, image=smoke_never_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_never_clickk)
        smoke_never.place(x=485,y=525)

        smoke_regularly = tk.Button(root, image=smoke_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_regu_clickk)
        smoke_regularly.place(x=485,y=575)

        smoke_skip_push = tk.Button(root, image=wo_smoke_drink_skip_push__img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        smoke_skip_push.place(x=485,y=625)
        
        smoke[0] = "None"
    smoke_skip_clickk = partial(smoke_skip_click)
    smoke_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= smoke_skip_clickk)
    smoke_skip_no_push.place(x=485,y=625)
    
    
    #---------------------------------------------------------------------------------------------------------------------------------




    #---------------------------------------------------------------------------------------------------------------------------------
    # Drink NO PUSH
    drink_frequently_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_no_push_img/drink_frequently.png")
    drink_rarely_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_no_push_img/drink_rarely.png")
    drink_regularly_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_no_push_img/drink_regularly.png")
    
    # Drink PUSH
    drink_frequently_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_push_img/drink_frequently_push.png")
    drink_rarely_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_push_img/drink_rarely_push.png")
    drink_regularly_push_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Drink_img/drink_push_img/drink_regularly_push.png")
    
    drink = ["None"]
    
    def drink_feq_click():
        drink_frequently_push = tk.Button(root, image=drink_frequently_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        drink_frequently_push.place(x=805,y=475)

        drink_rarely = tk.Button(root, image=drink_rarely_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_rar_clickk)
        drink_rarely.place(x=805,y=525)

        drink_regularly = tk.Button(root, image=drink_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_reg_clickk)
        drink_regularly.place(x=805,y=575)

        drink_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_skip_clickk)
        drink_skip_no_push.place(x=805,y=625)
        
        drink[0] = "frequently"
    drink_feq_clickk = partial(drink_feq_click)
    drink_frequently = tk.Button(root, image=drink_frequently_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_feq_clickk)
    drink_frequently.place(x=805,y=475)

    def drink_rar_click():
        drink_frequently = tk.Button(root, image=drink_frequently_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_feq_clickk)
        drink_frequently.place(x=805,y=475)

        drink_rarely_push = tk.Button(root, image=drink_rarely_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        drink_rarely_push.place(x=805,y=525)

        drink_regularly = tk.Button(root, image=drink_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_reg_clickk)
        drink_regularly.place(x=805,y=575)

        drink_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_skip_clickk)
        drink_skip_no_push.place(x=805,y=625)
        
        drink[0] = "rarely"
    drink_rar_clickk = partial(drink_rar_click)
    drink_rarely = tk.Button(root, image=drink_rarely_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_rar_clickk)
    drink_rarely.place(x=805,y=525)

    def drink_reg_click():
        drink_frequently = tk.Button(root, image=drink_frequently_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_feq_clickk)
        drink_frequently.place(x=805,y=475)

        drink_rarely = tk.Button(root, image=drink_rarely_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_rar_clickk)
        drink_rarely.place(x=805,y=525)

        drink_regularly_push = tk.Button(root, image=drink_regularly_push_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        drink_regularly_push.place(x=805,y=575)

        drink_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_skip_clickk)
        drink_skip_no_push.place(x=805,y=625)
        
        drink[0] = "regularly"
    drink_reg_clickk = partial(drink_reg_click)
    drink_regularly = tk.Button(root, image=drink_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_reg_clickk)
    drink_regularly.place(x=805,y=575)

    def drink_skip_click():
        drink_frequently = tk.Button(root, image=drink_frequently_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_feq_clickk)
        drink_frequently.place(x=805,y=475)

        drink_rarely = tk.Button(root, image=drink_rarely_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_rar_clickk)
        drink_rarely.place(x=805,y=525)

        drink_regularly = tk.Button(root, image=drink_regularly_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_reg_clickk)
        drink_regularly.place(x=805,y=575)

        drink_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_push__img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        drink_skip_no_push.place(x=805,y=625)
        
        drink[0] = "None"
    drink_skip_clickk = partial(drink_skip_click)
    drink_skip_no_push = tk.Button(root, image=wo_smoke_drink_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= drink_skip_clickk)
    drink_skip_no_push.place(x=805,y=625)

    #---------------------------------------------------------------------------------------------------------------------------------
    high_school_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/high_school.png")
    professional_college_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/professional_college.png")
    university_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/university.png")
    master_degree_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/master_degree.png")
    professor_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/professor.png")
    education_skip_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/skip.png")
    vocational_school_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Education_img/no_push/vocational_school.png")
    
    a = [0]
    education = ["None"]
    def education_click():
        match a[0]:
            case 0:
                high_school = tk.Button(root, image=high_school_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                high_school.place(x=521,y=263)
                education[0] = "high school"
            case 1:
                professional_college = tk.Button(root, image=professional_college_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                professional_college.place(x=520,y=261)
                education[0] = "professional college"
            case 2:
                university = tk.Button(root, image=university_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                university.place(x=522,y=262)
                education[0] = "university"
            case 3:
                master_degree = tk.Button(root, image=master_degree_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                master_degree.place(x=520,y=262)
                education[0] = "master degree"
            case 4:
                professor = tk.Button(root, image=professor_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                professor.place(x=522,y=261)
                education[0] = "professor"
            case 5:
                vocational_school = tk.Button(root, image=vocational_school_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                vocational_school.place(x=519,y=260)
                education[0] = "vocational school"
            case 6:
                education_skip = tk.Button(root, image=education_skip_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                education_skip.place(x=522,y=261)
                education[0] = "None"
        a[0] += 1
        if a[0] == 7: a[0] = 0
        
    education_clickk = partial(education_click)
    education_button = tk.Button(root, image =education_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= education_clickk)
    education_button.place(x=645,y=180)

    #---------------------------------------------------------------------------------------------------------------------------------
    
    #set zodiac
    infos = show_info()
    info = infos[-1]
    dob = info[1]
    components = dob.split('-')
    year, month, day = [int(item) for item in components]
    match month:
        case 12:
            zodiac = "sagitarius" if (day < 22) else "capricorn"
        case 1:
            zodiac = "capricorn" if (day < 20) else "aquarius"
        case 2:
            zodiac = "aquarius" if (day < 19) else "pisces"
        case 3:
            zodiac = "pisces" if (day < 21) else "aries"
        case 4:
            zodiac = "aries" if (day < 20) else "taurus"
        case 5:
            zodiac = "taurus" if (day < 21) else "gemini"
        case 6:
            zodiac = "gemini" if (day < 21) else "cancer"
        case 7:
            zodiac = "cancer" if (day < 23) else "leo"
        case 8:
            zodiac = "leo" if (day < 23) else "virgo"
        case 9:
            zodiac = "virgo" if (day < 23) else "libra"
        case 10:
            zodiac = "libra" if (day < 23) else "scorpio"
        case 11:
            zodiac = "scorpio" if (day < 22) else "sagittarius"
    
    #Zodiac
    aries_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/aries.png")
    taurus_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/taurus.png")
    gemini_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/gemini.png")
    cancer_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/cancer.png")
    leo_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/leo.png")
    virgo_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/virgo.png")
    libra_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/libra.png")
    scorpio_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/scorpio.png")
    sagittarius_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/sagittarius.png")
    capricorn_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/capricorn.png")
    aquarius_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/aquarius.png")
    pisces_img = tk.PhotoImage(file="GUI/sign_up_img/basic_information_img/Zodiac/pisces.png")
    
    match zodiac:
        case "aries":
            aries = tk.Label(label_background, image=aries_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            aries.place(x=861,y=260)
        case "taurus":
            taurus = tk.Label(label_background, image=taurus_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            taurus.place(x=859,y=260)
        case "gemini":
            gemini = tk.Label(label_background, image=gemini_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            gemini.place(x=861,y=260)
        case "cancer":
            cancer = tk.Label(label_background, image=cancer_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            cancer.place(x=859,y=260)
        case "leo":
            leo = tk.Label(label_background, image=leo_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            leo.place(x=861,y=260)
        case "virgo":
            virgo = tk.Label(label_background, image=virgo_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            virgo.place(x=860,y=260)
        case "libra":
            libra = tk.Label(label_background, image=libra_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            libra.place(x=859,y=260)
        case "scorpio":
            scorpio = tk.Label(label_background, image=scorpio_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            scorpio.place(x=861,y=260)
        case "sagittarius":
            sagittarius = tk.Label(label_background, image=sagittarius_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            sagittarius.place(x=861,y=260)
        case "capricorn":
            capricorn = tk.Label(label_background, image=capricorn_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            capricorn.place(x=861,y=260)
        case "aquarius":
            aquarius = tk.Label(label_background, image=aquarius_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            aquarius.place(x=860,y=260)
        case "pisces":
            pisces = tk.Label(label_background, image=pisces_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            pisces.place(x=859,y=260)
    


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

    weight = StringVar()
    input_weight = tk.Entry(label_background, textvariable = weight,width=18,bg="#FFFFFF", fg="#A9A9A9", font=("Arial", 14))
    input_weight.insert(0, " ?kg") # Insert opaque text into input_weight
    input_weight.bind("<FocusIn>", Input_Weight) # Attach event on click on input_weight
    input_weight.bind("<FocusOut>", Input_Weight_Focus_Out) # Hook event on hover out of input_weight
    input_weight.place(x=230, y=253)
    input_weight.configure(borderwidth=0, highlightthickness=0)
    
    
    #----------------------------------------------------------------------------------------------------------------------------
    #Continue Button
    
    continue_clickk = partial(continue_click, height, weight, zodiac, workout, smoke, drink, education, root)
    
    continue_button = tk.Button(label_background, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= continue_clickk)
    continue_button.place(x = 1050, y = 500)
    
    
    
    
    
    root.mainloop()