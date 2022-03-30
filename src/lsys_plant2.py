from functools import partial
from draw_turtle import *
from lsystem_gen import *

## Taken from https://medium.com/@hhtun21/l-systems-draw-a-stochastic-plant-ii-f322df2ea3c5

## l-system rules
axiom = "YYY"

rules = {
    "X" : "X[-FFF][+FFF]FX",
    "Y" : "YFX[+Y][-Y]"
}

generations = 5

## l-system interpretation rules
distance = 5
angle = 25
stack = ([], [])

draw_rules = {
    "F" : partial(t_draw, distance),
    "-" : partial(t_turn_right, angle), 
    "+" : partial(t_turn_left, angle),
    "[" : partial(t_push, stack),
    "]" : partial(t_pop, stack),
    "X" : partial(t_dot, size = 5, color = "green"),
    "Y" : partial(t_triangle, 4,78,"yellow"),
}

## Generate the lsys and draw it
s = generate(axiom, rules, generations)
t_init(pos = (-100,-300))
draw_lsys(s, draw_rules)