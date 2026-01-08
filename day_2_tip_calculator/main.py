class TipCalculator:

    """
        A simple calculator for splitting a bill with tip among multiple people.

        The class exposes a single public method, `run`, which computes how much
        each person should pay after adding a percentage-based tip to the total bill.
    """
    
    def run(self) -> None:

        """
          Calculate the amount each person should pay.
        """

        print("Welcome to the Tip Calculator")
        bill_total = self._get_input("What was the total bill? ")
        tip_percent = self._get_input("How much tip would you like to give in percent 10, 12, or 15? ")
        num_of_people = self._get_input("How many people to split the bill? ")

        bill_total_with_tips = bill_total + ( tip_percent / 100 * bill_total)
        bill_per_person = round(bill_total_with_tips / num_of_people, 2)

        print(f"Each Person should pay: {bill_per_person}")

    def _get_input(self, prompt: str) -> float| None:
        """
            Get the user's input and try to cast it into a float, exits program otherwise        
            `prompt` Prompt to display to the user       
        """

        user_input = input(prompt)

        try:
            user_input = float(user_input)
            return user_input
        except ValueError as e:
            print(f"Error Occured, Invalid input, Expecting a number, received '{user_input}'")
            exit(code=-1)


if __name__ == "__main__":
    calculator = TipCalculator()
    calculator.run()