# Café Info API

This is a **simple web API** built using **Flask**, **SQLAlchemy**, and **SQLite**.  
It provides a mock service that gives details about different cafés in various locations.

---

## Features

- RESTful API endpoints for cafés
- SQLite database managed with SQLAlchemy
- Easy to run locally for testing or development
- API documentation available via Postman

---

## Project Structure

- main.py # Flask app, routes, and database initialization
- models.py # SQLAlchemy models for the database
- instance/ # SQLite database file (cafe.db), populated one included for easy testing and spin up
- README.md

---

## How to run

`python main.py` The server will start on http://127.0.0.1:5000/ by default.

---

The api documentation can be found at
https://documenter.getpostman.com/view/11450572/UyrGAtjA
