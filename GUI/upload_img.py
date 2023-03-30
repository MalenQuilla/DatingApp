import tkinter as tk
from functools import partial
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from math import floor
from database_controller import insert_image
from GUI import letter_thanks

def con_click(images, root):
    insert_image(images[0], images[1], images[2])
    print('set up images success')
    root.destroy()
    letter_thanks.Letter_Thanks_Screen()
    

def Upload_Screen():
    root = tk.Tk()
    root.title("Profile Information")
    root.geometry('1440x900')
    root.resizable(width=False, height=False)



    background_img = tk.PhotoImage(file="GUI/upload_img/background_upload_img.png")
    continue_img = tk.PhotoImage(file="GUI/upload_img/continue_img.png")
    upload_img = tk.PhotoImage(file="GUI/upload_img/upload_click_img.png")

    label_background = tk.Label(root, image=background_img)
    label_background.pack()
    
    images = ["None", "None", "None"]
    
    def resize_img1(width, height):
        wid = floor(width/335)
        hei = floor(height/435)
        ration = min(wid, hei)
        return ration
    
    def resize_img2_3(width, height):
        wid = floor(width/230)
        hei = floor(height/200)
        ration = min(wid, hei)
        return ration
        
    def upload_file():
        global img
        #f_types = [('JPG Files', '*.jpg'), ('JPEG Files', '*.jpeg'), ('PNG Files', '*.png')]
        f_types = [('Image', '*.jpg *.jpeg *.png')]
        filename = filedialog.askopenfilename(multiple = False, filetypes = f_types)
        
        if images[0] == "None":
            images[0] = filename
            img = Image.open(filename)
            width, height = img.size  
            ration = resize_img1(width, height)
            new_wid = int(width/ration)
            new_hei = int(height/ration)
            img_resized = img.resize((new_wid, new_hei))
            left = (new_wid - 335)/2
            right = new_wid - (new_wid - 335)/2
            upper = (new_hei - 435)/2
            lower = new_hei - (new_hei - 435)/2
            img_resized = img_resized.crop([left, upper, right, lower])
            img_resized = ImageTk.PhotoImage(img_resized)
        
            def remove_img1():
                display_img1.destroy()
                images[0] = "None"
        
            display_img1 = Button(root, image = img_resized, borderwidth=0, highlightthickness=0, command= partial(remove_img1))
            display_img1.place(x = 682, y = 316)
            display_img1.image = img_resized
        elif images[1] == "None":
            images[1] = filename
            img = Image.open(filename)
            width, height = img.size  
            ration = resize_img2_3(width, height)
            new_wid = int(width/ration)
            new_hei = int(height/ration)
            img_resized = img.resize((new_wid, new_hei))
            left = (new_wid - 230)/2
            right = new_wid - (new_wid - 230)/2
            upper = (new_hei - 200)/2
            lower = new_hei - (new_hei - 200)/2
            img_resized = img_resized.crop([left, upper, right, lower])
            img_resized = ImageTk.PhotoImage(img_resized)
        
            def remove_img2():
                display_img2.destroy()
                images[1] = "None"
        
            display_img2 = Button(root, image = img_resized, borderwidth=0, highlightthickness=0, command= partial(remove_img2))
            display_img2.place(x = 1060, y = 316)
            display_img2.image = img_resized
        elif images[2] == "None":
            images[2] = filename
            img = Image.open(filename)
            width, height = img.size  
            ration = resize_img2_3(width, height)
            new_wid = int(width/ration)
            new_hei = int(height/ration)
            img_resized = img.resize((new_wid, new_hei))
            left = (new_wid - 230)/2
            right = new_wid - (new_wid - 230)/2
            upper = (new_hei - 200)/2
            lower = new_hei - (new_hei - 200)/2
            img_resized = img_resized.crop([left, upper, right, lower])
            img_resized = ImageTk.PhotoImage(img_resized)
        
            def remove_img3():
                display_image3.destroy()
                images[2] = "None"
        
            display_image3 = Button(root, image = img_resized, borderwidth=0, highlightthickness=0, command= partial(remove_img3))
            display_image3.place(x = 1060, y = 550)
            display_image3.image = img_resized
    
    upload_button= tk.Button(root, image= upload_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= lambda: upload_file())
    upload_button.place(x = 137, y = 370)


    continue_button = tk.Button(root, image= continue_img, bg="#FFFFFF", borderwidth=0, highlightthickness=0, command= partial(con_click, images, root))
    continue_button.place(x = 1170, y = 800)

    root.mainloop()