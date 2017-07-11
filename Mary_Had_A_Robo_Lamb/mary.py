from gopigo import *
import time

from __future__ import print_function
from six.moves import input


DISTANCE_TO_STOP = 20

print("Press ENTER to strart")
input()  # accepts keyboard input

# Infinite Loop
# Keep running until we break out of loop
while True:
    dist = us_dist(15)  # get distance from sensor
    print(dist)
    if dist < DISTANCE_TO_STOP:
        print("Stopping")
        stop()
        # Estimate distance travelled
        # If "run out of road" turn around
    else:
        fwd()

    time.sleep(.5)
