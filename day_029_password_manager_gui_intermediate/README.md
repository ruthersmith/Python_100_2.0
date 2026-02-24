# Password Manager (GUI Version)

An improved version of the Day 5 console-based random password generator,
expanded into a full-featured password manager with a graphical user interface.

## Features

- Generate secure random passwords
- Automatically copy generated passwords to clipboard using `pyperclip`
- Save login credentials (website, username/email, password)
- Search for existing entries
- Credentials stored in `credentials.json` (unencrypted)
- GUI interface using `tkinter`

## Requirements

- Python 3.x
- tkinter (standard library)
- pyperclip

This project runs inside the shared repository virtual environment.
See the root README for environment setup instructions.

## Notes

- Passwords are stored in plaintext; encryption is out of scope.
- Designed as a single-file GUI application.

## Entry Point

password_manager.py
