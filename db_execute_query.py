from mysql.connector import Error

def execute_query(conn, query, val) :
    cursor = conn.cursor()
    try :
        cursor.execute(query, val)
        conn.commit()
    except Error as error :
        print(f"Failed to commit query {error}")

def read_query(conn, query, val) :
    cursor = conn.cursor()
    result = None
    try:
        cursor.execute(query, (val,))
        result = cursor.fetchall()
        return result
    except Error as error:
        print(f"Error : '{error}'")