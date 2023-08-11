import sqlite3

connection = sqlite3.connect('database.db')

with open('schema7.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO user (uname) VALUES (?)", 
            ('admin', ))
cur.execute("INSERT INTO user (uname) VALUES (?)", 
            ('maciej', ))

cur.execute("INSERT INTO zadania (zadanie, priorytet, uname) VALUES (?, ?, ?)", 
            ('Wyrzuc smieci', 'niski', 'admin'))
cur.execute("INSERT INTO zadania (zadanie, priorytet, uname) VALUES (?, ?, ?)", 
            ('Ścisz TV', 'wysoki', 'maciej'))

connection.commit()
connection.close()