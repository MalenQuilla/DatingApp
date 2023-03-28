from mysql.connector import MySQLConnection, Error
 
def connect():
    """ Connect MySql """
    db_config = {
        'host': 'localhost',
        'database': 'test',
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

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
def insert_image(photo):
    query = "INSERT INTO Photo(image) " \
            "VALUES(%s)"
    args = (convertToBinaryData(photo),)
 
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
        
insert_image('GUI/sign_up_img/basic_information_img/back_ground_basic_information.png')