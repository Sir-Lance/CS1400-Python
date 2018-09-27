import turtle
window = turtle.Screen()
c1 = turtle.Turtle()
c1.speed(10)
r1 = int(input("R1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))
r2 = int(input("R2: "))
c1.setpos(0, 0)
c1.dot(r1)
c1.setpos(x2, y2 - r2)
c1.dot(r2)
d2 = r1 + r2
if d2 > r1 + r2:
    print("collision")
else:
    print("no collision")
window.exitonclick()
