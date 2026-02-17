from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


class PongGame:
    PADDLE_1_UP_KEY = "Up"
    PADDLE_1_DOWN_KEY = "Down"
    PADDLE_2_UP_KEY = 'w'
    PADDLE_2_DOWN_KEY = 's'

    is_multiplayer = True
    game_is_on = True

    def run(self):
        screen = Screen()
        screen.bgcolor('black')
        screen.setup(width=800, height=600)
        screen.title('Pong')
        screen.listen()
        screen.tracer(0)

        self.print_starting_info()

        # init scoreboard
        score_bord = Scoreboard()

        # First or Right paddle
        paddle_1 = Paddle(x=350, y=0)
        screen.onkey(paddle_1.go_up, PongGame.PADDLE_1_UP_KEY)
        screen.onkey(paddle_1.go_down, PongGame.PADDLE_1_DOWN_KEY)

        # Second or Left Paddle
        paddle_2 = Paddle(x=-350, y=0)
        if PongGame.is_multiplayer:
            screen.onkey(paddle_2.go_up, PongGame.PADDLE_2_UP_KEY)
            screen.onkey(paddle_2.go_down, PongGame.PADDLE_2_DOWN_KEY)

        # Ball
        ball = Ball()

        while PongGame.game_is_on:
            time.sleep(0.1)
            screen.update()
            ball.move()

            # check collision with  paddle
            if ball.distance(paddle_1) < 40 and ball.xcor() > 320:
                ball.moving_x_factor = -1 * ball.moving_x_factor
            elif ball.distance(paddle_2) < 50 and ball.xcor() < -320:
                ball.moving_x_factor = -1 * ball.moving_x_factor

            if ball.should_reset:
                # if ball is on left side, point goes to right
                score_bord.clear()
                if ball.xcor() < 0:
                    score_bord.r_point()
                else:
                    score_bord.l_point()
                ball.reset_pos()

        screen.exitonclick()

    def print_starting_info(self):
        """
            prints to the console som useful info
            acts kinda like a log for the beginning of the game
            useful for debugging to know what is happening at the beginning of the game
            with any Flags
        :return:
        """

        print("Game is starting")
        print("Game Mode: Multiplayer") if PongGame.is_multiplayer else print("Game Mode: Against AI")


if __name__ == '__main__':
    game = PongGame()
    game.run()