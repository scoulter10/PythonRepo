import connection
import pymysql.cursors
   
def get_data():
    conn = connection.getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `sleep_table`")
    data = cursor.fetchall()
    
    
    try:

     conn.commit()
     

        

    except:
        print ("error- the database is being rolled back")
        connection.rollback()
        connection.close()

print("data received")
