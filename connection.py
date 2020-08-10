import mysql.connector

def get_connection():
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="scoulter10",
        passwd="2whWwVG104cSygTd",
        database="sleep_log"
    )
    return mydb
    




 


