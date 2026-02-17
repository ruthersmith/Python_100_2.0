# 🕹️ Project: Pong

Fully interactive program designed to replicate the classic arcade game "Pong"

Pong is a table tennis–themed arcade sports video game, featuring simple two-dimensional graphics, manufactured by Atari and originally released in 1972. It was one of the earliest arcade video games;
read more at: https://en.wikipedia.org/wiki/Pong

---

## 🎮 Gameplay

This implementation is a **two-player game**:

- **Player 1** uses the **Up** and **Down** arrow keys to control their paddle.
- **Player 2** uses the **W** and **S** keys to control their paddle.

### Objective

Each player must:

- Prevent the ball from passing their paddle.
- Score points by getting the ball past their opponent’s paddle.

---

## ⚙️ Technical Details

This project is built using **object-oriented programming (OOP)** concepts, including:

- Classes
- Objects
- Inheritance

---

## 🚀 Entry Point

The entry point for the application is the `main.py` file. <br>
How to run: `python main.py`

## Project Structure

- main.py — Entry point of the application. Handles game setup, main loop, and overall game flow.

- ball.py — Defines the Ball class, which inherits from Turtle and manages ball movement, collision detection, and bouncing behavior.

- paddle.py — Defines the Paddle class, which inherits from Turtle and handles paddle creation and player controls.

- scoreboard.py — Defines the Scoreboard class, which inherits from Turtle and manages score display and game information.
