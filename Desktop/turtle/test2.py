import turtle

r = 150
angle1 = 70
angle2 = 40


# Initializing the turtle
wn = turtle.Screen()
wn.setup(500, 500)
wn.delay(25)
t = turtle.Turtle()


t1 = turtle.Turtle()


t1.color("red")
t1.fillcolor("red")
t1.begin_fill()
t1.circle(r, angle1)
t1.goto(0, r)
t1.penup()
t1.end_fill()
t1.penup()
t1.goto(0,0)
t1.right(angle1)
t1.circle(r, angle1)
t1.pendown()


t1.fillcolor("blue")
t1.begin_fill()
t1.circle(r, angle2)
t1.goto(0, r)
t1.penup()
t1.end_fill()
t1.penup()
t1.goto(0,0)
t1.right(angle1 + angle2)
t1.circle(r, angle1 + angle2)
t1.pendown()


wn.exitonclick()