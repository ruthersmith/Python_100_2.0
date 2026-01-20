from turtle import Turtle


class Snake:
    """
        responsible for the snake
    """
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    SPEED = 10

    def __init__(self):
        self.turtles: list[Turtle]= []
        for i in range(3):
            self.grow_turtle()
        self.head: Turtle = self.turtles[0]

    def grow_turtle(self):
        new_turtle_square = self.add_square_to_turtle()

        if len(self.turtles) == 0:
            self.turtles.append(new_turtle_square)
        else:
            new_turtle_square.setx(self.turtles[-1].xcor() - 20)
            self.turtles.append(new_turtle_square)
            self.move_forward()
            new_turtle_square.color("white")


        new_turtle_square.showturtle()



    def add_square_to_turtle(self):
        turtle = Turtle(shape="square")
        turtle.hideturtle() # Keeping it invisible for now until it it's added to the snake Game 
        turtle.penup()
        turtle.speed("fastest")

        return turtle

    def move_forward(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].pos())
        self.turtles[0].forward(Snake.SPEED)

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