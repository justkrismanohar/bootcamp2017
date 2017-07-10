from gopigo import *  # default api from Dexter
import math  # needed for numerical utils
import time # needed for sleep function


SENSOR_PORT = 15  # Assumes standard setup of robot
ROTATION_PER_DEGREE = 360.0 / 34  # Assumes that speed is set to 100
TURNS_PER_CM = 1.1666666
MARCH_DISTANCE = 1.18
SLEEP_TIME = 0.3
PRINT_MESSAGE = False



def measure():
    """
    Uses the ultrasonic sensor to measure the distance to the nearest object in front of the
    GoPiGo robot
    :return: the distance to the nearest object in centimetres
    """
    # grab the signal from the ultrasonic sensor
    distance = us_dist(SENSOR_PORT)
    return distance


def rest_sensor():
    """
    Needed to allow for proper sampling of sensor signal
    :return: None
    """
    time.sleep(SLEEP_TIME)


def activate_wheels(distance, speed=None):
    """
    Computes the number of rotations needed and activates the wheel encoders to suit
    :param distance: the distance in centimetres to traverse
    :param speed: the speed of the robot (optional, default is None to keep current speed)
    :return: None
    """
    # calculate the number of rotations of the wheel required to move that distance
    if speed:
        set_speed(int(speed))
    num_turns = distance / TURNS_PER_CM
    num_turns = math.trunc(num_turns)

    # activate both wheels and indicate the number of revolutions of the wheel
    enc_tgt(1, 1, num_turns)


def go_forward(distance, speed=None):
    """
    Moves the GoPiGo forward a specified number of centimetres
    :param distance: the centimetres to move forward
    :param speed: the speed of the robot (optional, default is None to keep current speed)
    :return: None
    """

    activate_wheels(distance, speed=None)
    if PRINT_MESSAGE:
        print('Moving ', distance, ' cm forward')
    fwd()


def reverse(distance):
    """
    Moves the GoPiGo backward a specified number of centimetres
    :param distance: the centimetres to move forward
    :param speed: the speed of the robot (optional, default is None to keep current speed)
    :return: None
    """
    activate_wheels(distance)
    if PRINT_MESSAGE:
        print('Moving ', distance, ' cm backwards')
    bwd()


def set_rotatation(angle):
    """
    Initializes the robot to turn a specified angle
    :param angle: the angle to rotate in degrees
    :return: the number of rotations to make
    """
    set_speed(100)
    num_rotations = angle / ROTATION_PER_DEGREE
    return num_rotations


def rotate_left(angle):
    """
    Rotates the robot a specified number of degrees to the left
    :param angle: the angle to rotate in degrees
    :return: None
    """
    num_rotations = set_rotatation(angle)
    enc_tgt(1, 0, num_rotations)
    left()



def rotate_right(angle):
    """
    Rotates the robot a specified number of degress to the right
    :param angle: the angle to rotate in degrees
    :return: None
    """
    num_rotations = set_rotatation(angle)
    enc_tgt(0, 1, num_rotations)
    right()


def march_forward(braking_distance, speed=None):
    """
    Makes the robot go forward until it detects an obstacle within a specified distance
    :param braking_distance: the max distance between the robot and possible obstacles
    :param speed: the speed to travel (optional)
    :return: the number of rotations made to encounter the object
    """

    if speed:
        set_speed(int(speed))

    num_rotations = 0
    free_distance = measure()

    while free_distance > braking_distance:
        go_forward(MARCH_DISTANCE, speed)
        num_rotations += 1
        rest_sensor()
        free_distance = measure()

    return num_rotations







