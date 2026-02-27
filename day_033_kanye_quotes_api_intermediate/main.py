"""
    Author: Ruthersmith Bercy

    Kanye Quote Generator (GUI Version)

    A graphical user interface application that displays random quotes
    from Kanye West using the Kanye REST API.

    Each time the main button is clicked, the program fetches a new
    quote from the API and updates the displayed text on the screen.

    The application is implemented as a single-class GUI program
    (`KanyeQuote`) and uses HTTP requests to retrieve quote data.

    ## Requirements (See the root README for environment setup instructions.)
    - requests (third-party library for HTTP requests)
    - tkinter (standard library)

     How to run:
        python main.py

"""

from tkinter import *
import requests

class KanyeQuote:

    def __init__(self):
        self.window = Tk()
        self.window.title("Kanye Says...")
        self.window.config(padx=50, pady=50)

        self.canvas = Canvas(width=300, height=414)
        self.background_img = PhotoImage(file="background.png")
        self.canvas.create_image(150, 207, image=self.background_img)
        self.quote_text = self.canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                        fill="white")
        self.canvas.grid(row=0, column=0)

        self.kanye_img = PhotoImage(file="kanye.png")
        self.kanye_button = Button(image=self.kanye_img, highlightthickness=0, command=self.get_quote)
        self.kanye_button.grid(row=1, column=0)


    def run(self):
        self.window.mainloop()
    

    def get_quote(self):
        new_quote = requests.get(url="https://api.kanye.rest/").json()['quote']
        self.canvas.itemconfig(self.quote_text, text=new_quote)

if __name__ == '__main__':
    KanyeQuote().run()

