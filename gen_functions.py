import turtle as t
import random

# Basic generators -other functions use these to do more complex stuff

def gen_colour(palette):  # selects a random colour from a specified palette
    return palette[random.randint(0,4)]

def gen_coord():  # generates a coordinate within the default screen size of (400,300)
    return random.randint(-390,390)

def gen_shape_size():  # sets size of edges for standard shapes
    return random.randint(15,250) 

def gen_iterations(size):  # generates a number of iterations for drawing a shape based on the size of the first one; smaller = higher frequency
    if size >= 400:
        return 0
    elif size >= 350:
        return random.randint(0,1)
    elif size >= 300:
        return random.randint(0,2)
    elif size >= 250:
        return random.randint(1,3)
    elif size >= 200:
        return random.randint(1,4)
    elif size >= 150:
        return random.randint(3,5)
    elif size >= 100:
        return random.randint(4,10)
    elif size >= 80:
        return random.randint(5,13)
    elif size >= 60:
        return random.randint(6,18)
    elif size >= 50:
        return random.randint(7,21)
    elif size >= 40:
        return random.randint(8,25)
    elif size >= 30:
        return random.randint(9,30)
    else:
        return random.randint(10,35)


# Pen reset functions -these reset the location and orientation of the turtle

def relocate_pen(x, y):  # moves pen to specified coordinates without drawing
    t.up()
    t.goto(x,y)

def rand_orient():  # randomly orients the turle to a different orientation than current
    t.left(random.randint(1,359))


# Shape parameter generators -generate the specific parameters for each shape, using the basic generators

def gen_triangle_params(mood_intensity):
    side1 = gen_shape_size()
    if mood_intensity == "low":
        angle = random.randint(68,112)
        side2 = round(((random.randint(100,150) * side1)/100))
        size = (round(side1 + side2)/2)
        return side1, angle, side2, size
    elif mood_intensity == "high":
        angle = random.randint(15,60)
        side2 = round(((random.randint(150,300) * side1)/100))
        size = (round(side1 + side2)/2)
        return side1, angle, side2, size
    else:
        angle = random.randint(45,135)
        side2 = round(((random.randint(100,300) * side1)/100))
        size = (round(side1 + side2)/2)
        return side1, angle, side2, size   

def gen_quad_params(mood_intensity):
    side1 = gen_shape_size()
    if mood_intensity == "low":
        angle1 = random.randint(78,102)
        angle2 = random.randint(78,102)
        side2 = round(((random.randint(100,150) * side1)/100))
        side3 = round(((random.randint(100,150) * side1)/100))
    elif mood_intensity == "high":
        angle1 = random.randint(22,135)
        angle2 = random.randint(22,135)
        side2 = round(((random.randint(150,300) * side1)/100))
        side3 = round(((random.randint(150,300) * side1)/100))
    else:
        angle1 = random.randint(68,112)
        angle2 = random.randint(68,112)
        side2 = round(((random.randint(100,300) * side1)/100))
        side3 = round(((random.randint(100,300) * side1)/100))
    size = (round(side1 + side2 + side3)/3)
    return side1, angle1, side2, angle2, side3, size
