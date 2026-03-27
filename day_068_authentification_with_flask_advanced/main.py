from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


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
        print(request.form)
        return redirect(url_for("secrets", name=new_user.name))
    else:
        return render_template("register.html")


def getUserByEmail(email):
    return User.query.filter_by(email=email).first()


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
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
