from flask import Flask, request
from flask_cors import CORS
import psycopg2
import json

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="postgres")


@app.route('/journal', methods=['POST'])
def journal():
    # Get the username and email from the request body
    print("if you see this you did it")


    rating = request.form.get('rating')
    comments = request.form.get('comments')

    # Insert the data into the database
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO journalEntries (rating,comments) VALUES (%s, %s)",
    (rating,comments))
    conn.commit()

    return 'added!'

@app.route('/journal-json', methods=['POST'])
def journalJson():
    # Get the username and email from the request body
    print("if you see this you did it")



    rating = request.json['rating']
    comments = request.json['comments']

    # Insert the data into the database
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO journalEntries (rating,comments) VALUES (%s, %s)",
    (rating, comments))
    conn.commit(),

    return {"message" : 'added!'}

if __name__ == '__main__':
    app.run()
