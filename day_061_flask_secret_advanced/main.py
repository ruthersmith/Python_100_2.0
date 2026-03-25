from flask import Flask, render_template
from login_form import LoginForm

app = Flask(__name__)
app.secret_key = "any-secret"


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    return render_template('login.html', form=loginForm)


if __name__ == '__main__':
    app.run(debug=True)
