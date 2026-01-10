import random

class Game:

    """
        A simple Rock-Paper-Scissors command-line game.

        This class encapsulates the full game loop for a single round of
        Rock-Paper-Scissors. The user is prompted to enter either "rock",
        "paper", or "scissors". The computer then randomly selects one of
        the same options, and the outcome (win, lose, or tie) is determined
        and printed to the console.

        Rock wins against scissors, Scissors win against paper, Paper  wins against rock 

        The `run()` method serves as the 'public' entry point and coordinates
        user input, computer choice generation, outcome evaluation, and
        output display.
    """

    def _get_ascii(self, player_input):

        ascii_dict = {
            "rock" : '''
                    _______
                ---'   ____)
                    (_____)
                    (_____)
                    (____)
                ---.__(___)
                ''',

            "paper" : '''
                    _______
                ---'   ____)____
                        ______)
                        _______)
                        _______)
                ---.__________)
                ''',
            "scissors" : '''
                    _______
                ---'   ____)____
                        ______)
                    __________)
                    (____)
                ---.__(___)
                '''
        }
        return ascii_dict[player_input]

        

    def run(self):
        """
        Runs a single round of the Rock-Paper-Scissors game.
        """
        choices = ['rock', 'paper', 'scissors']
        user_input = input("what do you choose type 'rock', 'paper' or 'scissors': ")
        ai_choice = random.choice(choices)

        print(f"You choose {user_input} {self._get_ascii(user_input)}")
        print(f"The computer choose {ai_choice} {self._get_ascii(ai_choice)}")

        if user_input == ai_choice:
            print("it was a draw")
        elif (user_input == 'rock' and ai_choice == 'scissors') \
                or (user_input == 'scissors' and ai_choice == 'paper') \
                or (user_input == 'paper' and ai_choice == 'rock') :
            print("user wins")
        else:
            print("computer wins")


if __name__ == "__main__":
    Game().run()