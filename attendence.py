import db_conn
import db_execute_query
import db_data_unpack
import datetime

def enter_attendence(ID, connection) :
    query_1 = """
    select Name from images where id = %s;
    """
        
    results = db_execute_query.read_query(connection, query_1, ID)

    # Fetching Name from database...
    name = db_data_unpack.unpack(results)

    query_2 = """
    insert into attendence(id, name) values (%s, %s)
    """
    data = (ID, name)

    db_execute_query.execute_query(connection, query_2, data)
    connection.close()

def markAttendance(ID) :

    system_time_stamp = datetime.datetime.now()
    connection = db_conn.create_db_connection("localhost", "root", "", "person")

    query_1 = """
    select login_info from attendence where id = %s order by login_info desc limit 1
    """

    time_stamp = db_execute_query.read_query(connection, query_1, ID)

    if not time_stamp :
        enter_attendence(ID, connection)
        exit()
    
    time_stamp = db_data_unpack.unpack(time_stamp)

    time_diff = system_time_stamp - time_stamp
    time_diff = time_diff.total_seconds() / 60 ** 2

    if time_diff > 1 :
        enter_attendence(ID, connection)