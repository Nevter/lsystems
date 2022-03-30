from functools import partial
from draw_turtle import *
from lsystem_gen import *

## Taken from https://en.wikipedia.org/wiki/Gosper_curve

## l-system rules
axiom = "A"

rules = {
    "A" : "A-B--B+A++AA+B-",
    "B" : "+A-BB--B-A++A+B"
}

generations = 5

## l-system interpretation rules
distance = 4
angle = 60
stack = ([], [])

draw_rules = {
    "A" : partial(t_draw, distance),
    "B" : partial(t_draw, distance),
    "-" : partial(t_turn_right, angle), 
    "+" : partial(t_turn_left, angle),
    "[" : partial(t_push, stack),
    "]" : partial(t_pop, stack),
    "X" : none,
    "Y" : none,
}

## Generate the lsys and draw it
s = generate(axiom, rules, generations)
t_init(pos = (-300,200))
draw_lsys(s, draw_rules)