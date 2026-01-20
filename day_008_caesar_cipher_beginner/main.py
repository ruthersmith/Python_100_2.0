"""
    Author: Ruthersmith Bercy

    Console-based Caesar Cipher application.

    This module defines the CaesarCipher class, which provides functionality
    to encrypt and decrypt text using the classic Caesar cipher technique.
    The application operates via the console and shifts alphabetic characters
    by a fixed number of positions while preserving non-alphabetic characters.

    How to run:
        python main.py
"""

class CaesarCipher:
    """
    Implements a Caesar cipher for encrypting and decrypting text.

    The cipher works by shifting each alphabetic character in the input
    text by a specified number of positions within the alphabet. Characters
    not found in the defined alphabet are left unchanged.

    Attributes:
        alphabet (list[str]): A list containing the characters used for
            encryption and decryption.
    """

    ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    LOGO = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
    
    def run(self):
        """
            Entry point for the Caesar Cipher console application.

            Handles user interaction, including collecting input text and
            shift values, and displays the resulting encrypted or decrypted
            output.
        """
        print(CaesarCipher.LOGO)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        new_text = ""

        if direction == 'encode':
            new_text = self._encrypt(text,shift)
        elif direction == 'decode':
            new_text = self._decrypt(text,shift)

        if new_text:
            print(new_text)

    def _encrypt(self, text : str, shift : int) -> str:
        """
            Encrypts text using a Caesar cipher shift.

            Iterates over each character in the input text. If the character
            exists in the alphabet list, its index is shifted by the given
            amount and wrapped using modular arithmetic. Characters not found
            in the alphabet are appended unchanged.

            Args:
                text (str): The text to encrypt.
                shift (int): The number of positions to shift each character.

            Returns:
                str: The encrypted text.
        """
        new_text_list = []
        text_list = list(text)
        
        for char in text_list:
            if  char in CaesarCipher.ALPHABET:
                new_char_index = (CaesarCipher.ALPHABET.index(char) + shift) % 26
                new_text_list.append(CaesarCipher.ALPHABET[new_char_index])
            else:
                new_text_list.append(char)

        return "".join(new_text_list)

    def _decrypt(self, text : str, shift : int) -> str:
        """
            Decrypts text encrypted with a Caesar cipher.

            Decryption is performed by reversing the shift value and delegating
            the operation to the internal encryption method.

            Args:
                text (str): The text to decrypt.
                shift (int): The original shift value used for encryption.

            Returns:
                str: The decrypted text.
        """
        shift *= -1
        return self._encrypt(text,shift)

if __name__ == "__main__":
    cipher = CaesarCipher()
    cipher.run()