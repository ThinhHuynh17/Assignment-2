# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 1
# Author: Huynh Hung Thinh (S3750559)
# Created date: 16/08/2020
# Last modified date: 16/08/2020


import turtle
import math


numbers_input = list(map(float, input("Enter maximum 7 numbers only: ").split()))
list_number = []

#Round numbers from the list
for i in numbers_input:
    i = i.__round__(1)
    list_number.append(i)

list_color = ["red","yellow","blue","green","orange","violet","indigo"]

#Turtle setup
pie = turtle.Turtle()
pie.speed(10)
wn = turtle.Screen()
sum = 0
angles = []

#Sum of numbers in the list
for i in list_number:
    sum = sum + i

#Calculate the angles of each number:
for i in list_number:
    i = (360 * (i * (sum/100))/100)
    angles.append(i)

#Pie chart:
for i in angles:
    if i == angles[0] :
        pie.color("red")
        pie.begin_fill()
        pie.circle(100,i)
        pie.goto(0,100)
        pie.penup()
        pie.end_fill()
        pie.goto(0,0)
        pie.rt(i)
        pie.circle(100,i)
        pie.pendown()
    else:
        new = angles[i] + angles[i-1]       #Make the turtle goes over previous angle and starts it own angle
        pie.color(x)
        pie.begin_fill()
        pie.circle(100,i)
        pie.goto(0,100)
        pie.penup()
        pie.end_fill()
        pie.goto(0,0)
        pie.rt(new)
        pie.circle(100,new)
        pie.pendown()








wn.exitonclick()