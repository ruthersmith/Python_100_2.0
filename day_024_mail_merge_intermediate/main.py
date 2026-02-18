"""
    Author: Ruthersmith Bercy

    Mail Merge Program
    A simple program to create personalized letters for multiple recipients.

    The program uses two input files:
    1. Template file: contains the letter text with the placeholder '[name]' 
    for the recipient’s name.
    2. Names file: contains a list of recipients, one name per line.

    Behavior:
    - Replaces '[name]' in the template with each recipient's name.
    - Generates a personalized letter for each recipient.

    Future Improvements:
    - Allow the user to specify a custom placeholder instead of being limited to '[name]'.

    How to run:
        python main.py

"""

class MailMerge:

    """
    Handles the mail merge process for a batch of recipients.

    Attributes:
        letter_path (str): Path to the template file containing '[name]' placeholder.
        names_path (str): Path to the file containing recipient names.

    Methods:
      run(): Generates a personalized letter for each recipient and saves it 
           to the `Output` directory. Each file is named by appending 
           `_letter.txt` to the recipient's name.
    """

    def __init__(self, letter_path, names_path):
        with open(letter_path) as letter_file:
            self.letter = letter_file.read()

        with open(names_path) as name_file:
            self.names = name_file.readlines()

    def run(self):
        base_path = "./Output"
        for name in self.names:
            path = f"{base_path}/{name.strip()}_letter.txt"
            file = open(path, "w")
            file.write(self.letter.replace('[name]', name.strip()))
            file.close()


if __name__ == "__main__":
    path_to_letter = "./Input/Letters/starting_letter.txt"
    path_to_names = "./Input/Names/invited_names.txt"
    mail_merge = MailMerge(path_to_letter, path_to_names)
    mail_merge.run()
