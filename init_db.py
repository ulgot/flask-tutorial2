import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO zadania (zadanie) VALUES (?)", ('Wyrzuc smieci',))
cur.execute("INSERT INTO zadania (zadanie) VALUES (?)", ('Ścisz TV',))

connection.commit()
connection.close()