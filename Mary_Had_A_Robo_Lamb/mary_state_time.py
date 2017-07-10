#Basic State Machine
#Stops and Cries if can't find Mary (maybe throes a fit?)
#Objective Measure Time

from gopigo import *
import time
from __future__ import print_function

distance_to_stop = 20
time_to_cry = 30 #time in seconds
state = 0 # state = 0 means found Mary, state = 1 means find Mary,
          # state = 3 means to start crying
          
start = time.time() #measured in seconds
end = start
time_diff = end - start
print("Press ENTER to strart")
raw_input()

servo(90)

while True:
    dist = us_dist(15)
    
    if dist < distance_to_stop:
        if state == 1:
            end = time.time() #end of lost state
            time_diff = end - start
            print("Found Mary Stopping in " + str(time_diff) + " seconds")
            stop()
            state = 0 #update state
            
            
    else:
        if state == 0:
            print("Lost Mary Starting")
            fwd()
            state = 1 #update state
            start = time.time() #re-start lost state
            end = start #end >= start
            time_diff = 0 #Reset lost time 

    if state == 1:
        end = time.time()
        time_diff = end - start
        print(str(dist) +" lost time " + str(time_diff))
        if(time_diff > time_to_cry):
            print("Where my Mary!?!?!")
            print("(T_T)")
            stop() #Maybe dance in cirlces or something here
            state = 3
            break;
        
    time.sleep(.5)
