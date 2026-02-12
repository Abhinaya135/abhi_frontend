from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhinaya@4577",  # replace with your MySQL password
    database="contactdb"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('contactus.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Insert data into MySQL
    sql = "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)"
    val = (name, email, message)
    cursor.execute(sql, val)
    db.commit()

    return f"<h2>Thanks {name}, your message was saved to the database!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
