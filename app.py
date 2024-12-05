from flask import Flask, render_template

app = Flask(__name__)

menu_items = [
    {"name": "Маргарита", "description": "Томатний соус, моцарела, базилік", "price": "120 грн"},
    {"name": "Пепероні", "description": "Томатний соус, моцарела, пепероні", "price": "140 грн"},
    {"name": "Гавайська", "description": "Томатний соус, моцарела, шинка, ананас", "price": "150 грн"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html", menu_items=menu_items)

if __name__ == "__main__":
    app.run(debug=True)
