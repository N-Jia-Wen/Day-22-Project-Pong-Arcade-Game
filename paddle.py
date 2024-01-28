from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.setheading(UP)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.setheading(UP)
        self.forward(40)

    def move_down(self):
        self.setheading(DOWN)
        self.forward(40)
