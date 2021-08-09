# Jeremy Nguyen and Raj Sunku
# Irma.py creates a map of Hurricane Irma and traces the route it will take, while also categorizing and coloring its path

import turtle
import csv

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    
    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

        

def irma():
    """Animates the path of hurricane Irma
    """
    # Do not change this line
    # t is the turtle, and you will not need the other variables
    (t, wn, map_bg_img) = irma_setup()

    hurricaneFile = "data/irma.csv"
    # The line below is a little magical. It opens the file,
    # with awareness of any errors that might occur.
    with open(hurricaneFile, 'r') as csvfile:
        # This line gives you an "iterator" you can use to get each line
        # in the file.
        pointreader = csv.reader(csvfile)

        # You'll need to add some code here, before the loop
        # One thing you'll need to figure out how to do is to
        # skip the first line of the file (which is the header).
        # You might use a boolean variable, or you can
        # look into Python's built-in next function
        #(https://docs.python.org/3/library/functions.html#next)
        # pointreader is an iterator

        t.pencolor("white")
        t.penup()
        t.speed(1)
        firstInstance = True

        for row in pointreader:
            # row is a list representing each line in the csv file
            # Each comma separated element is in its own index position
            # This code just prints out the date and time elements of each
            # row in the file.
            # Make sure you understand what is happening here.
            # Then, you'll need to change this code
            print("Date:", row[0], "Time:", row[1])

            # ensures the first row of labels is ignored
            if(not firstInstance):
                print(row)

                # converts the meaningful data into floats
                longitude = float(row[2])
                latitude = float(row[3])
                windSpeed = float(row[4])
                category = categorizer(windSpeed, t)

                # draws the path the hurricane takes 
                t.goto(latitude, longitude)
                t.write(str(category))
                t.pendown()

            firstInstance = False
    # Hack to make sure a reference to the background image stays around
    # Do not remove or change this line
    return map_bg_img


# Feel free to add "helper" functions here

def categorizer(windSpeed, t):
    """This method returns the category based on the wind speed and changes the state of the turtle based on the category"""

    if windSpeed < 74:
        t.pensize(1)
        t.pencolor("white")
        return 0
    elif windSpeed < 96:
        t.pensize(4)
        t.pencolor("blue")
        return 1
    elif windSpeed < 111:
        t.pensize(6)
        t.pencolor("green")
        return 2
    elif windSpeed < 130:
        t.pensize(8)
        t.pencolor("yellow")
        return 3
    elif windSpeed < 157:
        t.pensize(10)
        t.pencolor("orange")
        return 4
    else:
        t.pensize(12)
        t.pencolor("red")
        return 5

if __name__ == "__main__":
    bg=irma()
