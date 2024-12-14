from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def init_db():
    with sqlite3.connect("menu.db") as data:
        cursor = data.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS menu (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          description TEXT NOT NULL,
                          price TEXT NOT NULL)''')
        data.commit()

init_db()

def get_menu_items():
    with sqlite3.connect("menu.db") as data2:
        cursor = data2.cursor()
        cursor.execute("SELECT name, description, price FROM menu")
        return cursor.fetchall()

def add_menu_item(name, description, price):
    with sqlite3.connect("menu.db") as data2:
        cursor = data2.cursor()
        cursor.execute("INSERT INTO menu (name, description, price) VALUES (?, ?, ?)", (name, description, price))
        data2.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    menu_items = get_menu_items()
    return render_template("menu.html", menu_items=menu_items)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        price = request.form["price"]
        add_menu_item(name, description, price)
        return redirect(url_for("menu"))
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)