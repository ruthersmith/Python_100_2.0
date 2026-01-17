"""
    Author: Ruthersmith Bercy

    Console-based Blackjack game.

    Implements a single-player, single round Blackjack game against a dealer using
    standard casino rules. The game follows a phase-based flow:
    deal, player turn, dealer turn, and round resolution.

    How to run:
        python main.py
"""

import random

class BlackJack:
    """
        Manages the state and flow of a Blackjack game.

        This class encapsulates the game loop, rule enforcement, and
        player/dealer interactions. The game is started by calling
        the `run()` method.
    """

    CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    LOGO = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

    def __init__(self):
        self.user_cards = []
        self.dealer_cards = []


    def _initialize_game(self, game_on):
        if game_on:
            print(BlackJack.LOGO)
            for i in range(2):
                self.user_cards.append(random.choice(BlackJack.CARDS))
                self.dealer_cards.append(random.choice(BlackJack.CARDS))
                
            self._print_stats(print_user=True, print_dealer=False)
            print (f"The dealer's first card is {self.dealer_cards[0]} ")


    def _player_turn(self):
        """
            Executes the player's turn.

            Allows the player to hit or stand until they either bust,
            reach 21, or choose to stand by inputting 'n'.
        """
        user_input = ''
        while user_input != 'n' and sum(self.user_cards) < 21:
            user_input = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_input == 'y':
                self.user_cards.append(random.choice(BlackJack.CARDS))
                print(f"Your cards {self.user_cards} current score: {sum(self.user_cards)}")
    


    def _dealer_turn(self):
        """
            Executes the dealer's turn.
            Allows the dealer to pick up a card as long of the sum of their cards is below 17
        """
       
        while(sum(self.dealer_cards) < 17  ):
                self.dealer_cards.append(random.choice(BlackJack.CARDS))


    def _print_stats(self, print_user, print_dealer): 

        if print_user:
            print(f"Your cards {self.user_cards}, sum {sum(self.user_cards)}")
        if print_dealer:
            print(f"dealer's cards {self.dealer_cards}, sum {sum(self.dealer_cards)}")  


    def _determine_result(self):

        if(sum(self.user_cards) > 21):
            print (f"The Player Bust, player's total {sum(self.user_cards)}, dealer wins")
            return

        if(sum(self.dealer_cards) > 21):
            print (f"The dealer Bust, dealer total {sum(self.dealer_cards)}, user wins")
            return

        if sum(self.user_cards) == sum(self.dealer_cards):
            print("It's a draw")
        elif sum(self.user_cards) > sum(self.dealer_cards):
            print("user wins")
        else:
            print("dealer wins")


    def run(self):
        game_on = True if input("Do you want to play a game of Blackjack 'y' to play: ") == 'y' else False
        if game_on:
            self._initialize_game(game_on)
            self._player_turn()
            self._dealer_turn()
            self._print_stats(True,True)
            self._determine_result()
      
                
if __name__ == "__main__":
    game = BlackJack()
    game.run()
