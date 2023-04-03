from functools import partial
from tkinter import *
from tkextrafont import Font
import datetime
from io import BytesIO
from math import floor, ceil
from PIL import Image, ImageTk
from database_controller import show_info, show_basics, show_interests, show_photo
from Matching_Controller import Randomize

def return_status():
    return new_status

def exit_click(root):
    global new_status 
    new_status = "exit"
    root.destroy()
    
def matching_click(root):
    global new_status
    new_status = "matching"
    root.destroy()
    
def profile_click(root):
    global new_status
    new_status = "profile"
    root.destroy()
    
def chat_click(root):
    global new_status
    new_status = "chat"
    root.destroy()
    
def Profile_screen(user_id, status):
  
    root = Tk()

    root.geometry('1920x1080')
    root.resizable(width=False, height=False)
    root.attributes('-fullscreen', True)
    background = PhotoImage(file="GUI/MAIN/match_img/background.png")


    font = Font(file="GUI/MAIN/Be_Vietnam_Pro/BeVietnamPro-ExtraBold.ttf")

    label_background = Label(root, image = background)
    label_background.pack()
    
    #----------------------------------------------------------------------------------------------------------------------------
    # Taskbar no click
    profile_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar/open_profile_button.png")
    matching_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar/open_matching_button.png")
    chat_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar/open_chat_button.png")
    exit_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar/exit_button.png")

    # Taskbar click
    profile_click_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar_click/open_profile_button_click.png")
    matching_click_img = PhotoImage(file="GUI/MAIN/match_img/task_bar_img/taskbar_click/open_match_button_click.png")
    #----------------------------------------------------------------------------------------------------------------------------
    # LIKE - DISLIKE - CHANGE IMG
    like_img = PhotoImage(file="GUI/MAIN/match_img/button_in_match_img/like.png")
    dislike_img = PhotoImage(file="GUI/MAIN/match_img/button_in_match_img/dislike.png")
    change_img = PhotoImage(file="GUI/MAIN/match_img/button_in_match_img/swap.png")
    
    #----------------------------------------------------------------------------------------------------------------------------
    infos = show_info()
    basics = show_basics()
    interestss = show_interests()
    
    def display(i):
        #display info
        info = infos[i]
        name_data = info[0].split(' ')
        
        age_datas = info[1].split('-')
        today = datetime.date.today()
        year = today.year
        age_data = - int(age_datas[0]) + int(year)
        
        bio_data = info[4]
        
        gender_data = info[2]
        
        location_data = info[3]
        
        name = StringVar()
        name.set("About " + name_data[-1])
        Label(root, textvariable = name, bg = "#FFEEF6", fg="#4E4E4E", font=(font, 19, "bold")).place(x = 1120, y = 365)
        
        age = StringVar()
        age.set(name_data[-1] + ", " + str(age_data))
        Label(root, textvariable = age, bg = "#FFEEF6", fg="#4E4E4E", font=(font, 35, "bold")).place(x = 1117, y = 280)
        
        bio = StringVar()
        bio.set(bio_data)
        Label(root, textvariable=bio, wraplengt = 400, justify= "left", bg = "#FFEEF6", fg="#4E4E4E", font=(font, 13, "bold")).place(x = 1140, y = 430)
        
        gender = StringVar()
        gender.set(gender_data)
        Label(root, textvariable=gender, bg = "#FFEEF6", fg="#4E4E4E", font=(font, 16, "bold")).place(x = 1170, y = 562)
        
        location = StringVar()
        location.set(location_data)
        Label(root, textvariable=location, bg = "#FFEEF6", fg="#4E4E4E", font=(font, 16, "bold")).place(x = 1370, y = 615)
        
        #----------------------------------------------------------------------------------------------------------------------------
        #display basics
        basic = basics[i]
        
        height_data = basic[0]
        
        zodiac_data = basic[2]
        
        education_data = basic[3]
        
        workout_data = basic[4]
        
        smoke_data = basic[5]
        
        drink_data = basic[6]
        
        height = StringVar()
        height.set(height_data)
        Label(root, textvariable = height, bg = "#FFEEF6", fg="#4E4E4E", font=(font, 16, "bold")).place(x = 1170, y = 615)  
        
        zodiac = StringVar()
        zodiac.set(zodiac_data)
        Label(root, textvariable = zodiac, bg = "#FFEEF6", fg="#4E4E4E", font=(font, 16, "bold")).place(x = 1370, y = 742)     
        
        education = StringVar()
        education.set(education_data)
        Label(root, textvariable = education, bg = "#FFEEF6", fg="#4E4E4E", font=(font, 16, "bold")).place(x = 1370, y = 562)    
        
        workout = StringVar()
        workout.set(workout_data)
        Label(root, textvariable = workout, bg = "#FFEEF6", fg="#4E4E4E", font=(font, 16, "bold")).place(x = 1170, y = 742)     
        
        smoke = StringVar()
        smoke.set(smoke_data)
        Label(root, textvariable = smoke, bg = "#FFEEF6", fg="#4E4E4E", font=(font, 16, "bold")).place(x = 1370, y = 679)  
        
        drink = StringVar()
        drink.set(drink_data)
        Label(root, textvariable = drink, bg = "#FFEEF6", fg="#4E4E4E", font=(font, 16, "bold")).place(x = 1170, y = 679)    
                
        #----------------------------------------------------------------------------------------------------------------------------
        #display interests
        interests = interestss[i]
        
        interest1 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[0] + ".png")
        inter_img1 = Label(root, image= interest1, borderwidth=0, highlightthickness=0)
        inter_img1.place(x = 1120, y = 800)
        inter_img1.image = interest1
        
        interest2 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[1] + ".png")
        inter_img2 = Label(root, image= interest2, borderwidth=0, highlightthickness=0)
        inter_img2.place(x = 1320, y = 800)
        inter_img2.image = interest2
        
        interest3 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[2] + ".png")
        inter_img3 = Label(root, image= interest3, borderwidth=0, highlightthickness=0)
        inter_img3.place(x = 1119, y = 870) 
        inter_img3.image = interest3
        
        interest4 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[3] + ".png")
        inter_img4 = Label(root, image= interest4, borderwidth=0, highlightthickness=0)
        inter_img4.place(x = 1119, y = 940) 
        inter_img4.image = interest4
        
        interest5 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[4] + ".png")
        inter_img5 = Label(root, image= interest5, borderwidth=0, highlightthickness=0)
        inter_img5.place(x = 1321, y = 870)  
        inter_img5.image = interest5
        
    #----------------------------------------------------------------------------------------------------------------------------
    #display photos  
    j = [0]
    def show_image(i):  
        j[0] = 0 
     
        def resize_img(width, height):
            wid = floor(width/585)
            hei = floor(height/796)
            ration = min(wid, hei)
            return ration
        
        def resize_img2(width, height):
            wid = ceil(585/width)
            hei = ceil(796/height)
            ration = min(wid, hei)
            return ration
        
        imgs = show_photo(i + 1)[0]
        img = Image.open(BytesIO(imgs[j[0]]))
        wi, he = img.size 
        if wi < 585 or he < 796:
            ration = resize_img2(wi, he)
            new_wid = int(wi*ration)
            new_hei = int(he*ration)
        else:
            ration = resize_img(wi, he)
            new_wid = int(wi/ration)
            new_hei = int(he/ration)
        img_resized = img.resize((new_wid, new_hei))
        left = (new_wid - 585)/2
        right = new_wid - (new_wid - 585)/2
        upper = (new_hei - 796)/2
        lower = new_hei - (new_hei - 796)/2
        img_resized = img_resized.crop([left, upper, right, lower])
        
        photo = ImageTk.PhotoImage(img_resized)        
        Photo = Label(root, image= photo, borderwidth=0, highlightthickness=0)
        Photo.place(x = 305, y = 226)
        Photo.image = photo
        
        change = Button(root, image=change_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(change_image, i))
        change.place(x = 900, y = 610)
    
    def change_image(i):    
        j[0] += 1
        if j[0] == 3: j[0] = 0      
                
        def resize_img(width, height):
            wid = floor(width/585)
            hei = floor(height/796)
            ration = min(wid, hei)
            return ration
        
        def resize_img2(width, height):
            wid = ceil(585/width)
            hei = ceil(796/height)
            ration = min(wid, hei)
            return ration
        
        imgs = show_photo(i + 1)[0]
        img = Image.open(BytesIO(imgs[j[0]]))
        wi, he = img.size 
        if wi < 585 or he < 796:
            ration = resize_img2(wi, he)
            new_wid = int(wi*ration)
            new_hei = int(he*ration)
        else:
            ration = resize_img(wi, he)
            new_wid = int(wi/ration)
            new_hei = int(he/ration)
        img_resized = img.resize((new_wid, new_hei))
        left = (new_wid - 585)/2
        right = new_wid - (new_wid - 585)/2
        upper = (new_hei - 796)/2
        lower = new_hei - (new_hei - 796)/2
        img_resized = img_resized.crop([left, upper, right, lower])
        
        photo = ImageTk.PhotoImage(img_resized)        
        Photo = Label(root, image= photo, borderwidth=0, highlightthickness=0)
        Photo.place(x = 305, y = 226)
        Photo.image = photo    
    
    #----------------------------------------------------------------------------------------------------------------------------
    #display button
    exit_button = Button(root, image = exit_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(exit_click, root))
    exit_button.place(x = 5, y = 980)
    
    profile_button = Button(root, image = profile_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(profile_click, root))
    profile_button.place(x = 5, y = 300)
    
    matching_button = Button(root, image = matching_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(matching_click, root))
    matching_button.place(x = 5, y = 500)
    
    chat_button = Button(root, image = chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(chat_click, root))
    chat_button.place(x= 5, y = 700)
        
    match status:
        case "profile":
            profile_button = Button(root, image = profile_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            profile_button.place(x = 5, y = 300)
                        
            display(user_id)
            show_image(user_id)
        case "matching":
            random_id = Randomize(user_id + 1)
            id = [0]
            id[0] = int(random_id.getMultiRandom())
            matching_button = Button(root, image = matching_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            matching_button.place(x = 5, y = 500)
            if id[0] != user_id + 1:
                display(id[0] - 1)
                show_image(id[0] - 1)
                
                refresh_img = PhotoImage(file="GUI/MAIN/match_img/refresh.png")

                
                def like_click():
                    random_id.setLike(id[0])
                    
                    id[0] = int(random_id.getMultiRandom())
                    if id[0] == user_id + 1: profile_click(root)
                    
                    refresh = Label(root, image = refresh_img, borderwidth=0, highlightthickness=0)
                    refresh.place(x = 1095, y = 270)
                    refresh.image = refresh_img
                    
                    display(id[0] - 1)
                    show_image(id[0] - 1)
                    
                def dislike_click():
                    id[0] = int(random_id.getMultiRandom())
                    if id[0] == user_id + 1: profile_click(root)
                    
                    refresh = Label(root, image = refresh_img, borderwidth=0, highlightthickness=0)
                    refresh.place(x = 1095, y = 270)
                    refresh.image = refresh_img
                    
                    display(id[0] - 1)
                    show_image(id[0] - 1)
                
                like = Button(root, image=like_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(like_click))
                like.place(x = 900, y = 450)

                dislike = Button(root, image=dislike_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(dislike_click))
                dislike.place(x = 900, y = 780)
    
    root.mainloop()