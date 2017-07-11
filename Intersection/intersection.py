#Main idea: Bob should be able to navigate a busy intersection without
#traffic lights

import time
from gopigo import *

DIST_IN_FRONT = 10 #10 cm 

#Wrapper for polling the Ultrasonic sensor
def measure():
    return us_dist(15)

stop()
servo(90) #Look straight ahead

while True:
    dist = measure()
    if(dist < DIST_IN_FRONT):
        stop()
    else:
        fwd()
    time.sleep(.5)#Give some times in between polls
        
    
