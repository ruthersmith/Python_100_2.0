from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

class SnakeGame:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    UP_KEY = "Up"
    DOWN_KEY = "Down"
    RIGHT_KEY = "Right"
    LEFT_KEY = "Left"

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SnakeGame.SCREEN_WIDTH, height=SnakeGame.SCREEN_HEIGHT)
        self.screen.bgcolor("Black")
        self.screen.title("My Snake Game")
        self.game_is_on = True

    def run(self):
        scoreboard = ScoreBoard()
        snake = Snake()
        food = Food()
        self.screen.listen()
        self.screen.onkey(snake.up, SnakeGame.UP_KEY)
        self.screen.onkey(snake.down, SnakeGame.DOWN_KEY)
        self.screen.onkey(snake.left, SnakeGame.LEFT_KEY)
        self.screen.onkey(snake.right, SnakeGame.RIGHT_KEY)

        while self.game_is_on:

            snake.move_forward()
            # self.screen.update()

            # compare the distance between a turtle and another turtle
            if snake.head.distance(food) < 15:
                food.refresh()
                snake.grow_turtle()
                scoreboard.update(1)

            # detect collision with wall
            if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
                self.game_is_on = False
                scoreboard.game_over()

            # detect collision with tail
            for turtle_segment in snake.turtles[1:]:
                if turtle_segment.distance(snake.head) < 10:
                    self.game_is_on = False
                    scoreboard.game_over()

        self.screen.exitonclick()


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()