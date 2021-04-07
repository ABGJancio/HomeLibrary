from flask import Flask, request, redirect, render_template, url_for

from forms import BookForm
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwerty"


@app.route("/api/v1/books/", methods=["GET", "POST"])
def books_list_api_v1():
    form = BookForm()
    error = ""

    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
        return redirect(url_for("books_list_api_v1"))

    return render_template("books.html", form=form, books=books.all(), error=error)


@app.route("/api/v1/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id)
    print(book)
    form = BookForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id, form.data)
        return redirect(url_for("books_list_api_v1"))

    return render_template("book.html", form=form, book=book, book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)
