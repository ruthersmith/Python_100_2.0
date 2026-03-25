# Fake Flask Project – WTForms Playground

This is a **toy Flask project** meant for playing around with **WTForms**, routing, and templates.  
It’s intentionally simple, just to experiment with forms, validation, and basic navigation.

---

## Features

- Two routes:
  - `/` – The home page
  - `/login` – Login page using WTForms
- Login form checks for hardcoded credentials:
  - **Email:** `admin@example.com`
  - **Password:** `password`
- Depending on input, user is redirected to:
  - `success.html` → if credentials match
  - `denied.html` → if credentials are wrong

---

## Requirements

- flask
- flask-wtf
- email_validator

## Notes / Fun

This project is not for production, credentials are hardcoded.

## How to run

` python main.py`
