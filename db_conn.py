import mysql.connector
from mysql.connector import Error

def create_db_connection(host_name, user_name, user_password, db_name) :
    conn = None
    try :
        conn = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        
    except Error as error :
        print(f"Connection Failed {error}")
    
    return conn