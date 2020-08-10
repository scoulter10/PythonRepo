import mysql.connector
from mysql.connector import Error
import connection
import time
from motionThread import motion_start


conn = connection.get_connection()
##setting autocommit to True so the loop iterates through the query
conn.autocommit = True
mycursor = conn.cursor()
query = "SELECT state_value FROM state_table"

##this table uses a boolean value 1 for on and 0 for off
##while true loop runs continuously and checks every 5 seconds for the state

while True:
    mycursor.execute(query)
    myresult = mycursor.fetchone()

##crated a variable for the value of the state returned
    for x in myresult:
        print(x)

##if statement to determine which route to take - whether or not to run the methods   
    if x == 0:
        print("monitor is off")
        
    elif x == 1:
         print("pi is on")
         motion_start()
    else:
        print("error")      

    time.sleep(5)

 




        
                  

        

    

    
        

    
