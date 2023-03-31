import tkinter as tk
from functools import partial
from tkinter import *
from database_controller import show_info, show_basics, show_interests


def Matching_Screen(i):
    root = tk.Tk()

    root.geometry('1920x1080')
    root.resizable(width=False, height=False)
    #root.attributes('-fullscreen', True)
    background = tk.PhotoImage(file="GUI/MAIN/match_img/match_background_img.png")


    label_background = tk.Label(root, image = background)
    label_background.pack()
    #----------------------------------------------------------------------------------------------------------------------------
    # Taskbar no click
    profile_img = tk.PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar/open_profile_button.png")
    matching_img = tk.PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar/open_matching_button.png")
    chat_img = tk.PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar/open_chat_button.png")

    # Taskbar click
    profile_click_img = tk.PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar_click/open_profile_button_click.png")
    matching_click_img = tk.PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar_click/open_match_button_click.png")
    chat_click_img = tk.PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar_click/open_chat_button_click.png")
    #----------------------------------------------------------------------------------------------------------------------------
    # LIKE - DISLIKE - CHANGE IMG
    like_img = tk.PhotoImage(file="GUI/MAIN/match_img/button_in_match_img/like.png")
    dislike_img = tk.PhotoImage(file="GUI/MAIN/match_img/button_in_match_img/dislike.png")
    change_img = tk.PhotoImage(file="GUI/MAIN/match_img/button_in_match_img/swap.png")
    #----------------------------------------------------------------------------------------------------------------------------

    def get_profile(i):
        infos = show_info()
        basics = show_basics()
        interests = show_interests()
        print(infos[i - 1], basics[i - 1], interests[i - 1])
        
    get_profile(i)




    # Interest
    #Sport
    gym_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/sport_img/gym.png")
    badminton_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/sport_img/badminton.png")
    boxing_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/sport_img/boxing.png")
    basketball_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/sport_img/basketball.png")

    #Creativity
    art_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/creativity_img/art.png")
    design_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/creativity_img/design.png")
    photography_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/creativity_img/photography.png")
    make_up_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/creativity_img/make_up.png")


    #Going out
    bars_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/going_out_img/bars.png")
    concert_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/going_out_img/concerts.png")
    cafe_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/going_out_img/cafe.png")
    museums_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/going_out_img/museums.png")


    #Staying in
    baking_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/staying_in_img/baking.png")
    board_game_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/staying_in_img/board_game.png")
    cooking_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/staying_in_img/cooking.png")
    gardening_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/staying_in_img/gardening.png")


    # Food & Drink
    pizza_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/food_drink_img/pizza.png")
    susshi_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/food_drink_img/sushi.png")
    sweet_tooth_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/food_drink_img/sweet_tooth.png")
    tea_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/food_drink_img/tea.png")


    # Traveling
    backpacking_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/traveling_img/backpacking.png")
    beaches_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/traveling_img/beaches.png")
    camping_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/traveling_img/camping.png")
    winter_sports_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/traveling_img/winter_sports.png")


    # Music
    classical_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/music_img/classical.png")
    edm_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/music_img/edm.png")
    r_b_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/music_img/r_b.png")
    rap_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/music_img/rap.png")


    # Film & TV
    action_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/film_tv_img/action.png")
    comedy_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/film_tv_img/comedy.png")
    horrow_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/film_tv_img/horrow.png")
    romance_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/film_tv_img/romance.png")


    # Reading
    history_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/reading_img/history.png")
    novel_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/reading_img/novel.png")
    poetry_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/reading_img/poetry.png")
    pschology_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/reading_img/pschology.png")


    # Pets
    bird_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/pets_img/bird.png")
    cat_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/pets_img/cat.png")
    dog_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/pets_img/dog.png")
    snake_img = tk.PhotoImage(file="GUI/MAIN/match_img/interest_match_img/pets_img/snake.png")
    #----------------------------------------------------------------------------------------------------------------------------

    # Show 5 Interests of USER 
    #Sport
    gym =  tk.Label(label_background, image=gym_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    gym.place(x = 1120, y = 800)  


    badminton =  tk.Label(label_background, image=badminton_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    badminton.place(x = 1320, y = 800)  


    boxing = tk.Label(label_background, image=boxing_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    boxing.place(x = 1119, y = 870)  


    basketball = tk.Label(label_background, image=basketball_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    basketball.place(x = 1119, y = 940)  



    #Creativity
    art = tk.Label(label_background, image=art_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    art.place(x = 1321, y = 870)  



    #----------------------------------------------------------------------------------------------------------------------------

    profile = tk.Button(label_background, image=profile_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    profile.place(x = 106, y = 440)  

    matching =  tk.Button(label_background, image=matching_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    matching.place(x = 105, y = 610)  

    chat =  tk.Button(label_background, image=chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    chat.place(x = 105, y = 760) 


    # Taskbar click
    profile_click =  tk.Button(label_background, image=profile_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    profile_click.place(x = 108, y = 440)  

    matching_click =  tk.Button(label_background, image=matching_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    matching_click.place(x = 107, y = 610)  

    chat_click =  tk.Button(label_background, image=chat_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    chat_click.place(x = 105, y = 760)  


    #----------------------------------------------------------------------------------------------------------------------------
    # LIKE - DISLIKE - CHANGE IMG - BUTTON 
    like = tk.Button(label_background, image=like_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    like.place(x = 900, y = 450)

    dislike = tk.Button(label_background, image=dislike_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    dislike.place(x = 900, y = 610)


    change = tk.Button(label_background, image=change_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    change.place(x = 900, y = 780)

    




    #----------------------------------------------------------------------------------------------------------------------------
    #Continue Button
    
   
    
    
    
    
    root.mainloop()
if __name__ == "__main__":
    Matching_Screen()