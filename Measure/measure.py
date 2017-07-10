from gopigo import *
from math import *
import time

#Returns a reading from the ultrasonic sensor
def measure():
    return us_dist(15)
#Move approximately cm distance
def move(cm):
    num_rev = cm/1.1666666
    num_rev = trunc(num_rev)
    if(num_rev < 0): num_rev = num_rev*-1
    
    print(num_rev)
    enc_tgt(1,1,num_rev)

    if num_rev == 0:
        if cm != 0:
            print(str(cm) + " is too small")
    else :
        if cm < 0 :
            print ("Moving back")
            bwd()
        else:
            print ("Moving forward")
            fwd()

#Measures the number turn (a turn = 1/18 of a revolution) until ultrasonic sensor find something > 35 cm away
def m2():
	count = 0
	set_speed(200)
	dist = measure()
	while(dist <= 35):
		count = count + 1
		#move(1.18)
		move1(1)
		print("count "+ str(count) + " dist "+ str(dist))
		time.sleep(.3)
		dist = measure()
	return count
    
#Moves until it finds a object within 35 cm of the ultra sonic sensor
def m1():
	count = 0
	set_speed(200)
	dist = measure()
	while(dist > 35):
		count = count + 1
		move(1.18)
		print("count "+ str(count) + " dist "+ str(dist))
		time.sleep(.3)
		dist = measure()
	return count
#rotates left by one turn. The number of degrees for a turn varies with speed
def turn1(n):
    set_speed(100)#  with speed 100 , n = 34 is approx 360 degress. Each speed will have a different number to turn 360 degrees
    enc_tgt(1,0,n)
    left_rot()
    
#Turns the wheels n times
def move1(n):
    set_speed(200)
    enc_tgt(1,1,n)
    fwd()

#Measures the side of an object
def seek():
	#servo(180)
	m1()
	time.sleep(.5) #remeber to sleep between opernations, the mechanical components need time to work
	m2()
	time.sleep(1)
	print("Move1 20")
	move1(20)
	time.sleep(1)
	turn1(9)

#A general version of measuring the side of an object.
#Moves m turns and rotates a turns after measuring the side
def seek1(m,a):
	#servo(180)
	m1()
	time.sleep(.5)
	m2()
	time.sleep(1)
	print("Move1 20")
	move1(m)
	time.sleep(1)
	turn1(a)
	
#Measure four sides 
def seek41():
    seek1(25,10)
    time.sleep(1)
    seek1(25,10)
    time.sleep(1)
    seek1(25,10)
    time.sleep(1)
    seek1(25,10)
    time.sleep(1)

