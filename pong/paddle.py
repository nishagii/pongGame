from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        self.color("white")

    def goUp(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def goDown(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
