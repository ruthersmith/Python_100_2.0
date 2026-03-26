from flask import Flask, render_template, request, redirect, url_for
from config import app, Book, db


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add",  methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        data = dict(request.form)
        new_book = Book(title=data['book_name'],
                        author=data['book_author'],
                        rating=data['book_rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add.html')

@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit(book_id):
    if request.method == "POST":
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        print(request.form)
        return redirect(url_for('home'))
    else:
        book_to_update = Book.query.get(book_id)
        print(f"To Edit {book_to_update}")
        return render_template('edit.html', book=book_to_update)

@app.route('/delete/<book_id>')
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
