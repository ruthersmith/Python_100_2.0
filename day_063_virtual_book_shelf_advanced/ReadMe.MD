# Virtual Bookshelf Flask App

This is a **simple Flask application** to practice **CRUD operations** with **SQLAlchemy**.  
It allows you to **create, read, update, and delete books** from a virtual bookshelf.

---

## Features

- CRUD routes for `Book` objects:
  - Create a new book
  - List all books
  - Update a book
  - Delete a book
- Uses **Flask** and **SQLAlchemy** for database management
- SQLite database stored in the `instance/` folder by default
- Uses `app.app_context()` to ensure SQLAlchemy has access to the Flask app

---

## Project Structure

```text
virtual-bookshelf/
│
├─ main.py         # Main Flask routes (CRUD)
├─ config.py       # App and database setup, Book model
├─ templates/      # HTML templates
└─ README.md
```

## Running the app

`python main.py` since `main.py` has the routes and imports the app from `config.py`.
