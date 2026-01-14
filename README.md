Agro-Direct

A simple Flask-based web application for an agricultural marketplace — allowing farmers and buyers to interact, list products, and manage orders (CRUD operations).
(Note: Description is inferred from repository structure; update accordingly if your app purpose differs.)

🧠 Features

✔ Python Flask backend
✔ SQLite database for data storage (database.db)
✔ Dynamic HTML pages with templates
✔ Static assets (CSS/JS/Images)
✔ Basic user interface for product listing and management

📂 Project Structure
Agro-Direct/
├── app.py                  # Main Flask application
├── database.db             # SQLite database
├── static/                 # CSS, images, JS files
├── templates/              # HTML templates
├── README.md               # (You can add this file)

🛠️ Requirements

Python 3.8+

Flask

SQLite (built-in)

🚀 Installation & Setup

Clone the repository

git clone https://github.com/sameena-2004/Agro-Direct.git
cd Agro-Direct


Create and activate a Python virtual environment (recommended)

python3 -m venv venv
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate


Install dependencies

pip install flask


If your app uses additional packages, add them to requirements.txt and install with pip install -r requirements.txt.

⚙️ Configuration

No separate configuration file is included. If you want to configure Flask settings (e.g., debug mode, secret key), you can add:

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DEBUG'] = True


inside app.py.

🏃 Running the App
python app.py


Then open:

http://127.0.0.1:5000


in your browser.

💾 Database

The project includes an SQLite database file database.db.
If you want to reset or initialize the database manually, you can use sqlite3 or a Python script to create tables.

Example:

import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create your tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    description TEXT
)
""")
conn.commit()
conn.close()


(Adjust table fields based on your actual schema.)

📝 Contributing

Contributions are welcome!

Fork the repository

Create a feature branch

Commit changes

Raise a Pull Request

📌 License

Include your preferred license here (e.g., MIT License).

🙌 Acknowledgments

Thanks to everyone who contributes and supports this project.

👩‍💻 Author
Sameena Pathan
Data Science Student
GitHub: https://github.com/sameena-2004
