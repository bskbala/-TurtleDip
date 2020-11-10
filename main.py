# Turtle Dip using Functions

import turtle
bsk = turtle.Turtle()
bsk.shape("turtle")
bsk.color("blue")

def triangle():
    bsk.left(60)
    bsk.forward(30)
    bsk.left(120)
    bsk.left(30)
    bsk.left(120)
    bsk.forward(30)
triangle()