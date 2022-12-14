import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import turtle              # imports turtle
# angle = 90

# turtle = turtle.Turtle()      #creates an instance of turtle called turtle
# turtle.fd()                   # turtle will move forwards
# turtle.bk()                   # turtle will move backwards
# turtle.lt(angle)              # turns left default 90
# turtle.rt(angle)              # turns right default 90
# turtle.pu()                   # turtle up
# turtle.pd()                   # turtle down
# turtle.setheading(angle)     # sets the direction (180 is left)

def draw_triangle(length):
    turtle.setheading(180)      # set the direction of the turtle to left
    for i in range(3):       # draw 3 sides
        turtle.rt(120)          # rotate the turtle 120 degrees clockwise
        # turtle.write(i)
        turtle.fd(length)       # draw side
                             # turtle will end facing left (180)


def sierpinski_order_n_recursive(n , length):
    # turtle.write("hello")
    if n == 1:
        draw_triangle(length)
    elif n == 2:
        draw_triangle(length)
        turtle.rt(120)
        turtle.fd(length * 2 ** (n - 1))
        draw_triangle(length)
        turtle.lt(180)
        turtle.fd(length * 2 ** (n - 2))
        turtle.lt(180)
        
        turtle.lt(120)
        turtle.fd(length * 2 ** (n - 1))
        
        turtle.rt(120)
        turtle.fd(length * 2 ** (n - 2))


        draw_triangle(length)
        turtle.fd(length * 2 ** (n - 1))


    else:
        sierpinski_order_n_recursive(n - 1, length)
        
        turtle.rt(120)
        turtle.fd(length * 2 ** (n - 1))
        
        sierpinski_order_n_recursive(n -1, length)

        turtle.rt(120)
        turtle.write("1")
        turtle.fd(length * 2 ** (n-2))
        turtle.fd(length * 2 ** (n-3))
        turtle.write("2")
        turtle.rt(120)
        turtle.fd(length * 2 ** (n-1))
        turtle.fd(length * 2 ** (n-2))
        turtle.fd(length * 2 ** (n-3))
        
        # turtle.fd(length * 2 ** (n-2))
        # turtle.write("3")
        # turtle.fd(length * 2 ** (n-2))
        # turtle.write("4")
        # turtle.fd(length * 2 ** (n-2))
        # turtle.write("5")
        turtle.rt(120)
        turtle.fd(length * 2 ** (n-2))
        turtle.fd(length * 2 ** (n-3))
        turtle.write("6")
        

        # turtle.lt(180)
        # turtle.fd(length * 2 ** (n-2))
        # turtle.rt(60)
        # turtle.fd(length * 2 ** (n-1))
        # turtle.rt(120)
        # turtle.fd(length * 2 ** (n-2))


        # turtle.lt(120)
        # turtle.fd(length * 2 ** (n - 1))
        # turtle.rt()
        # turtle.fd(length * 2 ** (n - 1))
        sierpinski_order_n_recursive(n - 1, length)
        turtle.fd(length * 2 ** (n - 1))
        # turtle.write("hi1")
        # turtle.fd(length * 2 ** (n - 2))
        # turtle.write("xx2")
        # turtle.lt(180)
        # turtle.fd(length * 2 ** (n-2))
        # turtle.rt(60)
        # turtle.fd(length * 2 ** (n-1))
        # turtle.rt(120)
        # turtle.fd(length * 2 ** (n-2))

# sierpinski_order_n_recursive(6, 10)
# turtle.setposition(0, 150)
def screen():
    turt = turtle.Turtle()
    turt.color('blue')
    turt.fillcolor('cyan')
    turt.begin_fill()
    turt.penup()
    turt.goto(-250, -50)
    turt.pendown()
    turt.write('For the given n, can you imagine how the Hanoi Graph looks like?\nEnter n value in terminal and you will see if you get it right! :D', font=("Verdana",
                                    15, "normal"))
    turt.end_fill()
    

# turtle.setposition(10, 10)

# screen()


# turtle.write("For the given n, can you imagine how the Hanoi Graph looks like? Enter n value in terminal and you will see if you get it right! :D", font=("Verdana",
#                                     15, "normal"), align='left')

k = int(input("Please give a number n: "))
# 

turtle.speed(100)               # sets the draw speed, (1???10)
# turtle.write("hello")
# turtle.goto(-20*k, 0)
# turtle.write("xx")
sierpinski_order_n_recursive(k, int(1/k * 60))


# turtle.bye()
# turtle.bye()
turtle.exitonclick()
# turtle.done()