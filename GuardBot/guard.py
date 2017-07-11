import time
from gopigo import *
from music import *
from espeak import espeak #works only in python 2

RANGE = 10 #The line of sight in cm. Does not "see" beyond this value

#Wrapper for ultrasonic sensor
def measure():
    return us_dist(15)

dist = measure() #Check for intruder 
while dist > RANGE: #Did not "See" an intruder
    print(str(dist))
    dist = measure() #Check for intruder
    time.sleep(0.5) #Avoid spamming the sensor
    
#Borke out of the while loop becasue an intruder was detected
#React in some way
print(str(dist) +" WOOF! WOOF! I AM GONNA CALL THE PO PO!!!")

#Bob issues a warning
espeak.synth("WOOF! WOOF! I AM GONNA CALL THE PO PO!")
#espeak generates some warnings. Think it is some configuration issue
#https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=136974

time.sleep(3)#Allow Bob time to speak
c2 = play("01-super-mario-bros.mp3") #Load music. Save a refernce in variable c2
c2.start() #Play music

time.sleep(20)#Allow music to play for 20 seconds
c2.stop()#Stop music

#Note on simple music API 
#Threads can only be started once so no start/stop, maybe find
#simple audio library with this feature. I think the pygame mixer
#has a puase feature

