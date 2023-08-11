import re
import sqlite3
from flask import Flask, render_template, request
from flask import redirect, url_for, abort, make_response


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

        uname = 'admin'  # TODO: user-name brany z sesji

        if priorytet.lower() not in ['wysoki', 'normalny', 'niski']:
            msg = 'priorytet: wysoki, normalny, niski'
            return render_template('flash_info.html', msg=msg, backurl='zadania')

        try:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO zadania (zadanie, priorytet, uname) VALUES (?, ?, ?)', 
                (zadanie, priorytet, uname)
                )
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
        return render_template('zadania7.html', zadania=zadania)

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

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update_zad(id):
    zid = get_zad(id)
    
    if request.method == 'POST':
        zadanie = request.form['zadanie']
        if not zadanie:
            zadanie = zid['zadanie']
        
        priorytet = request.form['priorytet']
        if not priorytet:
            priorytet = zid['priorytet']

        try: 
            conn = get_db_connection()
            conn.execute('UPDATE zadania SET zadanie = ?, priorytet = ? WHERE id = ?', 
                        (zadanie, priorytet, id))
            conn.commit()
            conn.close()

            return redirect(url_for('zadania'))
        except:  # noqa: E722
            msg = f'DB error while UPDATE: {zid.zadanie} (id: {id})'
            return render_template('flash_info.html', msg=msg, backurl='zadania')
    else:
        return render_template('update.html', zadanie=zid)

@app.route('/login', methods=['POST', 'GET'])
def login():
    logged_user = request.cookies.get('uname')
    print(logged_user)
    if request.method == 'POST':
        if logged_user:
            msg = 'Wylogowano'
            resp = make_response(render_template('flash_info.html', 
                                                msg=msg, backurl='login')) 
            resp.set_cookie('uname', '')
            return resp
        else:
            uname = request.form['uname']

            conn = get_db_connection()
            users = conn.execute('SELECT * FROM user').fetchall()
            conn.close()

            for u in users:
                if uname == u['uname']:
                    msg = f'{uname.upper()}, witaj w CodeWithTeam!'
                    resp = make_response(render_template('flash_info.html', 
                                                        msg=msg, backurl='login')) 
                    resp.set_cookie('uname', uname)
                    return resp
            return render_template('flash_info.html', msg='User not found', backurl='login')
    else:
        return render_template('login.html', logged_user=logged_user)

if __name__ == "__main__":
    app.run(debug=True)