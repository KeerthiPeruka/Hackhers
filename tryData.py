from flask import Flask, request, render_template
from flask_cors import CORS
import psycopg2
from main import AI_Therapist
import jsonify

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres")

'''def index():
    return render_template('tryData.html')
'''
@app.route('/data', methods=['POST'])
def data():
    print("if you see this you did it")

    rating = request.form.get('rating')
    comments = request.form.get('comments')

    print(rating, comments)
    cur = conn.cursor()
    cur.execute("SELECT * FROM journalEntries")
    result = cur.fetchall()
    print(AI_Therapist(''.join(map(str, result[-1]))))
    cur.close()

    return 'added!'


@app.route('/data-json', methods=['POST'])
def dataJson():
    print("if you see this you did it")

    rating = request.json['rating']
    comments = request.json['comments']
    aiResponse = str(AI_Therapist(comments))
    print(aiResponse)
    return aiResponse
'''
cur = conn.cursor()
    cur.execute("SELECT rating, comments FROM journalEntries")
    result = cur.fetchall()

    print(AI_Therapist(''.join(map(str, result[-1]))))
    cur.close()
'''



if __name__ == '__main__':
    app.run()
