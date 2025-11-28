import random
from turtle import Turtle, Screen

bob_the_turtle = Turtle()
bob_the_turtle.shape("turtle")
bob_the_turtle.color("red")
bob_the_turtle.pensize(3)

colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]


def draw_shape(sides):
    angel = 360 / sides
    for _ in range( sides ):
        bob_the_turtle.forward(80)
        bob_the_turtle.right(angel)


for shap_sides in range(3,11):
    draw_shape(shap_sides)
    bob_the_turtle.color(random.choice(colors))


screen = Screen()
screen.exitonclick()