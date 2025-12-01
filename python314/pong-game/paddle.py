from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.hideturtle()
        self.goto(position)
        self.showturtle()

    def go_up(self):
        new_y = self.ycor() + 30
        self.sety(new_y)


    def go_down(self):
        new_y = self.ycor() - 30
        self.sety(new_y)




