import random
import turtle
import math


pen = turtle.Turtle()

def my_goto(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def head():
    a = 1
    pen.seth(90)
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a += 0.5
            pen.rt(3)
            pen.fd(a)
        else:
            a -= 0.5
            pen.rt(3)
            pen.fd(a)

def body():
    my_goto()


if __name__ == '__main__':
    turtle.screensize(800, 600)
    pen.pensize(3)
    pen.speed(3)
    my_goto(-200, 200)
    head()
    # turtle.exitonclick()
    # china()
    # hero()
    # walk()
    # flower()
    turtle.exitonclick()
