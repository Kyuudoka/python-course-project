import turtle as t
import random
from palette_lists import *
from user_quiz import *
from gen_functions import gen_colour, gen_coord, gen_iterations, relocate_pen, rand_orient, gen_triangle_params, gen_quad_params, gen_spiro_shuffles
from custom_shapes import draw_triangle, draw_quad, spiky_ring, small_ring, spiky_star


# Shape applicator functions -these draw a set number of an identical shape in random orientations and positions on the canvas. Energy and intensity apply here

def apply_triangles(palette, energy):
    for i in range(round(int(energy) * int(complexity) / 3)):  # Energy sets how many times the applicator runs i.e. how many different types of triangle it draws
        side1, angle, side2, size = gen_triangle_params(mood_intensity)
        iterations = gen_iterations(size)
        relocate_pen(gen_coord(), gen_coord())

        for i in range(iterations):  # Iterations is how many times an identical triangle is applied, which is weighted by size
            draw_triangle(gen_colour(palette), gen_colour(palette), side1, angle, side2)
            relocate_pen(gen_coord(), gen_coord())
            rand_orient()

def apply_quads(palette, energy):
    for i in range(round(int(energy) * int(complexity) / 3)):
        side1, angle1, side2, angle2, side3, size = gen_quad_params(mood_intensity)
        iterations = gen_iterations(size)

        for i in range(iterations):
            draw_quad(gen_colour(palette), gen_colour(palette), side1, angle1, side2, angle2, side3)
            relocate_pen(gen_coord(), gen_coord())
            rand_orient()

def apply_spirographs(palette):  # Adds random numbers of spirographs depending on complexity
    if int(complexity) < 5:
        pass
    else:
        shuffle1, shuffle2, shuffle3 = gen_spiro_shuffles(complexity)
        for i in range(shuffle1):
            spiky_ring(gen_colour(palette))
            relocate_pen(gen_coord(), gen_coord())
            rand_orient()
        for i in range(shuffle2):
            small_ring(gen_colour(palette))
            relocate_pen(gen_coord(), gen_coord())
            rand_orient()
        for i in range(shuffle3):
            spiky_star(gen_colour(palette))
            relocate_pen(gen_coord(), gen_coord())
            rand_orient()


# Code which puts everything together

t.speed(400)
if int(complexity) >= 5:
    apply_quads(palette, energy)
    apply_triangles(palette, energy)
    apply_spirographs(palette)
elif int(complexity) >= 3:
    apply_quads(palette, energy)
    apply_triangles(palette, energy)
else:
    apply_triangles(palette, energy)

t.mainloop()  # DO NOT DELETE -keeps output window open until manually closed