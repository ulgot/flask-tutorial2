import sqlite3

connection = sqlite3.connect('database.db')

with open('schema4.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


cur.execute("INSERT INTO zadania (zadanie, priorytet) VALUES (?, ?)", 
            ('Wyrzuc smieci', 'niski'))
cur.execute("INSERT INTO zadania (zadanie, priorytet) VALUES (?, ?)", 
            ('Ścisz TV', 'wysoki'))

connection.commit()
connection.close()