# Top Movies – Flask Application

A simple **Flask CRUD application** that allows a user to maintain a personal list of their favorite movies.

This project demonstrates:

- Flask routing
- SQLAlchemy database models
- WTForms form handling
- CRUD operations
- Flask application factory pattern
- Basic database seeding

The goal of this project is to practice building a **structured Flask application** with a clear separation of responsibilities.

---

# Features

Users can:

- Add a movie to their list
- View all saved movies
- Update movie information
- Delete a movie

The application uses:

- **Flask**
- **SQLAlchemy**
- **WTForms**
- **SQLite**
- **boostrap**

---

# Project Structure

- main.py # Entry point of the application
- config.py # Application factory and database configuration
- models.py # SQLAlchemy models
- forms.py # WTForms definitions
- seeder.py # Script for inserting a sample movie into the database
- templates/ # Jinja2 templates
- instance/ # SQLite database location
- README.md

## How to Run

Run the application with: `python main.py` <br>
Then open: http://127.0.0.1:5000

## Seeding

Run `python seeder.py` <br>
seeder.py is a small script used to **seed the database with an example movie**.
