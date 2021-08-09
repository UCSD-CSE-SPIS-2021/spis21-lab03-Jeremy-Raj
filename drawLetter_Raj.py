# Raj Sunku
# A program that draws the first letter of my name

import turtle

def draw_Raj(the_turtle):
     
    """"Draws the letter R"""""

    the_turtle.pendown()
    the_turtle.left(90)
    the_turtle.forward(100)
    the_turtle.right(90)
    the_turtle.forward(50)
    the_turtle.right(90)
    the_turtle.forward(50)
    the_turtle.right(90)
    the_turtle.forward(50)
    the_turtle.left(135)
    the_turtle.forward(71)

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.speed(1)
turtle2.speed(1)
turtle1.penup()
turtle1.forward(100)

draw_Raj(turtle1)
draw_Raj(turtle2)