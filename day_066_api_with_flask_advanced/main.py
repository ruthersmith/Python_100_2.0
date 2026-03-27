from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    """ returns a random cafe """
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    print(random_cafe.coffee_price)
    return jsonify(cafe=random_cafe.to_dict())

# Get all the cafes in the db
@app.route("/all")
def get_all_cafe():
    """ returns all the cafe """
    cafe_objects = db.session.query(Cafe).all()
    cafes = []
    for cafe in cafe_objects:
        cafes.append(cafe.to_dict())
    return jsonify(cafes=cafes)

## HTTP GET - Read Record
@app.route("/search")
def search():
    """
     record by location passed in as a url parameter
     http://127.0.0.1:5000/search?loc={location}
     """
    param = request.args.get("loc")
    cafe_objects = Cafe.query.filter_by(location=param)
    cafes = []
    for cafe in cafe_objects:
        cafes.append(cafe.to_dict())
    print(cafe_objects)
    return jsonify(cafe=cafes)

## HTTP POST - Create Record
@app.post("/add")
def add_cafe():
    """Adds a new cafe to the db"""
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@app.patch("/update-price/<id>")
def update_price(id):
    """
     Updates the price expected url is
    /update-price/{id}?new_price={new_price}
    """
    new_price = request.args.get("new_price")
    if not new_price:
        return jsonify(error={"Error": "No new price"}), 404

    cafe = Cafe.query.get(id)
    if cafe:
        print(f"changing old price {cafe.coffee_price} to new price {new_price}")
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 400

## HTTP DELETE - Delete Record
@app.delete("/report-closed/<cafe_id>")
def delete_cafe(cafe_id):
    """
    delete a cafe from the database only if they have the top secret api key
    http://127.0.0.1:5000/report-closed/{id}?api-key={API_KEY}
    """
    secret_key = "TopSecretAPIKey"
    input_key = request.args.get("api-key")
    if input_key != secret_key:
        return jsonify(error={"error": "Not allowed, correct api key required"}), 403

    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404



if __name__ == '__main__':
    app.run(debug=True)
