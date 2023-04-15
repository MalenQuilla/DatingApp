from GUI import *

def main():
    status = "none"
    start = login.Login()
    start.login_screen()
    user_id = start.get_user_id()
    status = start.get_status()
    if status == "done":
        user = App_UI.User(user_id, "profile") 
        user.Profile_screen()

if __name__ == "__main__":
    main()