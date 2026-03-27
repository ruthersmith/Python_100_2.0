from config import create_app, db
from models import Movie

app = create_app()

# Delete the existing movies from the database (clear the database)
with app.app_context():
    Movie.query.delete()
    db.session.commit()

new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

with app.app_context():
    db.session.add(new_movie)
    db.session.commit()

    print("Database seeded!")