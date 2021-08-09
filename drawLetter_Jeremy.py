# Jeremy Nguyen. drawLetter_Jeremy.py is a program that draws the first letter of my name (J)

import turtle

def draw_J(the_turtle):
    """This method draws the letter J given a turtle object"""

    # Makes the pen size 5 and puts the pen down
    the_turtle.pensize(5)
    the_turtle.pendown()

    # Draws a semicircle
    the_turtle.right(90)
    for i in range(180):
        the_turtle.left(1)
        the_turtle.forward(0.25)

    # Draws a straight vertical line
    the_turtle.forward(50)
    the_turtle.left(90)

    # Draws the stem of the J
    the_turtle.forward(20)
    the_turtle.right(180)
    the_turtle.forward(40)

my_turtle = turtle.Turtle()  # Create a new Turtle object
second_turtle = turtle.Turtle() # Create another Turtle object
second_turtle.penup()
second_turtle.backward(100)

draw_J(my_turtle)      # make the new Turtle draw the shape
draw_J(second_turtle)  # make the second Turtle draw the shape
