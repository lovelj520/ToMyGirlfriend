# -*- coding: utf-8 -*-
"""
@Time ： 2020/6/19 22:56
@Auth ： feige-xu
@File ：RedLove.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
sizeh = 1.2


def curve():
    for ii in range(200):
        turtle.right(1)
        turtle.forward(1 * sizeh)


turtle.speed(0)
turtle.color("red", "red")
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65 * sizeh)
curve()
turtle.left(120)
curve()
turtle.forward(111.65 * sizeh)
turtle.end_fill()
turtle.hideturtle()
