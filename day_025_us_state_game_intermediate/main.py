"""
    Author: Ruthersmith Bercy

    US State Quiz Game

    An educational GUI quiz game that tests the user's knowledge of U.S. states.

    The program displays a map of the United States and prompts the user to
    enter state names. Each time the user enters the name of a valid state,
    the program writes the state name onto the map at the correct location,
    using coordinates from the accompanying '50_states.csv' file.

    The game ends when:
    - The user correctly guesses all 50 states, or
    - The user exits the game.

    When the game ends, any states that were not guessed are printed to the console.

    ## Requirements (See the root README for environment setup instructions.)
    - pandas

    How to run:
        python main.py

"""
import turtle
import pandas
import time


class UsStateGame:
    """
        Main controller for the US State Quiz Game.

        Responsible for:
        - Loading state data from the CSV file
        - Handling user input
        - Displaying correctly guessed states on the map
        - Managing game termination logic
    """

    IMAGE_PATH = "blank_states_img.gif"
    DATA_PATH = '50_states.csv'

    def __init__(self):
        self.data = pandas.read_csv(UsStateGame.DATA_PATH)
        self.correct_guesses = 0
        self.already_guessed = []
        self.screen = turtle.Screen()
        self.screen.title('U.S State Game')
        self.screen.addshape(UsStateGame.IMAGE_PATH)
        turtle.shape(UsStateGame.IMAGE_PATH)

        self.writer = turtle.Turtle()
        self.writer.penup()
        self.writer.hideturtle()

    def exist(self, answer):
        """Check if the user input is a state and not already guessed"""
        row_returned = self.data[self.data.state == answer]
        if len(row_returned) == 1 and row_returned.state.values[0] not in self.already_guessed:
            self.show_state(row_returned)
            self.already_guessed.append(row_returned.state.values[0])
            self.correct_guesses += 1

    def show_state(self, row_returned):
        """
            Displays the correctly guessed state name on the map
            at its corresponding coordinates.
        """
        self.writer.goto(int(row_returned.x.item()), int(row_returned.y.item()))
        self.writer.write(row_returned.state.values[0])

    def run(self):
        """
            Starts and manages the main game loop.

            Continuously prompts the user for state names until
            all 50 states are guessed or the user exits the game.
        """
        while self.correct_guesses < 50:
            answer = self.screen.textinput(title=f'{self.correct_guesses}/50 states correct',
                                           prompt="Enter other state")
            if answer is None:
                break
            else:
                answer = answer.title()
                self.exist(answer)
                time.sleep(0.5)

        # print all the state that are missing, if exit the game
        print("missing states:")
        print(self.data.state[~self.data.state.isin(self.already_guessed)].values)
        # alternative to exit on click, closes when x is clicked not just anywhere
        self.screen.mainloop()


if __name__ == "__main__":
    state_game = UsStateGame()
    state_game.run()
