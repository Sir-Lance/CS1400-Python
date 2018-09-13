# This is my first graphics program using turtle
# This program illustrates several functions of turtle

# Import turtle module
import turtle
import math

# Define a function that draw an equal-lateral triangles
def drawTriangle(theTurtle,step):
    for i in range(3):
        theTurtle.forward(step)
        theTurtle.left(120)

# Define a function that draw a square
def drawSquare(theTurtle, step):
        for i in range(4):
                theTurtle.fd(step)
                theTurtle.left(90)

# Define a function that draw a full circle
# The current location will be the center of the circle
def drawCircle(theTurtle, radius):
    curPos = theTurtle.position()
    nXcord = curPos[0]
    nYcord = curPos[1] - radius
    theTurtle.penup()
    theTurtle.setpos(nXcord, nYcord)
    theTurtle.pendown()
    theTurtle.circle(radius)

# declare a window
wn = turtle.Screen()
wnTitle = "My Turtle Test"
wn.title(wnTitle)

# Creaet a turtle
myTurtle = turtle.Turtle()

# Set the properties of myTurtle
myTurtle.shape("turtle")
myTurtle.color("green")
myTurtle.pencolor("red")
myTurtle.pensize(5)

# Move the turtle
# Get the move size from the user
move_size = float(input("Please enter the move size:"))

# Draw a triangle
drawTriangle(myTurtle, move_size)

# Move to a new position and draw a new triangle and repeat
myTurtle.penup()
myTurtle.setpos(-move_size,0)
myTurtle.pendown()
drawTriangle(myTurtle, move_size)
myTurtle.penup()
myTurtle.setpos(-move_size/2,move_size*math.sqrt(3)/2)
myTurtle.pendown()
drawTriangle(myTurtle, move_size)

# Change the pen color and draw a square
myTurtle.pencolor("green")
myTurtle.penup()
myTurtle.setpos(-1.5*move_size, -0.5*move_size)
myTurtle.pendown()
drawSquare(myTurtle, 3*move_size)

# Create a second turtle
secondTurtle = turtle.Turtle()
secondTurtle.color("pink")
secondTurtle.pencolor("yellow")
secondTurtle.pensize(5)
drawSquare(secondTurtle,1.5*move_size)

# Move turtle to a new point and draw a circle
secondTurtle.penup()
secondTurtle.setpos(0,-2*move_size)
secondTurtle.pendown()
secondTurtle.dot(0.1*move_size)
drawCircle(secondTurtle, 1.5*move_size)

# Draw Dot
secondTurtle.pencolor('#00ffff')
secondTurtle.dot(0.5*move_size)

wn.exitonclick()
