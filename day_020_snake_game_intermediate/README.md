# Project: Snake

Fully interactive program designed to replicate the classic Snake arcade game.
Learn more about the game genre here:
https://en.wikipedia.org/wiki/Snake_(video_game_genre)

## Description

The goal of the game is to control the snake using the arrow keys to move around the screen and eat food that appears at random locations. Each time the snake eats food, it grows longer and the score increases.

The game ends if the snake:

- Collides with the wall
- Collides with itself

## Technical Overview

This project is implemented using Object-Oriented Programming (OOP) principles, making use of:

- Classes
- Objects
- Inheritance

The entry point for the application is the `main.py` file. <br>
How to run: `python main.py`

## Project Structure

- `main.py`: Entry point of the application. Initializes the game components and runs the main game loop.
- `snake.py`: Defines the Snake class. The snake is composed of a list of Turtle objects representing each segment of the body.
- `food.py`: Defines the Food class, responsible for creating and positioning food at random locations on the screen.
- `scoreboard.py`: Defines the Scoreboard class, which extends the Turtle class. Responsible for displaying text on the screen, including the current score and the "Game Over" message.

## Controls

- Up Arrow – Move up
- Down Arrow – Move down
- Left Arrow – Move left
- Right Arrow – Move right

## Known Issues

- Closing the game window may sometimes raise a Turtle `Terminator` error in the console.
  This happens because the game loop continues running after the window is closed.
  The game still functions correctly.
