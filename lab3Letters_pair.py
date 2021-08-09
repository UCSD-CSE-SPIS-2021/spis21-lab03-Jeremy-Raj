# 1. The anonymous turtle is a default turtle that doesn't require a constructor and is useful if you are planning to only use one turtle.
# 2. The "turtle" in the code represents the turtle library that was imported, while Turtle() is a method from that library that creates a new Turtle object, which is called "my_turtle".
# 3. my_turtle.goto(my_turtle.position()[0],-100)

import turtle

def draw_J(the_turtle, size = 1):
    """This method draws the letter J given a turtle object"""

    # Makes the pen size 5 and puts the pen down
    the_turtle.pensize(5)
    the_turtle.pendown()

    # Draws a semicircle
    the_turtle.right(90)
    for i in range(180):
        the_turtle.left(1)
        the_turtle.forward(0.25*size)

    # Draws a straight vertical line
    the_turtle.forward(50*size)
    the_turtle.left(90)

    # Draws the stem of the J
    the_turtle.forward(20*size)
    the_turtle.right(180)
    the_turtle.forward(40*size)

    
draw_J(turtle,10)      # make the new Turtle draw the shape
