from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DB_NAME = "database.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS farmers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        location TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS crops (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        farmer_id INTEGER,
        crop TEXT,
        price TEXT,
        quantity TEXT,
        FOREIGN KEY (farmer_id) REFERENCES farmers(id)
    )
    """)

    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/farmer/register", methods=["GET", "POST"])
def farmer_register():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        location = request.form["location"]

        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO farmers (name, phone, location) VALUES (?, ?, ?)",
            (name, phone, location)
        )
        conn.commit()

        farmer_id = cur.lastrowid
        conn.close()

        return redirect(url_for("farmer_dashboard", farmer_id=farmer_id))

    return render_template("farmer_register.html")

@app.route("/farmer/<int:farmer_id>")
def farmer_dashboard(farmer_id):
    conn = get_db()

    farmer = conn.execute(
        "SELECT * FROM farmers WHERE id=?", (farmer_id,)
    ).fetchone()

    crops = conn.execute(
        "SELECT * FROM crops WHERE farmer_id=?", (farmer_id,)
    ).fetchall()

    conn.close()
    return render_template("farmer_dashboard.html", farmer=farmer, crops=crops)

@app.route("/add_crop/<int:farmer_id>", methods=["GET", "POST"])
def add_crop(farmer_id):
    if request.method == "POST":
        crop = request.form["crop"]
        price = request.form["price"]
        quantity = request.form["quantity"]

        conn = get_db()
        conn.execute(
            "INSERT INTO crops (farmer_id, crop, price, quantity) VALUES (?, ?, ?, ?)",
            (farmer_id, crop, price, quantity)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("farmer_dashboard", farmer_id=farmer_id))

    return render_template("add_crop.html", farmer_id=farmer_id)

@app.route("/buyer")
def buyer_dashboard():
    conn = get_db()
    crops = conn.execute("""
        SELECT crops.crop, crops.price, crops.quantity,
               farmers.name, farmers.phone, farmers.location
        FROM crops
        JOIN farmers ON crops.farmer_id = farmers.id
    """).fetchall()
    conn.close()

    return render_template("buyer_dashboard.html", crops=crops)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
