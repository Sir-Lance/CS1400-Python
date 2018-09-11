 #create a screen
#create a turtle
#--algorithm task
#---exit function
#close the screen

#TURTLE

#Turtle has
#--Attributes
#--Functions
import turtle
#start
myCanvas = turtle.Screen()
#background color
myCanvas.bgcolor("black")
#create a TURTLE
myTurtle = turtle.Turtle()
#Properties
myTurtle.shape("turtle")
myTurtle.color("green")
myTurtle.pencolor("red")
myTurtle.pensize(5)
#move the TURTLE
#shape triangle
for i in range(3):
    myTurtle.fd(50)
    myTurtle.left(120)
#myTurtle.fd(50)
#myTurtle.left(120)
#myTurtle.fd(50)
#myTurtle.left(120)
#another shape(square)
myTurtle.pencolor("blue")
for i in [1, 2, 3, 4]:
    myTurtle.fd(50)
    myTurtle.right(90)
#another shape(circle)
myTurtle.circle(30)

#close
myCanvas.exitonclick()
