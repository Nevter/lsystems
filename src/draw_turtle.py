## Draws l-systems using turtle graphics
import turtle as t
import math

def t_draw_and_dot(distance):
    t.forward(distance) 
    t.dot()

def t_draw(distance):
    t.forward(distance) 

def t_turn_left(angle):
    t.left(angle)

def t_turn_right(angle):
    t.right(angle)   

def t_push_then_turn_left(stack, angle):
    stack[0].append(t.pos())
    stack[1].append(t.heading())
    t.left(angle)

def t_pop_then_turn_right(stack, angle):
    t.penup()
    t.setpos(stack[0].pop())
    t.setheading(stack[1].pop())
    t.pendown()
    t.right(angle) 

def t_push(stack):
    stack[0].append(t.pos())
    stack[1].append(t.heading())

def t_dot(size = 1, color = "black"):
    t.dot(size, color)

def t_triangle(base_length, base_angle = 60, color = None):
    heading = t.heading()
    side_length = ((base_length/2)/math.cos(math.radians(base_angle)))

    if color is not None: 
        t.fillcolor(color)
        t.begin_fill()

    t.left(90)
    t.forward(base_length/2)
    t.right(180-base_angle)
    t.forward(side_length)
    t.right(2*base_angle)
    t.forward(side_length)
    t.right(180-base_angle)
    t.forward(base_length/2)
    t.setheading(heading)

    t.end_fill()

def none():
    pass

def t_pop(stack):
    t.penup()
    t.setpos(stack[0].pop())
    t.setheading(stack[1].pop())
    t.pendown()

def t_init(pos = (0,-200), heading = 90):
    t.penup()
    t.setpos(pos)
    t.setheading(heading)
    t.pendown()
    t.speed(0)
    t.delay(0)
    t.ht()

def draw_lsys(sentence, draw_rules):
    for i in sentence: 
        draw_rules[i]() 
    t.done()