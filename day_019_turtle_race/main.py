"""
    Author: Ruthersmith Bercy

    Turtle racing program built using the turtle module.

    At the start of the program, the user is prompted to choose the color
    of the turtle they believe will win the race
    (red, orange, yellow, green, blue, or purple).

    The race then begins, and turtles move across the screen until one
    reaches the finish line. After the race window is closed, the winning
    turtle’s color is printed to the console, and the user is informed
    whether their prediction was correct.

    How to run:
    python main.py
"""

from turtle import Turtle, Screen
import random


class TurtleRace:
    """
        Class responsible for handling the turtle race
    """

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 400

    MAX_SPEED = 10

    def __init__(self):
        self.screen = Screen()
        # setup allows to setup screen height and width
        self.screen.setup(width=TurtleRace.SCREEN_WIDTH, height=TurtleRace.SCREEN_HEIGHT)
        self.turtles: list[Turtle] = []


    def init_turtle(self):
        """ creates our six turtle object and places them at the starting line ready to race"""
        y_coord = 180
        for i in range(6):
            new_turtle = Turtle(shape="turtle")
            new_turtle.penup()
            new_turtle.color(self.colors[i % len(self.colors)])
            new_turtle.goto(x=-230, y=y_coord)
            y_coord -= 66
            self.turtles.append(new_turtle)

    def race(self):
        """
            Runs the turtle race loop.
            Returns:
                str: The color of the turtle that won the race.
        """
        while True:
            for turtle in self.turtles:
                turtle.forward(random.randint(0, TurtleRace.MAX_SPEED))
                if turtle.xcor() > 230:
                    return turtle.pencolor()

    def run(self):
        user_bet = self.screen.textinput(title="Make your bet", prompt="Which color turtle will win (red,orange,yellow,green,blue,purple)")
        self.init_turtle()

        if user_bet:
            winner = self.race()
            print(f'you guessed {user_bet}')
            if user_bet == winner:
                print(f"You win the bet, winner is {winner}")
            else:
                print(f"you lose the bet, winner is {winner}")
        else:
            print("No bet entered, race aborted")
            exit(1)

        self.screen.exitonclick()


if __name__ == '__main__':
    TurtleRace().run()