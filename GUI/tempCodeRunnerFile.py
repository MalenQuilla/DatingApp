def Submit_Button_Continue():
    # Lưu giá trị của user_name_sign_up và password_sign_up vào các biến tạm
    username = user_name_sign_up.get()
    password = password_sign_up.get()
    confirm_password = confirm_password_sign_up.get()

    # Kiểm tra nếu tên đăng nhập không hợp lệ hoặc mật khẩu không khớp
    if not Notification_Special_Character(username):
        Incorrect_Notification()

    elif not Notification_not_Match_Password(username):
        Notification_not_Match_Password()
        
    else:
        Continue()

def Continue():
    continue_button = tk.Button(label_background, image=continue_img, command=Submit_Button_Continue)
    continue_button.config(bg ="#FFFFFF")
    continue_button.place(x=375, y=415)
    continue_button.configure(borderwidth=0, highlightthickness=0)

    # Gắn sự kiện FocusIn vào nút "Continue"
    continue_button.bind("<FocusIn>", lambda event: Submit_Button_Continue())