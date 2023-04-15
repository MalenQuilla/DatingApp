from GUI import *

def main():
    status = "none"
    while status != "login success" and status != "exit":
        start = login.Login()
        start.login_screen()
        user_id = start.get_user_id()
        status = start.get_status()
    if status == "login success":
        user = App_UI.User(user_id, "profile") #set the default page to user profile
        user.Profile_screen()

if __name__ == "__main__":
    main()