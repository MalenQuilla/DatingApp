import tkinter as tk
from functools import partial
from tkinter import *



def Chat_Screen():
    root = tk.Tk()
    root.title("Basics Information")

    root.geometry('1920x1080')
    root.resizable(width=False, height=False)
    background = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/chat_background.png")
 


    label_background = tk.Label(root, image = background)
    label_background.pack()
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Taskbar no click -- img
    profile_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/task_bar_img/taskbar/open_profile_button.png")
    matching_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/task_bar_img/taskbar/open_matching_button.png")
    chat_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/task_bar_img/taskbar/open_chat_button.png")
    exit_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/task_bar_img/taskbar/exit_button.png")
    # Taskbar click -- img
    profile_click_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/task_bar_img/taskbar_click/open_profile_button_click.png")
    matching_click_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/task_bar_img/taskbar_click/open_match_button_click.png")
    chat_click_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/task_bar_img/taskbar_click/open_chat_button_click.png")

    #--------------------------------------------------------------------------------------------------------------------------------------------------
    #SEND IMAGE -- ICON -- MESSAGE img
    open_image_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/image_icon_send_img/open_image.png")
    open_icon_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/image_icon_send_img/open_icon.png")    
    send_message_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/image_icon_send_img/send_message.png")


    #Person who chat with you
    who_chat_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/who_chat_img.png")
    face_user_chat_img = tk.PhotoImage(file="DatingAppProject/GUI/MAIN/chat_img/face_user_chat_img.png")

    #--------------------------------------------------------------------------------------------------------------------------------------------------
    # Taskbar no click ---- BUTTON
    profile = tk.Button(label_background, image=profile_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    profile.place(x = 7, y = 300)  

    matching =  tk.Button(label_background, image=matching_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    matching.place(x = 4, y = 500)  

    chat =  tk.Button(label_background, image=chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    chat.place(x = 6, y = 700) 

    exit = tk.Button(label_background, image=exit_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    exit.place(x = 5, y = 950) 


    # Taskbar click ---- BUTTON
    profile_click =  tk.Button(label_background, image=profile_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    profile_click.place(x = 7, y = 300)    

    matching_click =  tk.Button(label_background, image=matching_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    matching_click.place(x = 4, y = 500)

    chat_click =  tk.Button(label_background, image=chat_click_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    chat_click.place(x = 6, y = 700) 
    #--------------------------------------------------------------------------------------------------------------------------------------------------
    # Face user chat
    face_user_chat = tk.Label(label_background, image=face_user_chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    face_user_chat.place(x = 640, y = 225)   

    # Person who chat with you 
    
    who_chat_1 = tk.Button(label_background, image=who_chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    who_chat_1.place(x = 150, y = 300)    


    who_chat_2 = tk.Button(label_background, image=who_chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    who_chat_2.place(x = 150, y = 450) 
   

    who_chat_3 = tk.Button(label_background, image=who_chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    who_chat_3.place(x = 150, y = 600)   


    who_chat_4 = tk.Button(label_background, image=who_chat_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    who_chat_4.place(x = 150, y = 750)    
    
    # OPEN IMAGE -- ICON -- SEND MESSAGE Button
    open_image= tk.Button(label_background, image=open_image_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    open_image.place(x = 1450, y = 930)    

    open_icon = tk.Button(label_background, image=open_icon_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)  
    open_icon.place(x = 1570, y = 930)    

    send_message = tk.Button(label_background, image=send_message_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0)
    send_message.place(x = 1680, y = 920)    


    #--------------------------------------------------------------------------------------------------------------------------------------------------
    
    root.mainloop()
if __name__ == "__main__":
    Chat_Screen()