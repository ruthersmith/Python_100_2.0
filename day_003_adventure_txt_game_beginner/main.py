
"""
Author: Ruthersmith Bercy
Choose-Your-Own-Adventure Game Module.

This module implements a simple text-based choose-your-own-adventure game.
The game is composed of a sequence of predefined steps that the player must successfully complete in order to win.

Classes
-------
Game
    Orchestrates the overall game flow. It introduces the game, iterates
    through a predefined list of GameStep instances, and determines whether
    the player wins or loses.

GameStep
    Represents a single decision point in the game. Each step prompts the
    player for input and evaluates whether the chosen option is correct.

How to run:
        python main.py

"""


class GameStep:

    """
    Represents a single decision point in the adventure game.

    A GameStep encapsulates all logic required to run one step of the game.
    When executed via `run`, it:
    - Prompts the user for input
    - Compares the input against the correct choice
    - Displays an appropriate failure message for incorrect input

    Parameters
    ----------
    prompt : str
        The text prompt presented to the player.
    correct_choice : str
        The expected input that represents the correct choice.
    wrong_choice_messages : dict[str, str]
        A mapping of user inputs to failure messages. This dictionary
        should typically contain a default failure message and may
        optionally include more specific messages for particular
        incorrect inputs.
    """
    
    def __init__(self, prompt : str, correct_choice : str, wrong_choice_message : dict):
        self.prompt : str = prompt
        self.correct_choice : str = correct_choice
        self.wrong_choice_message : dict = wrong_choice_message
        self.end_game : bool = False

    def run(self):
        user_input=input(self.prompt) 

        if user_input != self.correct_choice:
            self.end_game = True

            if user_input in self.wrong_choice_message.keys():
                print(self.wrong_choice_message[user_input])
            else:
                print(self.wrong_choice_message["default"])
    

class Game:
    """
        Controls the flow of the choose-your-own-adventure game.

        The Game class owns a predefined sequence of GameStep instances and
        controls the overall game flow. Calling `run`:
        - Introduces the game to the player
        - Executes each GameStep in order
        - Ends the game immediately if any step is failed
        - Declares a win if all steps are completed successfully

        The list of steps is defined as a class-level attribute.
      
    """

    game_steps : list[GameStep] = [

        GameStep("You are at a crossroad, where do you want to go?\nType 'left' or 'right': ", 
                 "left",
                 {"default" : "Fall into a hole. Game Over."}),
        GameStep("You've come to a lake. There is an island in the middle of the lake. type \"wait\" to wait for a boat. Type \"swim\" to swim across: ",
                 "wait",
                 {"default" : "Attacked by trout. GameOver."}),

        GameStep("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?: ",
                "yellow",
                {
                    "default" : "Game Over.",
                    "red" : "Burned by fire. Game Over.",
                    "blue" : "Eaten by beasts.Game Over."
                }
        )
                                          
    ]

        
        

    art = r"""
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
"""


    def run(self):
        """Runs the game from start to finish."""

        user_won = True
        print (self.art)
        print("Welcome to Treasure Island.\nYour mission is to find the treasure.")


        for step in self.game_steps:
            step.run()
            if step.end_game:
                user_won = False
                break
        
        if user_won:
            print("You found the trasure, you win!")

if __name__ == "__main__":
    game = Game()
    game.run()