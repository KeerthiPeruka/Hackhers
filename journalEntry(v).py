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

@app.route('/journal', methods=['POST'])
def journal():
    # Get the username and email from the request body
    print("if you see this you did it")


    date = request.form.get('date')
    rating = request.form.get('rating')
    comments = request.form.get('comments')

    # Insert the data into the database
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO journalEntries (date,rating,comments) VALUES (%s, %s, %s)",
    (date,rating,comments))
    conn.commit()

    return 'added!'

@app.route('/journal-json', methods=['POST'])
def journalJson():
    # Get the username and email from the request body
    print("if you see this you did it")


    date = request.json['date']
    rating = request.json['rating']
    comments = request.json['comments']

    # Insert the data into the database
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO journalEntries (date,rating,comments) VALUES (%s, %s, %s)",
    (date, rating, comments))
    conn.commit(),

    return 'added!'

if __name__ == '__main__':
    app.run()
