from flask import Flask, request
from flask_cors import CORS
import psycopg2
import json
from main import AI_Therapist

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="postgres")

#i hope this project works
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

@app.route('/ai-json', methods=['POST'])
def aiJson():
    # Get the username and email from the request body
    print("if you see this you did it")



    rating = request.json['rating']
    comments = request.json['comments']

    print(rating, comments)
    # Insert the data into the database
    #aiResponse = str(AI_Therapist(comments))

    aiResponse = str(AI_Therapist(str("RATING:" + rating +  " HISTORY:" + comments)))
    print(aiResponse)

    return {"aiResponse" : aiResponse}

if __name__ == '__main__':
    app.run()
