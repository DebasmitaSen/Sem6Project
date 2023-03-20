import mysql.connector
import os
from mysql.connector import Error
from mysql.connector import errorcode

try :
    conn = mysql.connector.connect(host = 'localhost',
                                   database = 'person',
                                   user = 'root',
                                   password = '')
    
except mysql.connector.Error as error :
    print(f"Connection Failed {error}")

