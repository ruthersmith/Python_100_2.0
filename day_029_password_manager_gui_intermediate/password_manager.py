"""
    Author: Ruthersmith Bercy

    Password Manager (GUI Version)
    
    An improved version of the Day 5 console-based random password generator,
    expanded into a full-featured password manager with a graphical user interface.

    This application allows users to:

    - Generate secure random passwords
    - Automatically copy generated passwords to the clipboard using `pyperclip`
    - Save login credentials (e.g., website, email/username, password)
    - Search for stored credentials
    - Manage saved password data

    Credentials are stored in a default `credentials.json` file (unencrypted;
    encryption is out of scope for this project).

    ## Requirements (See the root README for environment setup instructions.)
    - pyperclip

    How to run:
        python password_manager.py

"""
import os
import sys
import tkinter as tk
from tkinter import messagebox
import json
import random
import pyperclip

# add the path to the password generator folder
sys.path.append(os.path.abspath("../day_005_random_password_generator_beginner"))
from password_generator import PasswordGenerator

class PasswordManager:

    """
        Main controller for the Password Manager GUI application.

        Responsibilities:
        - Manage user interaction through the GUI
        - Handle password generation via the `password_generator` module
        - Save and retrieve credentials from a JSON file
        - Manage basic input validation

    """

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Manager")
        self.canvas = tk.Canvas(width=200, height=200)
        self.logo_img = tk.PhotoImage(file='logo.png')
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.window.config(padx=20, pady=20)
        self.canvas.grid(row=0, column=1)

        website_label = tk.Label(text='Website*:')
        website_label.grid(row=1, column=0)

        self.website_entry = tk.Entry()
        self.website_entry.grid(row=1, column=1, sticky="EW")
        self.website_entry.focus()

        search_btn = tk.Button(text='Search', command=self.search)
        search_btn.grid(row=1, column=2, sticky="EW")

        user_label = tk.Label(text='Email/Username*:')
        user_label.grid(row=2, column=0)

        self.user_entry = tk.Entry(width=35)
        self.user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

        password_label = tk.Label(text='Password:')
        password_label.grid(row=3, column=0)

        self.password_entry = tk.Entry(width=21)
        self.password_entry.grid(row=3, column=1, sticky="EW")

        password_generate_btn = tk.Button(text='Generate Password', command=self.handle_password_generation)
        password_generate_btn.grid(row=3, column=2)

        add_btn = tk.Button(text='Add', width=36, command=self.save_to_file)
        add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")


    def search(self, filename='credentials.json'):
        """
            Search for an existing entry for a particular website.

            Reads from the default JSON file (`credentials.json`) and displays
            the credentials if found. Triggered when the user clicks the "Search" button.

            Parameters:
            - filename (str): Path to the credentials file. Defaults to 'credentials.json'.
        """

        website_query = self.website_entry.get()
        try:
            with open(filename,'r') as file:
                data = json.load(file)
                entry = data[website_query]
                message = f"Username/Email: {entry['username']}\nPassword: {entry['password']}"
                messagebox.showinfo(title=website_query,message=message)
        except FileNotFoundError as error:
            messagebox.showerror(title='Error',message=f"No Data file found\n{error}" )
        except KeyError as error:
            messagebox.showerror(title="Error", message=f"No Entry for website {error} exist")


    def save_to_file(self, filename='credentials.json'):
        """Saves user-provided credentials to the JSON file after basic validation."""

        password = self.password_entry.get()
        username_email = self.user_entry.get()
        website = self.website_entry.get()

        new_data = {
            website: {
                "username": username_email,
                "password": password
            }
        }

        # make sure username and website are not empty
        if len(username_email) < 1 or len(website) < 1:
            messagebox.showwarning(title="Empty Fields", message="Complete required field to continue")
            return

        ask_user_to_confirm = f"Is it ok to save?\nusername: {username_email}\nPassword: {password}"
        is_ok = messagebox.askokcancel(title=website, message=ask_user_to_confirm)

        if is_ok:
            try:
                with open(filename, 'r') as file:
                    # reading existing data
                    data = json.load(file)
                    # updating with new data
                    data.update(new_data)

                with open(filename, 'w') as file:
                    # saving updated data
                    # indent optional, just makes it easier to read
                    json.dump(data, file, indent=4)

            except FileNotFoundError:
                with open(filename, 'w') as file:
                    json.dump(new_data, file, indent=4)
            finally:
                self.password_entry.delete(0, tk.END)
                self.website_entry.delete(0, tk.END)

    def handle_password_generation(self):
        """
            Generates a secure random password using the `password_generator` module
            when the user clicks the "Generate Password" button.

            The generated password is automatically inserted into the password field
            of the GUI and also saved to the clipboard
        """

        nr_letters = random.randint(8, 14)
        nr_symbols = random.randint(2, 8)
        nr_numbers = random.randint(2, 8)

        self.password_entry.delete(0, tk.END)
        new_password = PasswordGenerator.generate_password(nr_letters, nr_symbols, nr_numbers)
        self.password_entry.insert(0, new_password)
        pyperclip.copy(new_password)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.run()