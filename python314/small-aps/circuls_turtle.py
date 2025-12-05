from random import randint, choice
from turtle import Turtle, Screen



bob_the_turtle = Turtle()
bob_the_turtle.shape("turtle")
bob_the_turtle.pensize(2)
bob_the_turtle.speed("fastest")
screen = Screen()
screen.colormode(255)



def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color=(r,g,b)
    return color

def draw_shape(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        bob_the_turtle.circle(99)
        bob_the_turtle.pencolor((random_color()))
        current_heading = bob_the_turtle.heading()
        bob_the_turtle.setheading(current_heading + size_of_gap)

draw_shape(20)

screen.exitonclick()