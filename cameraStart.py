from picamera import PiCamera
from datetime import datetime
import time

x = datetime.now()
filename = "{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}.h264".format(x)
    
def cam_start():
    camera = PiCamera()
    camera.resolution = '720p'

    camera.start_recording(filename)
    print("recording")
    time.sleep(20)
    #this will record 20 second video
    camera.stop_recording()
    camera.close()
    time.sleep(10)


        
        
        

    
