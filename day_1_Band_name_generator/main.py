
class BandNameGenerator:

    ''''
        This is a simple class to create a user's possible band name by 
        getting as input the name of the city the user grew up on and the name of their pet
        and combining them.
    '''

    def run(self):
        print("Welcome to the Band Name Generator")
        city = input("What is the name of the city you grew up in: ")
        pet = input("What is the name of your pet: ")
        print(f"Your band name could be {city} {pet}")

if __name__ == "__main__":
    generator = BandNameGenerator()
    generator.run()