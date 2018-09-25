import turtle
import math

window = turtle.Screen()
windowTitle = "Project 2"
window.bgcolor("purple")

window.bgcolor("purple")

cube = turtle.Turtle()
tetra = turtle.Turtle()
octa = turtle.Turtle()
dode = turtle.Turtle()
icos = turtle.Turtle()

def drawSpeed():
    cube.speed(10)
    tetra.speed(10)
    octa.speed(10)
    dode.speed(10)
    icos.speed(10)
drawSpeed()

#Start position X = 0
def drawCube(cube):
    #cube.color("blue", "green")
    #cube.begin_fill()
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
    cube.penup()
    #cube.end_fill()
drawCube(cube)

#Start position X = 100
def drawTetra(tetra):
    #tetra.color("blue", "green")
    #tetra.begin_fill()
    tetra.penup()
    tetra.setpos(100, 0)
    tetra.pendown()
    for i in range(3):
        tetra.fd(100)
        tetra.left(120)

    tetra.setpos(150, 25)
    tetra.setpos(200, 0)
    tetra.setpos(150, 25)
    tetra.setpos(150, 87.66)
    #tetra.end_fill()
drawTetra(tetra)

#Start position X = -100
def drawOcta(octa):
    #octa.color("blue", "green")
    #octa.begin_fill()
    octa.penup()
    octa.setpos(-100, 0)
    octa.pendown()
    for i in range(6):
        octa.fd(50)
        octa.left(60)

    octa.left(30)
    for i in range(3):
        octa.fd(87)
        octa.left(120)
    #octa.end_fill()
drawOcta(octa)

#Start position X = -250
def drawDode(dode):
    #dode.color("blue", "green")
    #dode.begin_fill()
    dode.penup()
    dode.setpos(-250, 0)
    dode.pendown()
    for i in range(5):
        dode.fd(70)
        dode.left(72)
    dode.penup()
    dode.setpos(-233, 25)
    dode.pendown()
    for i in range(5):
        dode.fd(35)
        dode.left(72)
    dode.penup()
    dode.setpos(-250, 0)
    dode.pendown()
    #line to center
    dode.left(55)
    dode.fd(30)
    #follow edge
    dode.left(55)
    dode.fd(35)
    #center to edge
    dode.left(52)
    dode.fd(29)
    #edge to center and follow the center
    dode.back(30)
    dode.right(125)
    dode.fd(37)
    #center to edge
    dode.left(52)
    dode.fd(29)
    dode.back(29)
    dode.right(126)
    dode.fd(36)
    dode.left(55)
    dode.fd(30)
    dode.back(30)
    dode.right(128)
    dode.fd(36)
    dode.left(55)
    dode.fd(30)
    #dode.end_fill()
drawDode(dode)

#Start position X = 250
def drawIcos(icos):

    icos.penup()
    icos.setpos(250, 0)
    icos.pendown()
    for _ in range(6):
        icos.fd(50)
        icos.left(60)
    icos.left(30)
    for _ in range(2):
        #icos.left(30)
        icos.fd(85)
        icos.left(120)
    icos.left(0)
    icos.fd(85)
    icos.left(120)
    icos.fd(42.5)
    icos.left(60)
    icos.fd(42.5)
    for _ in range(2):
        icos.left(120)
        icos.fd(42.5)
    #icos.left(120)
    #icos.fd(42.5)
    icos.setpos(250, 0)
    icos.left(30)
    icos.fd(50)
    icos.left(120)
    icos.fd(25)
    icos.right(30)
    icos.fd(42.5)
    icos.right(30)
    icos.fd(25)
    icos.back(25)
    icos.left(150)
    icos.fd(42.5)
    icos.right(30)
    icos.fd(25)

drawIcos(icos)

window.exitonclick()
