import psycopg2


# conn = psycopg2.connect('dbname = postgres user = postgres')


conn = psycopg2.connect(database="postgres",
                       user="postgres",
                       password="postgres")


cur = conn.cursor()


cur.execute("SELECT * FROM registration;")


records = cur.fetchall()
print(records)
