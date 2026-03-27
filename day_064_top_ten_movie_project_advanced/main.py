from flask import render_template, redirect, url_for, request
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


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = Movie.query.get(movie_id)
    edit_form = MovieForm(obj=movie)
    if request.method == "POST":
        movie.title = request.form["title"]
        movie.year = request.form["year"]
        movie.description = request.form["description"]
        movie.rating = request.form["rating"]
        movie.ranking = request.form["ranking"]
        movie.review = request.form["review"]
        movie.img_url = request.form["img_url"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form, movie=movie)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):    
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
