from functools import partial
from draw_turtle import *
from lsystem_gen import *

## Taken from https://en.wikipedia.org/wiki/L-system

## l-system rules
axiom = "0"

rules = {
    "1" : "11",
    "0" : "1[0]0"
}

generations = 6

## l-system interpretation rules
distance = 10 
angle = 45
stack = ([], [])

draw_rules = {
    "0" : partial(t_draw_and_dot, distance),
    "1" : partial(t_draw, distance),
    "[" : partial(t_push_then_turn_left, stack, angle),
    "]" : partial(t_pop_then_turn_right, stack, angle),
}

## Generate the lsys and draw it
s = generate(axiom, rules, generations)
t_init()
draw_lsys(s, draw_rules)