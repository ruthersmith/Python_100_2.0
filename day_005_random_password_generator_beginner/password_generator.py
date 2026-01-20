"""
    Author: Ruthersmith Bercy

    Random Password Generator

    A command-line utility and reusable module for generating random passwords.
    When run directly, the script prompts the user for the desired number of
    letters, symbols, and numbers, then generates and prints a random password.

    The core password generation logic is implemented in the PasswordGenerator
    class and exposed via the `generate_password` method, allowing other scripts
    to import and reuse it programmatically.

    How to run:
        python password_generator.py
"""


import random

class PasswordGenerator:

    """
    Generates random passwords composed of letters, symbols, and numbers.

    The `run_cmd` method provides an interactive command-line interface.
    The `generate_password` method can be used programmatically by other
    scripts to generate passwords with custom character counts.
    """

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def generate_password(self, nr_letters : int = 4, nr_symbols : int = 4, nr_numbers : int = 4):
        """
            Generates a random password.

            Args:
                nr_letters (int): Number of alphabetic characters.
                nr_symbols (int): Number of symbol characters.
                nr_numbers (int): Number of numeric characters.

            Returns:
                str: The generated password.
        """
        
        password = []
        password.extend(random.choices(PasswordGenerator.letters, k=nr_letters))
        password.extend(random.choices(PasswordGenerator.symbols, k=nr_symbols))
        password.extend(random.choices(PasswordGenerator.numbers, k=nr_numbers))

        random.shuffle(password)

        return "".join(password) 
    
    def run_cmd(self):

        print("Welcome to the PyPassword Generator!")

        nr_letters= int(input("How many letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        password = self.generate_password(nr_letters, nr_symbols, nr_numbers)
        print(f"Your password is {password}")

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run_cmd()