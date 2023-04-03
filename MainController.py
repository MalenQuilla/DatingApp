from GUI import *
from Matching_Controller import Match

def main():
    login.login_screen()
    user_id = login.get_user_id()
    status = "profile"
    while status != "exit":
        user_profile.Profile_screen(user_id, status)
        status = user_profile.return_status()
        if status == "chat":
            check = Match(user_id)
            check.isMatch()
            chat.Chat_Screen()
            status = chat.return_status()

if __name__ == "__main__":
    main()