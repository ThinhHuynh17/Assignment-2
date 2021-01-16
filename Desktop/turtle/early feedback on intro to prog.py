# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 1
# Author: Huynh Hung Thinh (3750559)
# Created date: 18/07/2020
# Last modified date: 19/07/2020



# Define turtle and window:

import turtle
import math

rua = turtle.Turtle()
rua.shape("classic")
rua.speed(20)

wn = turtle.Screen()
wn.bgcolor("lightpink")

# Algorithm:

for i in range(500):
    for j in ["yellow","red","blue","green"]:
        rua.color(j)
        rua.begin_fill()
        rua.fd(i)
        rua.rt(90)
        rua.fd(i)
        rua.rt(135)
        rua.fd(math.sqrt(2*(i*i)))
        rua.fd(i)
        rua.rt(90)
        rua.fd(i)
        rua.rt(135)
        rua.fd(math.sqrt(2*(i*i)))
        rua.end_fill()


wn.exitonclick()