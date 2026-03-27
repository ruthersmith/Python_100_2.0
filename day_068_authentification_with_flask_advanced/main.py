from flask import render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import  login_user, login_required, current_user, logout_user
from config import create_app, db
from models import  User, getUserByEmail

app = create_app()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        if getUserByEmail(request.form.get('email')):
            flash("User already exist")
            return redirect(url_for("login"))

        password = generate_password_hash(request.form.get('password'))
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=password
        )

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        
        return redirect(url_for("secrets", name=new_user.name))
    else:
        return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # Find user by email entered.
        user = User.query.filter_by(email=email).first()

        if not user:
            flash(f"user with email {email} not found ")
        else:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("secrets", name=user.name))
            else:
                flash("Incorrect Password entered")

    return render_template("login.html")


@app.route('/secrets/<name>')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
