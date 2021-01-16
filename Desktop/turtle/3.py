import turtle


meo = turtle.Turtle()
gau = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("lightblue")



for i in range(3):
    meo.forward(100)
    meo.left(120)
    meo.forward(100)


for i in range(4):
    gau.fd(100)
    gau.lt(90)
    gau.fd(100)

for i in range (6):
    c.fd(100)
    c.lt(180-((6-2)*180)/6)
    c.fd(100)

for i in range(8):
    d.fd(100)
    d.lt(180-(((8-2)*180)/8))
    d.fd(100)

def draw_polygons(turtle,distance,angle,sides):
    sides = int(input("Polygon sides: "))
    for i in range(sides):
        turtle.forward(distance)
        angle = 180-(((sides-2)*180)/sides)
        turtle.forward(distance)

draw_polygons()






wn.exitonclick()

