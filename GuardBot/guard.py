from gopigo import *
import time
from music import *
from espeak import espeak #works only in python 2
def measure():
    return us_dist(15)

range = 10 #braks if something moves within 10 cm line of sight
dist = measure()

while dist >range:
    print(str(dist))
    dist = measure()
    time.sleep(0.5)


print(str(dist) +" WOOF! WOOF! I AM GONNA CALL THE PO PO!!!")
espeak.synth("WOOF! WOOF! I AM GONNA CALL THE PO PO!")
#espeak generates some warnings. Think it is some configuration issue
#https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=136974
time.sleep(3)
#c2 = play("C2.wav")
c2 = play("01-super-mario-bros.mp3")
c2.start()
print("RING RING...RING RING")
time.sleep(20)
c2.stop()
#Threads can only be started once so no start/stop, maybe find
#simple audio library with this feature. I think the pygame mixer
#has a puase feature

