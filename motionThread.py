import picam3
from picam3 import motion
from cameraStart import cam_start
from sqlInsert import insert_time
import time
from sendEmail import send_mail
from stream import StreamingServer
from stream import StreamingOutput


def motion_start():
    motionState = False
    #we are not detecting motion presently

    try:
        print("turning on device - you have 10 seconds")
        time.sleep(10)
        print("ready to detect motion!")

        while True:
            motionState = picam3.motion()
            #motion() is the method i created in the picam3 file
            print (motionState)
      
            if motionState==True:
                insert_time()
                send_mail()
                ##cam_start()
                StreamingServer.start_stream()
                print("video streamed!")
                time.sleep(10)

    except KeyboardInterrupt:
        print ("quit")
           # MotionSensor.close()


