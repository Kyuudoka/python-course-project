import turtle as t
import random

# Randomised shapes

def draw_triangle(colour, fillcolour, side1, angle, side2):
    start = t.pos()  # Setup
    t.pencolor(colour)
    t.fillcolor(fillcolour)

    t.down()  # Drawing
    t.begin_fill()
    t.forward(side1)
    t.left(angle)
    t.forward(side2)
    t.goto(start)
    t.end_fill()
    t.up()

def draw_quad(colour, fillcolour, side1, angle1, side2, angle2, side3):
    start = t.pos()  # Setup
    t.pencolor(colour)
    t.fillcolor(fillcolour)
    t.begin_fill()

    t.down()  # Drawing
    t.forward(side1)
    t.left(angle1)
    t.forward(side2)
    t.left(angle2)
    t.forward(side3)
    t.goto(start)
    t.end_fill()

# Classic symmetrical shapes

def draw_pentagon(size, colour, fillcolour):
    pass

def draw_hexagon(size, colour, fillcolour):
    pass

def draw_circle(size, colour, fillcolour):
    pass

# Misc shapes

def draw_star(size, colour, fillcolour):
    pass

def draw_rand_ellipse(size, colour, fillcolour):
    pass

# Spirographs

def spiky_ring(colour):
    start = t.pos()
    t.down()
    t.pencolor(colour)
    for i in range(10):
        t.forward(100)
        t.left(45)
        t.forward(5)
        t.left(45)
        t.forward(5)
        t.left(45)
        t.forward(5)
        t.left(45)
        t.forward(5)
        t.left(45)
        t.forward(100)
        t.left(200)
        t.forward(100)
    t.forward(100)
    t.left(45)
    t.forward(5)
    t.left(45)
    t.forward(5)
    t.left(45)
    t.forward(5)
    t.left(45)
    t.forward(5)
    t.left(45)
    t.forward(100)
    t.left(200)
    t.goto(start) # alternatively change to t.forward(106) to approx close loop

def small_ring(colour):
    t.down()
    t.pencolor(colour)
    for i in range(18):
        t.forward(60)
        t.left(95)
        t.forward(90)
        t.left(105)
        t.forward(25)
        t.left(20)

