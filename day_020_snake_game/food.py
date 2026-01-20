from turtle import Turtle
import random


class Food(Turtle):
    """
        Represents food that the snake can consume.

        The food appears at random locations on the screen and is repositioned
        each time it is eaten by the snake.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")  # this way we don't see it be created and being moved to where it's going

        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)