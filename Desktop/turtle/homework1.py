import turtle

#create 2 turtles and define windows

rua = turtle.Turtle()
rua.shape("turtle")
rua.speed(5)
rua.color("hotpink")
rua.penup()


pen = turtle.Turtle()
pen.shape("classic")
pen.speed(5)
pen.color("blue")
pen.penup()

wn = turtle.Screen()
wn.bgcolor("lightblue")


#Algorithm

for i in range(12):
    rua.forward(100)
    rua.stamp()
    rua.backward(100)
    rua.right(30)
    pen.forward(80)
    pen.stamp()
    pen.backward(80)
    pen.right(30)



wn.exitonclick()