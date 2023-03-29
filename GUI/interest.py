import tkinter as tk
import textwrap
from functools import partial
from tkinter import *
# from database_controller import show_info, insert_baiscs


def Interest_Screen():
    root = tk.Tk()
    root.title("Basics Information")

    root.geometry('1280x800')
    root.resizable(width=False, height=False)
    background = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/background_img.png")

    continue_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/continue_img.png")

    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind(
        '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
    )
    second_frame = Frame(my_canvas, width = 1280, height = 1921)
    label_background = tk.Label(second_frame, image = background)
    label_background.pack()
    my_canvas.create_window((0, 0), window= second_frame, anchor="nw")








    #----------------------------------------------------------------------------------------------------------------------------    
    #Interest 

    #Sport
    gym_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/gym.png")
    badminton_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/badminton.png")
    boxing_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/boxing.png")
    basketball_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/sport_img/basketball.png")

    #Creativity
    design_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/design.png")
    photograph_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/photography.png")
    art_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/art.png")
    make_up_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/creativity_img/make-up.png")

    #Going out
    bars_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/bars.png")
    concerts_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/concerts.png")
    museums_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/museums.png") 
    cafe_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/going_out_img/cake.png")

    #Stayng in
    baking_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/baking.png") 
    cooking_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/cooking.png")
    board_game_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/board_game.png") 
    gardening_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/staying_in_img/gardening.png")
    #----------------------------------------------------------------------------------------------------------------------------   
    #Interest CLICK

    #Sport CLICK
    gym_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/sport_img/gym.png")
    badminton_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/sport_img/badminton.png")
    boxing_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/sport_img/boxing.png")
    basketball_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/sport_img/basketball.png")

    #Creativity CLICK
    design_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/creativity_img/design.png")
    photograph_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/creativity_img/photograph.png")
    art_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/creativity_img/art.png")
    make_up_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/creativity_img/make_up.png")

    #Going out CLICK
    bars_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/going_out_img/bars.png")
    concerts_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/going_out_img/concerts.png")
    museums_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/going_out_img/museums.png") 
    cafe_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/going_out_img/cafe.png")

    #Stayng in CLICK
    baking_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/baking.png") 
    cooking_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/cooking.png")
    board_game_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/board_game.png") 
    gardening_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/staying_in_img/gardening.png")








    #----------------------------------------------------------------------------------------------------------------------------

    #Sport
    def gym_click():
        gym = tk.Button(second_frame, image=gym_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(gym_unclick))
        gym.place(x=130,y=248)
    def gym_unclick():
        gym = tk.Button(second_frame, image=gym_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(gym_click))
        gym.place(x = 131, y = 250)
    gym_unclick()
    
    def badminton_click():
        badminton = tk.Button(second_frame, image=badminton_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(badminton_unclick))
        badminton.place(x = 130, y = 335)
    def badminton_unclick():
        badminton = tk.Button(second_frame, image=badminton_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(badminton_click))
        badminton.place(x = 130, y = 335)
    badminton_unclick()    
    
    def boxing_click():
        boxing = tk.Button(second_frame, image=boxing_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(boxing_unclick))
        boxing.place(x= 352, y= 246)
    def boxing_unclick():
        boxing = tk.Button(second_frame, image=boxing_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(boxing_click))
        boxing.place(x = 355, y = 250)
    boxing_unclick()
    
    def basketball_click():
        basketball = tk.Button(second_frame, image=basketball_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(basketball_unclick))
        basketball.place(x= 353, y= 332)
    def basketball_unclick():
        basketball = tk.Button(second_frame, image=basketball_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(basketball_click))
        basketball.place(x = 355, y = 335)
    basketball_unclick()

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Creativity
    def design_click():
        design_click = tk.Button(second_frame, image=design_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(design_unclick))
        design_click.place(x = 732, y = 251)
    def design_unclick():
        design = tk.Button(second_frame, image=design_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(design_click))
        design.place(x = 731, y = 250)
    design_unclick()
    
    def photograph_click():
        photograph = tk.Button(second_frame, image=photograph_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(photograph_unclick))
        photograph.place(x = 731, y = 334)
    def photograph_unclick():
        photograph = tk.Button(second_frame, image=photograph_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(photograph_click))
        photograph.place(x = 730, y = 335)
    photograph_unclick()
    
    def art_click():
        art = tk.Button(second_frame, image=art_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(art_unclick))
        art.place(x = 957, y = 250)
    def art_unclick():
        art = tk.Button(second_frame, image=art_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(art_click))
        art.place(x = 955, y = 250)
    art_unclick()

    def make_up_click():
        make_up = tk.Button(second_frame, image=make_up_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(make_up_unclick))
        make_up.place(x = 955, y = 335)
    def make_up_unclick():
        make_up = tk.Button(second_frame, image=make_up_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(make_up_click))
        make_up.place(x = 955, y = 333)
    make_up_unclick()
    
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Going out
    def bars_click():
        bars = tk.Button(second_frame, image=bars_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(bars_unclick))
        bars.place(x = 129, y = 557)
    def bars_unclick():
        bars = tk.Button(second_frame, image=bars_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(bars_click))
        bars.place(x = 132, y = 560)
    bars_unclick()

    def concerts_click():
        concerts = tk.Button(second_frame, image=concerts_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(concerts_unclick))
        concerts.place(x = 128, y = 638)
    def concerts_unclick():
        concerts = tk.Button(second_frame, image=concerts_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(concerts_click))
        concerts.place(x = 130, y = 639)
    concerts_unclick() 

    def museums_click():
        museums = tk.Button(second_frame, image=museums_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(museums_unclick))
        museums.place(x = 353, y = 558)
    def museums_unclick():
        museums = tk.Button(second_frame, image=museums_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(museums_click))
        museums.place(x = 355, y = 560)
    museums_unclick() 

    def cafe_click():
        cafe = tk.Button(second_frame, image=cafe_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cafe_unclick))
        cafe.place(x = 354, y = 638)
    def cafe_unclick():
        cafe = tk.Button(second_frame, image=cafe_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cafe_click))
        cafe.place(x = 355, y = 639)
    cafe_unclick() 
    
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Stayng in CLICK
    def baking_click():
        baking = tk.Button(second_frame, image=baking_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(baking_unclick))
        baking.place(x = 732, y = 560)
    def baking_unclick():
        baking = tk.Button(second_frame, image=baking_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(baking_click))
        baking.place(x = 732, y = 563)
    baking_unclick() 

    def cooking_click():
        cooking = tk.Button(second_frame, image=cooking_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cooking_unclick))
        cooking.place(x = 730, y = 641)
    def cooking_unclick():
        cooking = tk.Button(second_frame, image=cooking_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cooking_click))
        cooking.place(x = 731, y = 640)
    cooking_unclick() 

    def board_game_click():
        board_game = tk.Button(second_frame, image=board_game_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(board_game_unclick))
        board_game.place(x = 954, y = 559)
    def board_game_unclick():
        board_game = tk.Button(second_frame, image=board_game_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(board_game_click))
        board_game.place(x = 955, y = 560)
    board_game_unclick() 

    def gardening_click():
        gardening = tk.Button(second_frame, image=gardening_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(gardening_unclick))
        gardening.place(x = 952, y = 638)
    def gardening_unclick():
        gardening = tk.Button(second_frame, image=gardening_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(gardening_click))
        gardening.place(x = 954, y = 640)
    gardening_unclick() 
    






    #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Traveling
    backpacking_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/backpacking.png") 
    beaches_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/beaches.png") 
    winter_sports_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/winter_sports.png") 
    camping_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/traveling_img/camping.png")

    #Food & Drink
    sushi_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/sushi.png")
    pizza_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/pizza.png") 
    sweet_tooth_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/sweet_tooth.png")
    tea_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/food_drink_img/tea.png")
    
    #Music
    classical_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/music_img/classical.png") 
    r_b_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/music_img/R&B.png")
    edm_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/music_img/edm.png")
    rap_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/music_img/rap.png")

    #Flim & TV
    action_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/action.png")
    romance_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/romance.png")
    comedy_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/comedy.png")
    horror_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/film_tv_img/horror.png")
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Button no Click of Traveling -- Food & Drink --  Music -- Flim & TV
    #Traveling CLICK
    backpacking_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/traveling_img/backpacking.png") 
    beaches_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/traveling_img/beaches.png") 
    winter_sports_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/traveling_img/winter_sports.png") 
    camping_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/traveling_img/camping.png")

    #Food & Drink CLICK
    sushi_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/sushi.png")
    pizza_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/pizza.png") 
    sweet_tooth_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/sweet_tooth.png")
    tea_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/food_drink_img/tea.png")
    
    #Music CLICK
    classical_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/music_img/classical.png") 
    r_b_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/music_img/R&B.png")
    edm_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/music_img/edm.png")
    rap_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/music_img/rap.png")

    #Flim & TV CLICK
    action_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/action.png")
    romance_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/romance.png")
    comedy_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/comedy.png")
    horror_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/film_tv_img/horror.png")


    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------














    #Traveling
    def backpacking_click():
        backpacking = tk.Button(second_frame, image=backpacking_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(backpacking_unclick))
        backpacking.place(x = 130, y = 864)
    def backpacking_unclick():
        backpacking = tk.Button(second_frame, image=backpacking_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(backpacking_click))
        backpacking.place(x = 131, y = 865)
    backpacking_unclick() 

    def beaches_click():
        beaches = tk.Button(second_frame, image=beaches_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(beaches_unclick))
        beaches.place(x = 128, y = 943)
    def beaches_unclick():
        beaches = tk.Button(second_frame, image=beaches_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(beaches_click))
        beaches.place(x = 131, y = 944)
    beaches_unclick() 

    def winter_sports_click():
        winter_sports = tk.Button(second_frame, image=winter_sports_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(winter_sports_unclick))
        winter_sports.place(x = 354, y = 866)
    def winter_sports_unclick():
        winter_sports = tk.Button(second_frame, image=winter_sports_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(winter_sports_click))
        winter_sports.place(x = 355, y = 865)
    winter_sports_unclick() 

    def camping_click():
        camping = tk.Button(second_frame, image=camping_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(camping_unclick))
        camping.place(x = 354, y = 944)
    def camping_unclick():
        camping = tk.Button(second_frame, image=camping_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(camping_click))
        camping.place(x = 355, y = 945)
    camping_unclick() 
    
    # Food & Drink
    def sushi_click():
        sushi = tk.Button(second_frame, image=sushi_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(sushi_unclick))
        sushi.place(x = 732, y = 867)
    def sushi_unclick():
        sushi = tk.Button(second_frame, image=sushi_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(sushi_click))
        sushi.place(x = 731, y = 867)
    sushi_unclick() 
    
    def pizza_click():
        pizza = tk.Button(second_frame, image=pizza_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(pizza_unclick))
        pizza.place(x = 730, y = 945)
    def pizza_unclick():
        pizza = tk.Button(second_frame, image=pizza_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(pizza_click))
        pizza.place(x = 732, y = 949)
    pizza_unclick() 

    def sweet_tooth_click():
        sweet_tooth = tk.Button(second_frame, image=sweet_tooth_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(sweet_tooth_unclick))
        sweet_tooth.place(x = 955, y = 864)
    def sweet_tooth_unclick():
        sweet_tooth = tk.Button(second_frame, image=sweet_tooth_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(sweet_tooth_click))
        sweet_tooth.place(x = 955, y = 866)
    sweet_tooth_unclick() 
    
    def tea_click():
        tea = tk.Button(second_frame, image=tea_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(tea_unclick))
        tea.place(x = 952, y = 945)
    def tea_unclick():
        tea = tk.Button(second_frame, image=tea_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(tea_click))
        tea.place(x = 954, y = 948)
    tea_unclick()


    
    #Music
    def classical_click():
        classical = tk.Button(second_frame, image=classical_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(classical_unclick))
        classical.place(x = 127, y = 1171)
    def classical_unclick():
        classical = tk.Button(second_frame, image=classical_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(classical_click))
        classical.place(x = 130, y = 1173)
    classical_unclick()

    def r_b_click():
        r_b = tk.Button(second_frame, image=r_b_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(r_b_unclick))
        r_b.place(x = 128, y = 1251)
    def r_b_unclick():
        r_b = tk.Button(second_frame, image=r_b_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(r_b_click))
        r_b.place(x = 130, y = 1254)
    r_b_unclick()

    def edm_click():
        edm = tk.Button(second_frame, image=edm_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(edm_unclick))
        edm.place(x = 355, y = 1170)
    def edm_unclick():
        edm = tk.Button(second_frame, image=edm_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(edm_click))
        edm.place(x = 355, y = 1174)
    edm_unclick()
    
    def rap_click():
        rap = tk.Button(second_frame, image=rap_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(rap_unclick))
        rap.place(x = 356, y = 1253)
    def rap_unclick():
        rap = tk.Button(second_frame, image=rap_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(rap_click))
        rap.place(x = 356, y = 1255)
    rap_unclick()
    

    #Flim & TV
    def action_click():
        action = tk.Button(second_frame, image=action_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(action_unclick))
        action.place(x = 750, y = 1180)
    def action_unclick():
        action = tk.Button(second_frame, image=action_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(action_click))
        action.place(x = 732, y = 1172)
    action_unclick()
    
    def romance_click():
        romance = tk.Button(second_frame, image=romance_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(romance_unclick))
        romance.place(x = 731, y = 1253)
    def romance_unclick():
        romance = tk.Button(second_frame, image=romance_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(romance_click))
        romance.place(x = 731, y = 1253)
    romance_unclick()
    
    def comedy_click():
        comedy = tk.Button(second_frame, image=comedy_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(comedy_unclick))
        comedy.place(x = 957, y = 1173)
    def comedy_unclick():
        comedy = tk.Button(second_frame, image=comedy_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(comedy_click))
        comedy.place(x = 955, y = 1172)
    comedy_unclick()
    
    def action_click():
        action = tk.Button(second_frame, image=action_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(action_unclick))
        action.place(x = 734, y = 1173)
    def action_unclick():
        action = tk.Button(second_frame, image=action_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(action_click))
        action.place(x = 733, y = 1172)
    action_unclick()
    
    def horror_click():
        horror = tk.Button(second_frame, image=horror_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(horror_unclick))
        horror.place(x = 954, y = 1254)
    def horror_unclick():
        horror = tk.Button(second_frame, image=horror_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(horror_click))
        horror.place(x = 955, y = 1253)
    horror_unclick()
    












    #-------------------------------------------------------------------------------------------------------------------------------------------------------

    #Reading
    history_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/history.png")
    novel_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/novel.png")
    poetry_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/poetry.png")
    pschology_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/reading_img/pschology.png")

    #Pets
    dog_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/dog.png")
    cat_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/cat.png")
    snake_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/snake.png")
    bird_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_no_click_img/pets_img/bird.png")

    #Reading CLICK
    history_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/reading_img/history.png")
    novel_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/reading_img/novel.png")
    poetry_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/reading_img/poetry.png")
    pschology_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/reading_img/psychology.png")

    #Pets CLICK
    dog_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/pets_img/dog.png")
    cat_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/pets_img/cat.png")
    snake_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/pets_img/snake.png")
    bird_click_img = tk.PhotoImage(file="DatingAppProject/GUI/sign_up_img/interest_img/interest_click_img/pets_img/bird.png")
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------











    # Button no Click of Reading and Pets

    def history_click():
        history = tk.Button(second_frame, image=history_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(history_unclick))
        history.place(x = 129, y = 1477)
    def history_unclick():
        history = tk.Button(second_frame, image=history_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(history_click))
        history.place(x = 130, y = 1478)
    history_unclick()
    
    def novel_click():
        novel = tk.Button(second_frame, image=novel_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(novel_unclick))
        novel.place(x = 128, y = 1558)
    def novel_unclick():
        novel = tk.Button(second_frame, image=novel_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(novel_click))
        novel.place(x = 129, y = 1561)
    novel_unclick()

    def poetry_click():
        poetry = tk.Button(second_frame, image=poetry_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(poetry_unclick))
        poetry.place(x = 353, y = 1476)
    def poetry_unclick():
        poetry = tk.Button(second_frame, image=poetry_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(poetry_click))
        poetry.place(x = 355, y = 1478)
    poetry_unclick()

    def pschology_click():
        pschology = tk.Button(second_frame, image=pschology_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(pschology_unclick))
        pschology.place(x = 349, y = 1557)
    def pschology_unclick():
        pschology = tk.Button(second_frame, image=pschology_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(pschology_click))
        pschology.place(x = 354, y = 1561)
    pschology_unclick()



    # Button no Click of Reading and Pets
    def dog_click():
        dog = tk.Button(second_frame, image=dog_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(dog_unclick))
        dog.place(x = 729, y = 1480)
    def dog_unclick():
        dog = tk.Button(second_frame, image=dog_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(dog_click))
        dog.place(x = 732, y = 1482)
    dog_unclick()
    
    def cat_click():
        cat = tk.Button(second_frame, image=cat_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cat_unclick))
        cat.place(x = 730, y = 1560)
    def cat_unclick():
        cat = tk.Button(second_frame, image=cat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(cat_click))
        cat.place(x = 732, y = 1564)
    cat_unclick()
    
    def snake_click():
        snake = tk.Button(second_frame, image=snake_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(snake_unclick))
        snake.place(x = 954, y = 1479)
    def snake_unclick():
        snake = tk.Button(second_frame, image=snake_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(snake_click))
        snake.place(x = 957, y = 1480)
    snake_unclick()
    
    def bird_click():
        bird = tk.Button(second_frame, image=bird_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(bird_unclick))
        bird.place(x = 955, y = 1562)
    def bird_unclick():
        bird = tk.Button(second_frame, image=bird_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0,command= partial(bird_click))
        bird.place(x = 955, y = 1563)
    bird_unclick()

















    #----------------------------------------------------------------------------------------------------------------------------
    #Continue Button
    
    # continue_clickk = partial(continue_click, height, weight, zodiac, workout, smoke, drink, education, second_frame)
    
    continue_button = tk.Button(second_frame, image=continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    continue_button.place(x = 539, y = 1750)
    root.mainloop()

if __name__ == "__main__":
    Interest_Screen()

