from mysql.connector import MySQLConnection, Error
 
def connect():
    """ Kết nối MySQL bằng module MySQLConnection """
    db_config = {
        'host': 'localhost',
        'database': 'Data/Users/DatingAppDatabase',
        'user': 'root',
        'password': ''
    }
 
    # Biến lưu trữ kết nối
    conn = None
 
    try:
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            return conn
 
    except Error as error:
        print(error)
 
    return conn
 
# Test thử
conn = connect()
print(conn)