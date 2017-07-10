import turtle


SPEED = 1
SPEED_INCREMENT = 1

def set_speed(speed):
    """
    Set speed to a specified value
    :param speed: the speed value
    :return: None
    """
    global SPEED
    SPEED = speed


def increase_speed():
    """
    Increases speed
    :return: None
    """
    global SPEED
    SPEED += SPEED_INCREMENT


def decrease_speed():
    """
    Decreases speed
    :return: None
    """
    global speed
    if SPEED - SPEED_INCREMENT > 0:
        SPEED -= SPEED_INCREMENT


def stop_drawing():
    """
    Stop drawing lines in turtle
    :return: None
    """
    turtle.penup()

def start_drawing():
    """
    Start or resume drawing lines in turtle
    :return:
    """
    turtle.pendown()

def forward(distance):
    """
    Moves the cursor forward a specified distance
    :param distance: the distance to traverse
    :return: None
    """
    turtle.forward(distance)


def backward(distance):
    """
    Moves the cursor backwards a specified distance
    :param distance: the distance to traverse
    :return: None
    """
    turtle.backward(distance)

def left_rotate(angle):
    turtle.left(angle)


def right_rotate(angle):
    turtle.right(angle)


