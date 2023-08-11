import sqlite3
from flask import Flask, render_template, request, redirect, url_for, abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_zad(id):
    conn = get_db_connection()
    zad = conn.execute('SELECT * FROM zadania WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if zad is None:
        abort(404)
    return zad


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

@app.route('/zadania', methods=['POST', 'GET'])
def zadania():
    if request.method == 'POST':
        zadanie = request.form['zadanie']
        priorytet = request.form.get('priorytet')

        if priorytet.lower() not in ['wysoki', 'normalny', 'niski']:
            msg = 'priorytet: wysoki, normalny, niski'
            return render_template('flash_info.html', msg=msg, backurl='zadania')

        try:
            conn = get_db_connection()
            conn.execute('INSERT INTO zadania (zadanie, priorytet) VALUES (?, ?)', 
                         (zadanie, priorytet))
            conn.commit()
            conn.close()

            return redirect(url_for('zadania'))
        except:  # noqa: E722
            msg = 'DB error while INSERT'
            return render_template('flash_info.html', msg=msg, backurl='zadania')
        
    else:
        conn = get_db_connection()
        zadania = conn.execute('SELECT * FROM zadania').fetchall()
        conn.close()
        return render_template('zadania5.html', zadania=zadania)

@app.route('/delete/<int:id>')
def del_zadanie(id):
    zadanie = get_zad(id)
    try:
        conn = get_db_connection()
        conn.execute('DELETE FROM zadania WHERE id = ?', (id, ))
        conn.commit()
        conn.close()

        return redirect(url_for('zadania'))
    except:  # noqa: E722
        msg = f'DB error while DELETE: {zadanie.zadanie} (id: {zadanie.id})'
        return render_template('flash_info.html', msg=msg, backurl='zadania')


if __name__ == "__main__":
    app.run(debug=True)