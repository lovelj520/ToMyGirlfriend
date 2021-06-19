# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/19 23:40
@Auth ： feige-xu
@File ：fingerHeart.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

import turtle



turtle.speed(1)

turtle.Turtle().screen.delay(0)



def go_to(x, y):

    turtle.up()

    turtle.goto(x, y)

    turtle.down()



def ring(a, b, c, d):

    for i in range(a):

        turtle.forward(b)

        if d == 'right':

            turtle.right(c)

        else:

            turtle.left(c)



def heart(x, y, size):

    go_to(x, y)

    turtle.left(150)

    turtle.begin_fill()

    turtle.forward(51 * size)

    ring(150, size, 0.3, 'right')

    ring(210, size, 0.786, 'right')

    turtle.left(120)

    ring(210, size, 0.786, 'right')

    ring(150, size, 0.3, 'right')

    turtle.forward(51 * size)

    turtle.end_fill()



# 头部

turtle.color('black')

go_to(-228, 72)

turtle.pensize(3)

turtle.left(150)

ring(350, 1, 0.8, 'right')



# 手臂

turtle.left(150)

turtle.forward(70)

turtle.left(90)

turtle.forward(10)

ring(200, 0.1, 0.9, 'right')

turtle.forward(10)

turtle.left(90)

turtle.forward(20)

ring(200, 0.1, 0.9, 'right')

turtle.forward(10)

turtle.left(90)

ring(200, 0.2, 0.9, 'right')

turtle.left(100)

turtle.left

turtle.forward(80)



# 身体

go_to(-228, 72)

turtle.left(40)

turtle.forward(40)

ring(120, 0.2, 0.9, 'left')



go_to(-219, 52)

turtle.right(95)

turtle.forward(80)

turtle.right(85)

ring(205, 0.1, 0.9, 'left')

turtle.forward(40)

turtle.left(90)

turtle.forward(10)

ring(200, 0.1, 0.9, 'right')

turtle.forward(10)

turtle.left(90)

turtle.forward(40)

ring(205, 0.1, 0.9, 'left')

turtle.right(92)

turtle.forward(90)



# 左眼

go_to(-217, 155)

turtle.fillcolor('black')

turtle.begin_fill()

turtle.circle(5)

turtle.end_fill()



# 右眼

go_to(-169, 158)

turtle.fillcolor('black')

turtle.begin_fill()

turtle.circle(5)

turtle.end_fill()



# 微笑

go_to(-210, 132)

turtle.right(180)

ring(200, 0.2, 0.9, 'left')



# 腮红

turtle.color('#ffa0a0')

turtle.pensize(5)

turtle.left(170)



go_to(-235, 135)

turtle.forward(11)

go_to(-225, 135)

turtle.forward(11)

go_to(-155, 140)

turtle.forward(11)

go_to(-165, 140)

turtle.forward(11)



# 比心

turtle.setheading(0)

heart(-35, 135, 0.10)

turtle.setheading(0)

heart(5, 150, 0.13)

turtle.setheading(0)

heart(52, 165, 0.15)



# 写字

go_to(-39, 69)

turtle.write("520", align="left", font=("黑体", 30, "normal"))

