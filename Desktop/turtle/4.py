import turtle

a = turtle.Turtle()
a.speed(9)
a.color("yellow")
wn = turtle.Screen()
wn.bgcolor("red")

a.begin_fill()
for i in range(5):
    a.fd(100)
    a.rt(144)
    a.fd(100)
a.end_fill()

wn.exitonclick()
