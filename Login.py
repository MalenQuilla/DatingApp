import mysql.connector
from mysql.connector import MySQLConnection, Error
def connect():
    #""" Kết nối MySQL bằng module MySQLConnection """
    db_config = {
        'host': 'localhost',
        'database': 'Data/Users/DatingAppDatabase',
        'user': 'root',
        'password': 'Anhtung777'
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
def show_accounts():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_account")
 
        rows = cursor.fetchall()
 
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
        # Đóng kết nối
        cursor.close()
        conn.close()

show_accounts()