from turtle import Screen
from paddle import Paddle

screen=Screen()


screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)#turn off animation


right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))


screen.listen()
screen.onkey(right_paddle.goUp,"Up")
screen.onkey(right_paddle.goDown,"Down")
screen.onkey(left_paddle.goUp, "w")
screen.onkey(left_paddle.goDown, "s")

is_game_on=True

while is_game_on:
    screen.update()


screen.exitonclick()
