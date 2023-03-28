from Data.user import User
import os

def import2File(thisUser, username):
    path = os.path.realpath('DatingAppProject/Data/Users/' + username)
    try:
        os.mkdir(path)
    except IOError:
        pass
    with open(path + '/Info.txt', "w+") as f1:
        f1.write("\n".join(f"{tup}" for tup in (thisUser.getInfo())))
    with open(path + '/Basics.txt', "w+") as f2:
        f2.write("\n".join(f"{tup}" for tup in (thisUser.getUserBasics())))
    with open(path + '/Interests.txt', "w+") as f3:
        f3.write("\n".join(f"{tup}" for tup in (thisUser.getUserInterests())))
        
     
thisUser = User()
thisUser.setUserInfo("Tung", 19, "Male", "hanoi", "None")
thisUser.setUserBasics("1m82", "None", "None", "None", "None", "None", "None")
thisUser.setUserInterests("None", "None", "None", "None", "None", "None", "None", "None", "None", "None")
import2File(thisUser, "tungdv")

