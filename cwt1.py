from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def start():
    msg = f'''
<head>
<link rel="stylesheet" href="{ url_for('static', filename='css/main.css') }">
</head>
<table>
<tr>
<td><a href={url_for('about')}>about</a></td>
<td><a href={url_for('maciej')}>maciej</a></td>
</tr>
</table>
<h1>Witaj na stronie projektu Code With Team</h1>
<p>Zapraszamy!</p>
'''
    return msg

@app.route('/about')
def about():
    msg = f'''
<table>
<tr>
<td><a href={url_for('start')}>start</a></td>
<td><a href={url_for('maciej')}>maciej</a></td>
</tr>
</table>
<p>Jaki jest cel projektu?</p>
<p>Edukowanie studentów w zakresie współpracy w zespole, umiejętności miękkich, 
korzystania z narzędzi do pracy w zespole np. git oraz tworzenia oprogramowania.</p>
<br />
<p>Dla kogo jest skierowany?</p>
<p>Projekt jest skierowany do studentów którzy programują lub znają podstawy w zakresie
programowania.</p>
<br />
<p>Jaki będzie efekt końcowy?</p>
<p>Powstanie strony internetowej, gdzie studenci łączą się w 3-4 osobowe zespoły, a 
następnie przystępują do kursu który będzie kończył się otrzymaniem certyfikatu za 
ukończenie kursu.</p>
'''
    return msg

@app.route('/maciej')
def maciej():
    msg = f'''
    <table>
<tr>
<td><a href={url_for('start')}>start</a></td>
<td><a href={url_for('about')}>about</a></td>
</tr>
</table>
    <p><b>Maciej Zelder</b><br />Student 2 roku IS UŚ</p>'''
    return msg

if __name__ == "__main__":
    app.run(debug=True)