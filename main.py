from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor('black')
s.title('Snake Game')
s.tracer(0)

snak = Snake()
food = Food()
scoreboard = Scoreboard()

s.listen()
s.onkey(snak.up, "Up")
s.onkey(snak.down, "Down")
s.onkey(snak.left, "Left")
s.onkey(snak.right, "Right")

game_is_on = True
while game_is_on:
    s.update()
    snak.move()
    time.sleep(0.08)

    # detecting collision
    if snak.head.distance(food) < 15:
        food.refresh()
        snak.extend()
        scoreboard.update()

    # detect wall collision
    if snak.head.xcor() > 280 or snak.head.xcor() < -280 or snak.head.ycor() > 280 or snak.head.ycor() < -280:
        scoreboard.reset_game()
        snak.reset()
        # game_is_on = False

    # head collision
    for i in snak.t[1:]:
        # if i == snak.head:
        #     continue
        if snak.head.distance(i) < 10:
            # game_is_on = False
            scoreboard.reset_game()
            snak.reset()
    snak.change = True


s.exitonclick()
