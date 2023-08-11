from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/maciej')
def maciej():
    return render_template('maciej.html')

if __name__ == "__main__":
    app.run(debug=True)