import db_conn
import db_execute_query
import db_data_unpack
import datetime

def total_attendence(ID, connection, name) :
    query_1 = """
    select total_att from total_attendence where id = %s
    """
    total_att = db_execute_query.read_query(connection, query_1, ID)

    if not total_att :
        query_2 = """
        insert into total_attendence(id, name, total_att) values (%s, %s, 1)
        """
        data = (ID, name)

        db_execute_query.execute_query(connection, query_2, data)
        return
    
    query_3 = """
    update total_attendence set total_att = total_att + 1 where id = %s
    """

    db_execute_query.execute_query_(connection, query_3, ID)


def enter_attendence(ID, connection) :
    query_1 = """
    select Name from student_info where id = %s;
    """
        
    results = db_execute_query.read_query(connection, query_1, ID)

    # Fetching Name from database...
    name = db_data_unpack.unpack(results)

    query_2 = """
    insert into attendence(id, name, login_info) values (%s, %s, %s)
    """
    time = datetime.datetime.now()
    data = (ID, name, time)

    db_execute_query.execute_query(connection, query_2, data)
    total_attendence(ID, connection, name)
    connection.close()

def markAttendance(ID) :

    system_time_stamp = datetime.datetime.now()
    connection = db_conn.create_db_connection("localhost", "root", "", "students_details")

    query_1 = """
    select login_info from attendence where id = %s order by login_info desc limit 1
    """

    time_stamp = db_execute_query.read_query(connection, query_1, ID)

    if not time_stamp :
        enter_attendence(ID, connection)
        return
    
    time_stamp = db_data_unpack.unpack(time_stamp)

    time_diff = system_time_stamp - time_stamp
    time_diff = time_diff.total_seconds() / 60 ** 2

    if time_diff > 1 :
        enter_attendence(ID, connection)