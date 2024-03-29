from flask import Flask, request
from flask_cors import CORS
import psycopg2
import json

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="postgres")

@app.route('/create', methods=['POST'])
def create():
    # Get the username and email from the request body
    print("if you see this you did it")


    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    email = request.form.get('email')
    password = request.form.get('password')
    passwordRedo = request.form.get('passwordRedo')

    # Insert the data into the database
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO registration (firstName, lastName, email, password, passwordRedo) VALUES (%s, %s, %s, %s, %s)",
    (firstName, lastName, email, password, passwordRedo))
    conn.commit()

    return 'added!'

@app.route('/create-json', methods=['POST'])
def createJson():
    # Get the username and email from the request body
    print("if you see this you did it")


    firstName = request.json['firstName']
    lastName = request.json['lastName']
    email = request.json['email']
    password = request.json['password']
    passwordRedo = request.json['passwordRedo']

    # Insert the data into the database
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO registration (firstName, lastName, email, password, passwordRedo) VALUES (%s, %s, %s, %s, %s)",
    (firstName, lastName, email, password, passwordRedo))
    conn.commit(),

    return 'added!'

if __name__ == '__main__':
    app.run()
