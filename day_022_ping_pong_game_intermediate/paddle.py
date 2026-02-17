from turtle import Turtle


class Paddle(Turtle):
    """
        Represents a player's paddle.

        Responsible for paddle creation and vertical movement
        based on user input. Inherits from Turtle.
    """

    MOVE_OFFSET = 20

    def __init__(self, x, y, shape='square', color='white'):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.color(color)
        self.shape(shape)
        self.setx(x)
        self.sety(y)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        """
        when calls move the paddle up along the y access by the MOVE_OFFSET
        :return:
        """
        new_y = self.ycor() + Paddle.MOVE_OFFSET
        self.goto(self.xcor(),new_y)

    def go_down(self):
        """
        when calls move the paddle down along the y access by the MOVE_OFFSET
        :return:
        """
        new_y = self.ycor() - Paddle.MOVE_OFFSET
        self.goto(self.xcor(), new_y)