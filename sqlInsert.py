import mysql.connector
import connection
from mysql.connector import Error

conn = connection.get_connection()
mycursor = conn.cursor()

def insert_time():

    query = "INSERT INTO sleep_table(Id, date_time, pi_id) VALUES ('', now(), '1')"

    try:
        mycursor.execute(query)
        conn.commit()
        print (mycursor.rowcount, "record inserted")

    except:
        print("error- database is being rolled back")
        conn.rollback()
        conn.close()
    
        
    


