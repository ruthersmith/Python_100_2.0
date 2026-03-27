from flask import Flask, render_template, redirect, url_for, request
from config import create_app, db
from models import Movie
from forms import MovieForm

app = create_app()


@app.route("/")
def home():
    movie_list = db.session.query(Movie).all()
    return render_template("index.html", movies=movie_list)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_movie = Movie(
            title=request.form["title"],
            year=request.form["year"],
            description=request.form["description"],
            rating=request.form["rating"],
            ranking=request.form["ranking"],
            review=request.form["review"],
            img_url=request.form["img_url"],
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=MovieForm())


if __name__ == '__main__':
    app.run(debug=True)
