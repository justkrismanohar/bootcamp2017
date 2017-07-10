from gopigo import *
import time

from __future__ import print_function


distance_to_stop = 20
print("Press ENTER to strart")
raw_input()

while True:
    dist = us_dist(15)
    print dist
    if dist < distance_to_stop:
        print("Stopping")
        stop()
    else:
        fwd()

    time.sleep(.5)
