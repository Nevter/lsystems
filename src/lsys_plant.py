from functools import partial
from draw_turtle import *
from lsystem_gen import *

## Taken from https://en.wikipedia.org/wiki/L-system

## l-system rules
axiom = "X"

rules = {
    "X" : "F+[[X]-X]-F[-FX]+X",
    "F" : "FF"
}

generations = 5

## l-system interpretation rules
distance = 10
angle = 25
stack = ([], [])

draw_rules = {
    "F" : partial(t_draw, distance),
    "-" : partial(t_turn_right, angle), 
    "+" : partial(t_turn_left, angle),
    "[" : partial(t_push, stack),
    "]" : partial(t_pop, stack),
    "X" : none,
    #"X" : partial(t_dot),
}

## Generate the lsys and draw it
s = generate(axiom, rules, generations)
t_init(pos = (-100,-300), heading = 70)
draw_lsys(s, draw_rules)