import turtle as t
import random
from palette_lists import *
from user_quiz import *
from gen_functions import gen_colour, gen_coord, gen_iterations, relocate_pen, rand_orient, gen_triangle_params, gen_quad_params
from custom_shapes import draw_triangle, draw_quad
# from turt_drawing_presets.fractals import spiky_ring


# Shape applicator functions -these draw a set number of an identical shape in random orientations and positions on the canvas. Energy and intensity apply here

def apply_triangles(palette, energy):
    for i in range(round(int(energy) * int(complexity) / 2)):  # Energy sets how many times the applicator runs i.e. how many different types of triangle it draws
        side1, angle, side2, size = gen_triangle_params(mood_intensity)
        iterations = gen_iterations(size)
        relocate_pen(gen_coord(), gen_coord())

        for i in range(iterations):  # Iterations is how many times an indentical triangle is applied, which is weighted by size
            draw_triangle(gen_colour(palette), gen_colour(palette), side1, angle, side2)
            relocate_pen(gen_coord(), gen_coord())
            rand_orient()

def apply_quads(palette, energy):
    for i in range(round(int(energy) * int(complexity) / 2)):
        side1, angle1, side2, angle2, side3, size = gen_quad_params(mood_intensity)
        iterations = gen_iterations(size)

        for i in range(iterations):
            draw_quad(gen_colour(palette), gen_colour(palette), side1, angle1, side2, angle2, side3)
            relocate_pen(gen_coord(), gen_coord())
            rand_orient()

def apply_spirographs(palette, energy):
    pass


# Code which puts everything together

t.speed(400)
if int(complexity) >= 5:
    apply_quads(palette, energy)
    apply_triangles(palette, energy)
    apply_spirographs(palette, energy)
elif int(complexity) >= 3:
    apply_quads(palette, energy)
    apply_triangles(palette, energy)
else:
    apply_triangles(palette, energy)


# Test scripts below here



# Test scripts above here


t.mainloop()  # DO NOT DELETE -keeps output window open until manually closed