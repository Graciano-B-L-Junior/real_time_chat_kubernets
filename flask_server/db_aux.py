from mysql.connector import connection
import time

def get_connection() -> connection.MySQLConnection:
    cnx = connection.MySQLConnection(user='root', password='root',
                                 host='mysql_container',
                                 database='speedchatdb')
    return cnx

def close_connection(cnx):
    cnx.close()

def connect_to_mysql(attempts=3, delay=3):
    attempt = 1
    # Implement a reconnection routine
    while attempt < attempts + 1:
        try:
            conn = connection.MySQLConnection(user='root', password='root',
                                 host='mysql_container',
                                 database='speedchatdb')
            print("connection successfully")
            return conn
        except Exception as err:
            print(err)
            print("trying again ...")
            time.sleep(delay ** attempt)
            attempt += 1
    return None