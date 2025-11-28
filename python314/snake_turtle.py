from random import randint, choice
from turtle import Turtle, Screen

bob_the_turtle = Turtle()
bob_the_turtle.shape("turtle")
bob_the_turtle.pensize(15)
bob_the_turtle.speed("fastest")
screen = Screen()
screen.colormode(255)

directions = [0,90,180,270]

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color=(r,g,b)
    return color


for _ in range(100):

    bob_the_turtle.forward(35)
    bob_the_turtle.pencolor((random_color()))
    bob_the_turtle.setheading(choice(directions))

screen.exitonclick()