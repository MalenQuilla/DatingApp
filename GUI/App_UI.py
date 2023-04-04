from functools import partial
from tkinter import *
from tkextrafont import Font
import datetime
from io import BytesIO
from math import floor, ceil
from PIL import Image, ImageTk
from database_controller import show_info, show_basics, show_interests, show_photo, show_matched, show_name
from Matching_Controller import Randomize, Match

class User:
    def __init__(self, user_id, status):
        self.__status = status
        self.__user_id = user_id
        self.__root = Tk()
        self.__root.geometry('1920x1080')
        self.__root.resizable(width=False, height=False)
        self.__root.attributes('-fullscreen', True)
        self.__font = Font(file="GUI/MAIN/Be_Vietnam_Pro/BeVietnamPro-ExtraBold.ttf")
        
        self.__img_index = 0
    def return_status(self):
        return self.__status

    def exit_click(self): 
        self.__status = "exit"
        self.__root.destroy()
        
    def matching_click(self):
        self.__status = "matching"
        self.Profile_screen()
        
    def profile_click(self):
        self.__status = "profile"
        self.Profile_screen()
        
    def chat_click(self):
        self.__status = "chat"
        isMatch = Match(self.__user_id)
        isMatch.isMatch()
        self.Chat_Screen()
        
    def Profile_screen(self):
        background = PhotoImage(file="GUI/MAIN/match_img/background.png")

        label_background = Label(self.__root, image = background)
        label_background.place(x = 0, y = 0)
        
        refresh_img = PhotoImage(file="GUI/MAIN/match_img/refresh.png")
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
            refresh = Label(self.__root, image = refresh_img, borderwidth=0, highlightthickness=0)
            refresh.place(x = 1095, y = 270)
            refresh.image = refresh_img
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
            Label(self.__root, textvariable = name, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 19, "bold")).place(x = 1120, y = 365)
            
            age = StringVar()
            age.set(name_data[-1] + ", " + str(age_data))
            Label(self.__root, textvariable = age, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 35, "bold")).place(x = 1117, y = 280)
            
            bio = StringVar()
            bio.set(bio_data)
            Label(self.__root, textvariable=bio, wraplengt = 400, justify= "left", bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 13, "bold")).place(x = 1140, y = 430)
            
            gender = StringVar()
            gender.set(gender_data)
            Label(self.__root, textvariable=gender, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1170, y = 562)
            
            location = StringVar()
            location.set(location_data)
            Label(self.__root, textvariable=location, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1370, y = 615)
            
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
            Label(self.__root, textvariable = height, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1170, y = 615)  
            
            zodiac = StringVar()
            zodiac.set(zodiac_data)
            Label(self.__root, textvariable = zodiac, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1370, y = 742)     
            
            education = StringVar()
            education.set(education_data)
            Label(self.__root, textvariable = education, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1370, y = 562)    
            
            workout = StringVar()
            workout.set(workout_data)
            Label(self.__root, textvariable = workout, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1170, y = 742)     
            
            smoke = StringVar()
            smoke.set(smoke_data)
            Label(self.__root, textvariable = smoke, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1370, y = 679)  
            
            drink = StringVar()
            drink.set(drink_data)
            Label(self.__root, textvariable = drink, bg = "#FFEEF6", fg="#4E4E4E", font=(self.__font, 16, "bold")).place(x = 1170, y = 679)    
                    
            #----------------------------------------------------------------------------------------------------------------------------
            #display interests
            interests = interestss[i]
            
            interest1 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[0] + ".png")
            inter_img1 = Label(self.__root, image= interest1, borderwidth=0, highlightthickness=0)
            inter_img1.place(x = 1120, y = 800)
            inter_img1.image = interest1
            
            interest2 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[1] + ".png")
            inter_img2 = Label(self.__root, image= interest2, borderwidth=0, highlightthickness=0)
            inter_img2.place(x = 1320, y = 800)
            inter_img2.image = interest2
            
            interest3 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[2] + ".png")
            inter_img3 = Label(self.__root, image= interest3, borderwidth=0, highlightthickness=0)
            inter_img3.place(x = 1119, y = 870) 
            inter_img3.image = interest3
            
            interest4 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[3] + ".png")
            inter_img4 = Label(self.__root, image= interest4, borderwidth=0, highlightthickness=0)
            inter_img4.place(x = 1119, y = 940) 
            inter_img4.image = interest4
            
            interest5 = PhotoImage(file="GUI/MAIN/match_img/interest_match_img/All_img/" + interests[4] + ".png")
            inter_img5 = Label(self.__root, image= interest5, borderwidth=0, highlightthickness=0)
            inter_img5.place(x = 1321, y = 870)  
            inter_img5.image = interest5
            
        #----------------------------------------------------------------------------------------------------------------------------
        #display photos  
        def show_image(i):  
            self.__img_index = 0 
        
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
            img = Image.open(BytesIO(imgs[self.__img_index]))
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
            Photo = Label(self.__root, image= photo, borderwidth=0, highlightthickness=0)
            Photo.place(x = 305, y = 226)
            Photo.image = photo
            
            change = Button(self.__root, image=change_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(change_image, i))
            change.place(x = 900, y = 610)
        
        def change_image(i):    
            self.__img_index += 1
            if self.__img_index == 3: self.__img_index = 0      
                    
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
            img = Image.open(BytesIO(imgs[self.__img_index]))
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
            Photo = Label(self.__root, image= photo, borderwidth=0, highlightthickness=0)
            Photo.place(x = 305, y = 226)
            Photo.image = photo    
        
        #----------------------------------------------------------------------------------------------------------------------------
        #display button
        exit_button = Button(self.__root, image = exit_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.exit_click))
        exit_button.place(x = 5, y = 980)
        
        profile_button = Button(self.__root, image = profile_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.profile_click))
        profile_button.place(x = 5, y = 300)
        
        matching_button = Button(self.__root, image = matching_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.matching_click))
        matching_button.place(x = 5, y = 500)
        
        chat_button = Button(self.__root, image = chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.chat_click))
        chat_button.place(x= 5, y = 700)
            
        match self.__status:
            case "profile":
                profile_button = Button(self.__root, image = profile_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                profile_button.place(x = 5, y = 300)
                            
                display(self.__user_id - 1)
                show_image(self.__user_id - 1)
            case "matching":
                random_id = Randomize(self.__user_id)
                id = [0]
                id[0] = int(random_id.getMultiRandom())
                matching_button = Button(self.__root, image = matching_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
                matching_button.place(x = 5, y = 500)
                if id[0] != self.__user_id:
                    display(id[0] - 1)
                    show_image(id[0] - 1)

                    
                    def like_click():
                        random_id.setLike(id[0])
                        
                        id[0] = int(random_id.getMultiRandom())
                        if id[0] == self.__user_id: self.profile_click()
                                               
                        display(id[0] - 1)
                        show_image(id[0] - 1)
                        
                    def dislike_click():
                        id[0] = int(random_id.getMultiRandom())
                        if id[0] == self.__user_id: self.profile_click()
                        
                        display(id[0] - 1)
                        show_image(id[0] - 1)
                    
                    like = Button(self.__root, image=like_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(like_click))
                    like.place(x = 900, y = 450)

                    dislike = Button(self.__root, image=dislike_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(dislike_click))
                    dislike.place(x = 900, y = 780)
        
        self.__root.mainloop()

    def Chat_Screen(self):        
        background = PhotoImage(file="GUI/MAIN/chat_img/chat_background.png")
    
        label_background = Label(self.__root, image = background)
        label_background.place(x = 0, y = 0)
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        # Taskbar no click -- img
        profile_img = PhotoImage(file="GUI/MAIN/chat_img/task_bar_img/taskbar/open_profile_button.png")
        matching_img = PhotoImage(file="GUI/MAIN/chat_img/task_bar_img/taskbar/open_matching_button.png")
        exit_img = PhotoImage(file="GUI/MAIN/chat_img/task_bar_img/taskbar/exit_button.png")
        # Taskbar click -- img
        chat_click_img = PhotoImage(file="GUI/MAIN/chat_img/task_bar_img/taskbar_click/open_chat_button_click.png")

        #--------------------------------------------------------------------------------------------------------------------------------------------------
        #SEND IMAGE -- ICON -- MESSAGE img
        # open_image_img = PhotoImage(file="GUI/MAIN/chat_img/image_icon_send_img/open_image.png")
        # open_icon_img = PhotoImage(file="GUI/MAIN/chat_img/image_icon_send_img/open_icon.png")    
        send_message_img = PhotoImage(file="GUI/MAIN/chat_img/image_icon_send_img/send_message.png")


        #Person who chat with you
        who_chat_img = PhotoImage(file="GUI/MAIN/chat_img/who_chat_img.png")
        face_user_chat_img = PhotoImage(file="GUI/MAIN/chat_img/face_user_chat_img.png")

        #--------------------------------------------------------------------------------------------------------------------------------------------------
        # Taskbar no click ---- BUTTON
        exit_button = Button(self.__root, image = exit_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.exit_click))
        exit_button.place(x = 5, y = 980)
        
        profile_button = Button(self.__root, image = profile_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.profile_click))
        profile_button.place(x = 5, y = 300)
        
        matching_button = Button(self.__root, image = matching_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(self.matching_click))
        matching_button.place(x = 5, y = 500)

        chat_click =  Button(self.__root, image=chat_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        chat_click.place(x = 5, y = 700) 
        #--------------------------------------------------------------------------------------------------------------------------------------------------
        # Face user chat
        face_user_chat = Label(self.__root, image=face_user_chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        face_user_chat.place(x = 640, y = 225)   

        # Person who chat with you 
        
        matched_lists = show_matched(self.__user_id)[0]
        matched_list = matched_lists[0].split(" ")
        name_lists = show_name()
        posy = 300
        for i in matched_list:
            name = name_lists[int(i) - 1][0]   
    
            who_chat = Button(self.__root, font=(self.__font, 19, "bold"), image=who_chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
            who_chat.place(x = 150, y = posy)  
            who_chat.config(text= name, compound= "center", fg="#4E4E4E")
            
            posy += 150
        

        # who_chat_2 = Button(self.__root, image=who_chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        # who_chat_2.place(x = 150, y = 450) 
    

        # who_chat_3 = Button(self.__root, image=who_chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        # who_chat_3.place(x = 150, y = 600)   


        # who_chat_4 = Button(self.__root, image=who_chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        # who_chat_4.place(x = 150, y = 750)    
        
        # OPEN IMAGE -- ICON -- SEND MESSAGE Button
        # open_image= Button(self.__root, image=open_image_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        # open_image.place(x = 1450, y = 930)    

        # open_icon = Button(self.__root, image=open_icon_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)  
        # open_icon.place(x = 1570, y = 930)    

        send_message = Button(self.__root, image=send_message_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
        send_message.place(x = 1680, y = 920)    

        #--------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.__root.mainloop()