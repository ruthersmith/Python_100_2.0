# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:19:44 2021

@author: bercy
"""
# Password Generator Project
import random


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 14)
    nr_symbols = random.randint(2, 8)
    nr_numbers = random.randint(2, 8)
    total_characters = nr_letters + nr_symbols + nr_numbers

    password = []

    for char in range(total_characters):
        new_char = letters[random.randint(0, len(letters) - 1)]
        password.append(new_char)

    for i in range(nr_numbers):
        pass_index = random.randint(0, len(password) - 1)
        num_index = random.randint(0, len(numbers) - 1)
        password[pass_index] = numbers[num_index]

    for i in range(nr_symbols):
        pass_index = random.randint(0, len(password) - 1)
        symbol_index = random.randint(0, len(symbols) - 1)
        password[pass_index] = symbols[symbol_index]

    return "".join(password)


if __name__ == '__main__':
    password_generator()
