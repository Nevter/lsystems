from functools import partial
from draw_turtle import *
from lsystem_gen import *

## Taken from https://medium.com/@hhtun21/l-systems-draw-your-first-fractals-139ed0bfcac2#:~:text=3.,is%20replaced%20with%20%E2%80%9CAB.%E2%80%9D

## l-system rules
axiom = "F++F++F"

rules = {
    "F" : "F-F++F-F",
}

generations = 4

## l-system interpretation rules
distance = 7
angle = 60

draw_rules = {
    "F" : partial(t_draw, distance),
    "+" : partial(t_turn_left, angle),
    "-" : partial(t_turn_right, angle),
}

## Generate the lsys and draw it
s = generate(axiom, rules, generations)
t_init(pos = (-200,-200), heading = 0)
draw_lsys(s, draw_rules)