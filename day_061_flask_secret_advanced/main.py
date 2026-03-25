from flask import Flask, render_template
from login_form import LoginForm


app = Flask(__name__)
app.secret_key = "any-secret" # This is required to use CSRF with WTForms


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()

    if loginForm.validate_on_submit():

        email = loginForm.email.data
        password = loginForm.password.data
        
        if email == "admin@example.com" and password == "password":
            return render_template("success.html")
        else:
            return render_template("denied.html")
        
        
    return render_template('login.html', form=loginForm)


if __name__ == '__main__':
    app.run(debug=True)
