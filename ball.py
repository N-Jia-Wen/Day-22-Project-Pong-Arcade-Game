from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.setheading(45)
        self.move_speed = 5

    # Model answer adds to the x coord and y coord by a fixed amount (10)
    # for ball_move and assigns this amount to 2 attributes (self.x_move and self.y_move):
    def ball_move(self):
        self.forward(self.move_speed)

    def wall_bounce(self):
        self.setheading(360 - self.heading())

    def paddle_bounce(self):
        self.setheading(540 - self.heading())
        self.move_speed += 1

    def reset_position(self):
        self.goto(0, 0)
        self.setheading(self.heading() + 270)
        self.move_speed = 10
