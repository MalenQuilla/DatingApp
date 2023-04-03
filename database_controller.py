from mysql.connector import MySQLConnection, Error
 
def connect():
    """ Connect MySql """
    db_config = {
        'host': 'localhost',
        'database': 'DatingApp',
        'user': 'root',
        'password': 'pass123'
    }
 
    conn = None
 
    try:
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            return conn
 
    except Error as error:
        print(error)
 
    return conn

#----------------------------------------------------------------------------------------------------

#get data from db

def counts():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT User_id FROM User_account")
        rows = cursor.fetchall()
        
        return(cursor.rowcount)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()

def show_account():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_account")
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_info():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_Information")
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_basics():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_basics")
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_interests():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_interests")
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_seen():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Seen FROM User_match")
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def update_seen(new_seen, user_id):
    query = """ UPDATE User_match
                SET Seen = %s
                WHERE id = %s """
 
    data = (new_seen, user_id)
    try:
        conn = connect()
        
        cursor = conn.cursor()
        cursor.execute(query, data)
        
        conn.commit()
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_liked(i):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Liked FROM User_match WHERE id = %s", (i,))
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def update_liked(new_liked, user_id):
    query = """ UPDATE User_match
                SET Liked = %s
                WHERE id = %s """
 
    data = (new_liked, user_id)
    try:
        conn = connect()
        
        cursor = conn.cursor()
        cursor.execute(query, data)
        
        conn.commit()
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def update_matched(new_matched, user_id):
    query = """ UPDATE User_match
                SET Matched = %s
                WHERE id = %s """
 
    data = (new_matched, user_id)
    try:
        conn = connect()
        
        cursor = conn.cursor()
        cursor.execute(query, data)
        
        conn.commit()
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
#----------------------------------------------------------------------------------------------------
#set data to db

def insert_account(Account_username, Account_password):
    query = "INSERT INTO User_account(Account_username, Account_password) " \
            "VALUES(%s,%s)"
    args = (Account_username, Account_password)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()

def insert_matching(seen):
    query = "INSERT INTO User_match(Seen) " \
            "VALUES(%s)"
    args = (seen,)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()

def insert_info(User_name, User_dob, User_gender, User_location, User_bio):
    query = "INSERT INTO User_information(User_name, User_dob, User_gender, User_location, User_bio) " \
            "VALUES(%s,%s,%s,%s,%s)"
    args = (User_name, User_dob, User_gender, User_location, User_bio)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def insert_baiscs(Basics_height, Basics_weight, Basics_zodiac, Basics_education, Basics_workout, Basics_smoke, Basics_drink):
    query = "INSERT INTO User_basics(Basics_height, Basics_weight, Basics_zodiac, Basics_education, Basics_workout, Basics_smoke, Basics_drink) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s)"
    args = (Basics_height, Basics_weight, Basics_zodiac, Basics_education, Basics_workout, Basics_smoke, Basics_drink)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def insert_interest(in1, in2, in3, in4, in5):
    query = "INSERT INTO User_interests(interest1, interest2, interest3, interest4, interest5) " \
            "VALUES(%s,%s,%s,%s,%s)"
    args = (in1, in2, in3, in4, in5)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def insert_interests_old(Interests_sports, Interests_creativity, Interests_goingout, Interests_stayingin, Interests_film_tv, Interests_reading, Interests_music, Interests_food, Interests_travelling, Interests_pet):
    query = "INSERT INTO User_basics(Interests_sports, Interests_creativity, Interests_goingout, Interests_stayingin, Interests_film_tv, Interests_reading, Interests_music, Interests_food, Interests_travelling, Interests_pet) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    args = (Interests_sports, Interests_creativity, Interests_goingout, Interests_stayingin, Interests_film_tv, Interests_reading, Interests_music, Interests_food, Interests_travelling, Interests_pet)
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
      
        
#insert Image
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
def insert_image(photo1, photo2, photo3):
    query = "INSERT INTO User_photo(image1, image2, image3) " \
            "VALUES(%s, %s, %s)"
    args = (convertToBinaryData(photo1), convertToBinaryData(photo2), convertToBinaryData(photo3))
 
    try:
 
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
  
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_photo(id):
    query = """ SELECT image1, image2, image3 FROM User_photo WHERE id = %s """
    data = (id,)
    
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, data)
        rows = cursor.fetchall()
 
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()