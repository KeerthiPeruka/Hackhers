from flask import Flask, request
from flask_cors import CORS
import psycopg2
import json

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="postgres")
@app.route('/')
def bad_dad():
    return 'Nanna makes me do such annoying work at so late at night'

@app.route('/create', methods=['POST'])
def create():
    # Get the username and email from the request body
    print("if you see this you did it")


    email = request.form.get('email')
    password = request.form.get('password')

    # Insert the data into the database
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO login (email,password) VALUES (%s, %s)",
    (email, password))
    conn.commit()

    return 'added!'

@app.route('/create-json', methods=['POST'])
def createJson():
    # Get the username and email from the request body
    print("if you see this you did it")


    email = request.json['email']
    password = request.json['password']

    # Insert the data into the database
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO login (email, password) VALUES (%s, %s)",
    (email, password))
    conn.commit(),

    return 'added!'

if __name__ == '__main__':
    app.run()
