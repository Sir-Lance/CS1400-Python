import turtle
import math

window = turtle.Screen()
windowTitle = "Project 2"

cube = turtle.Turtle()
tetra = turtle.Turtle()

def drawCube(cube):
    for i in range(4):
        cube.fd(50)
        cube.left(90)

    cube.penup()
    cube.setpos(20, 20)
    cube.pendown()

    for i in range(4):
        cube.fd(50)
        cube.left(90)

    cube.penup()
    cube.setpos(0, 50)
    cube.pendown()
    cube.setpos(20, 70)
    cube.penup()
    cube.setpos(50,50)
    cube.pendown()
    cube.setpos(70, 70)
    cube.penup()
    cube.setpos(50, 0)
    cube.pendown()
    cube.setpos(70, 20)
    cube.penup()
    cube.setpos(0, 0)
    cube.pendown()
    cube.setpos(20, 20)
drawCube(cube)

def drawTetra(tetra):

drawTetra(tetra)
window.exitonclick()
