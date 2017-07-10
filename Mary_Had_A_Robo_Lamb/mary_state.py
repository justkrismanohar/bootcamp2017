#Basic State Machine

from gopigo import *
import time
from __future__ import print_function
from six.moves import input

distance_to_stop = 20
state = 0 # state = 0 means found Mary, state = 1 means find Mary

print("Press ENTER to strart")
input()

while True:
    dist = us_dist(15)
    print dist
    if dist < distance_to_stop:
        if state == 1:
            print("Found Mary Stopping")
            stop()
            state = 0 #update state 
    else:
        if state == 0:
            print("Lost Mary Starting")
            fwd()
            state = 1 #update state

    time.sleep(.5)
