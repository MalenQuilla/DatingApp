from GUI import *

def main():
    login.login_screen()
    user_id = login.get_user_id()
    status = "profile"
    while status != "exit":
        user_profile.Profile_screen(user_id - 1, status)
        status = user_profile.return_status()
        if status == "chat":
            chat.Chat_Screen()
            status = chat.return_status()
main()