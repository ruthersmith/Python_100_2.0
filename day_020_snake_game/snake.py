from turtle import Turtle


class Snake:
    """
        responsible for the snake
    """
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.turtles = []
        for i in range(3):
            self.grow_turtle()
        self.head = self.turtles[0]
        self.speed = 10

    def grow_turtle(self):
        new_turtle_square = self.add_square_to_turtle()
        if len(self.turtles) == 0:
            self.turtles.append(new_turtle_square)
        else:
            new_turtle_square.setx(self.turtles[-1].xcor() - 20)
            self.turtles.append(new_turtle_square)

    def add_square_to_turtle(self):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.speed("fastest")

        return turtle

    def move_forward(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].pos())
        self.turtles[0].forward(self.speed)

    def up(self):
        if self.head.heading() != Snake.DOWN:
            self.head.setheading(Snake.UP)

    def down(self):
        if self.head.heading() != Snake.UP:
            self.head.setheading(Snake.DOWN)

    def left(self):
        if self.head.heading() != Snake.RIGHT:
            self.head.setheading(Snake.LEFT)

    def right(self):
        if self.head.heading() != Snake.LEFT:
            self.head.setheading(Snake.RIGHT)