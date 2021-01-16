# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 1
# Author: Huynh Hung Thinh (S3750559)
# Created date: 15/08/2020
# Last modified date: 16/08/2020

import turtle
import math
#Menu setup

def menu():
    print('1. Draw UK flag')
    print('2. Draw Australia flag')
    print('3. Exit')
    option = input('Enter an option (1/2/3): ')
    if option == str(1):
        draw_UK_flag(200, 100)
    elif option == str(2):
        draw_AUS_flag(200, 100)
    elif option == str(3):
        print("Program exits. Have a nice day!")
    else:
        print("Invalid option")
        print("*************************")
        menu()

#Turtle setup:

uk_flag = turtle.Turtle()
uk_flag.shape("classic")
uk_flag.speed(20)
aus_flag = turtle.Turtle()
aus_flag.shape("classic")
aus_flag.speed(20)
makeStar = turtle.Turtle()
makeStar.color("#FFFFFF")
makeStar.speed(20)
makeStar.shape("classic")
makeStar.hideturtle()
wn = turtle.Screen()
wn.bgcolor("pink")

#Options setup

def draw_UK_flag(x,y):                   #Draw the UK flag manually by using goto and set coordinates. Begins with inner white lines then inner red lines then outer white lines then outer red lines lastly.
    uk_flag.color("#00247D")
    uk_flag.begin_fill()
    for i in range(2):
        uk_flag.fd(x)
        uk_flag.lt(90)
        uk_flag.fd(y)
        uk_flag.lt(90)
    uk_flag.end_fill()

    uk_flag.penup()
    uk_flag.goto(0,y)
    uk_flag.pendown()
    uk_flag.color("#FFFFFF")
    uk_flag.begin_fill()
    for i in range(2):
        uk_flag.fd(13)
        uk_flag.rt(90 - 63.44)
        uk_flag.fd(209)
        uk_flag.rt(63.44)
        uk_flag.fd(7)
        uk_flag.rt(90)
    uk_flag.end_fill()

    uk_flag.color("#CF142B")
    uk_flag.goto(0,y)
    uk_flag.rt(90-63.44)
    uk_flag.fd((math.sqrt((x*x)+(y*y))))
    uk_flag.penup()
    uk_flag.goto(0,y)
    uk_flag.pendown()
    uk_flag.begin_fill()
    uk_flag.rt(63.44)
    uk_flag.fd(13/3)
    uk_flag.lt(63.44)
    uk_flag.fd(1360/23)
    uk_flag.lt(90-63.44)
    uk_flag.fd(8.1)
    uk_flag.end_fill()

    uk_flag.penup()
    uk_flag.goto(187, 100)
    uk_flag.pendown()
    uk_flag.color("#FFFFFF")
    uk_flag.begin_fill()
    uk_flag.rt(90 + 63.44)
    uk_flag.fd(209)
    uk_flag.lt(63.44)
    uk_flag.fd(7)
    uk_flag.lt(90)
    uk_flag.fd(13)
    uk_flag.lt(90-63.44)
    uk_flag.fd(209)
    uk_flag.lt(63.44)
    uk_flag.fd(7)
    uk_flag.lt(90)
    uk_flag.fd(13)
    uk_flag.end_fill()

    uk_flag.color("#CF142B")
    uk_flag.penup()
    uk_flag.goto(0,0)
    uk_flag.rt(90+63.44)
    uk_flag.pendown()
    uk_flag.fd(math.sqrt((x*x)+(y*y)))
    uk_flag.penup()
    uk_flag.goto(0,0)
    uk_flag.pendown()
    uk_flag.begin_fill()
    uk_flag.rt(90-63.44)
    uk_flag.fd(8.1)
    uk_flag.lt(90-63.44)
    uk_flag.fd(1360/23)
    uk_flag.lt(90+63.44)
    uk_flag.fd(8.1)
    uk_flag.end_fill()

    uk_flag.penup()
    uk_flag.goto(x,y)
    uk_flag.pendown()
    uk_flag.begin_fill()
    uk_flag.fd(8.1)
    uk_flag.lt(90-63.44)
    uk_flag.fd(1360/23)
    uk_flag.lt(90+63.44)
    uk_flag.fd(8.1)
    uk_flag.end_fill()

    uk_flag.penup()
    uk_flag.goto(x,0)
    uk_flag.pendown()
    uk_flag.begin_fill()
    uk_flag.lt(90)
    uk_flag.fd(5)
    uk_flag.lt(63.44)
    uk_flag.fd(1360/23)
    uk_flag.lt(63.44)
    uk_flag.fd(5)
    uk_flag.end_fill()

    uk_flag.penup()
    uk_flag.color("#FFFFFF")
    uk_flag.goto(78,0)
    uk_flag.pendown()
    uk_flag.rt(127)
    uk_flag.begin_fill()
    for i in range(2):
        uk_flag.fd(100)
        uk_flag.rt(90)
        uk_flag.fd(43)
        uk_flag.rt(90)
    uk_flag.end_fill()

    uk_flag.penup()
    uk_flag.goto(0,27)
    uk_flag.pendown()
    uk_flag.begin_fill()
    for i in range(2):
        uk_flag.fd(45)
        uk_flag.rt(90)
        uk_flag.fd(200)
        uk_flag.rt(90)
    uk_flag.end_fill()

    uk_flag.penup()
    uk_flag.goto(90,0)
    uk_flag.pendown()
    uk_flag.color("#CF142B")
    uk_flag.begin_fill()
    for i in range(2):
        uk_flag.fd(100)
        uk_flag.rt(90)
        uk_flag.fd(20)
        uk_flag.rt(90)
    uk_flag.end_fill()

    uk_flag.penup()
    uk_flag.goto(0,40)
    uk_flag.pendown()
    uk_flag.begin_fill()
    for i in range(2):
        uk_flag.fd(20)
        uk_flag.rt(90)
        uk_flag.fd(200)
        uk_flag.rt(90)
    uk_flag.end_fill()

    uk_flag.hideturtle()

def rectangle(x,y): #Draw Aus flag border
    aus_flag.penup()
    aus_flag.goto(0,100)
    aus_flag.pendown()
    aus_flag.color("#00247D")
    aus_flag.begin_fill()
    for i in range(2):
        aus_flag.fd(x)
        aus_flag.rt(90)
        aus_flag.fd(y)
        aus_flag.rt(90)
    aus_flag.end_fill()

def n_pointed_star(size,points): #Draw odd pointed star
    makeStar.begin_fill()
    for i in range(points):
        makeStar.fd(size)
        makeStar.lt(360.0 / points * 3)
    makeStar.end_fill()

def draw_AUS_stars(): #Draw stars on Aus flag
    makeStar.penup()
    makeStar.goto(75,-60)
    makeStar.pendown()
    n_pointed_star(50,7)
    makeStar.penup()
    makeStar.goto(300,-68)
    makeStar.pendown()
    n_pointed_star(34,7)
    makeStar.penup()
    makeStar.goto(230,10)
    makeStar.pendown()
    n_pointed_star(34,7)
    makeStar.penup()
    makeStar.goto(300,65)
    makeStar.pendown()
    n_pointed_star(34,7)
    makeStar.penup()
    makeStar.goto(355,25)
    makeStar.pendown()
    n_pointed_star(34,7)
    makeStar.penup()
    makeStar.goto(335,-10)
    makeStar.pendown()
    n_pointed_star(20,5) #

def draw_AUS_flag(x,y): #Complete Aus flag
    rectangle(2*x,2*y)
    draw_UK_flag(x,y)
    draw_AUS_stars()
    draw_AUS_stars()

menu()

wn.exitonclick()

