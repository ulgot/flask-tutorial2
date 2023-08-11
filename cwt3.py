import sqlite3
from flask import Flask, render_template, request, redirect, url_for

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('start3.html')

@app.route('/about')
def about():
    return render_template('about3.html')

@app.route('/maciej')
def maciej():
    return render_template('maciej3.html')

# @app.route('/zadania')
# def zadania():
#     return render_template('zadania3.html')

@app.route('/zadania', methods=['POST', 'GET'])
def zadania():
    if request.method == 'POST':
        zadanie = request.form['zadanie']

        try:
            conn = get_db_connection()
            conn.execute('INSERT INTO zadania (zadanie) VALUES (?)', (zadanie, ))
            conn.commit()
            conn.close()

            return redirect(url_for('zadania'))
        except:  # noqa: E722
            return 'DB error'
        
    else:
        conn = get_db_connection()
        zadania = conn.execute('SELECT * FROM zadania').fetchall()
        conn.close()
        return render_template('zadania3A.html', zadania=zadania)
        # return render_template('zadania3.html', zadania=zadania)

if __name__ == "__main__":
    app.run(debug=True)