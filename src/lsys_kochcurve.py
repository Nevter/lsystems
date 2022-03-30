from functools import partial
from draw_turtle import *
from lsystem_gen import *

## Taken from https://en.wikipedia.org/wiki/L-system

## l-system rules
axiom = "F"

rules = {
    "F" : "F+F-F-F+F",
}

generations = 5

## l-system interpretation rules
distance = 5
angle = 90

draw_rules = {
    "F" : partial(t_draw, distance),
    "+" : partial(t_turn_left, angle),
    "-" : partial(t_turn_right, angle),
}

## Generate the lsys and draw it
s = generate(axiom, rules, generations)
t_init(pos = (-200,-200), heading = 0)
draw_lsys(s, draw_rules)