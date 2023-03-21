import db_conn
import db_execute_query

def markAttendance(ID):
    query_1 = """
    select Name from images where id = %s;
    """
    connection = db_conn.create_db_connection("localhost", "root", "", "person")
    results = db_execute_query.read_query(connection, query_1, ID)

    tuple = results[0]
    name, = tuple

    query_2 = """
    insert into attendence(id, name) values (%s, %s)
    """
    data = (ID, name)

    db_execute_query.execute_query(connection, query_2, data)
