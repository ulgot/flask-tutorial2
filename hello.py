from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# @app.route('/')
# def say_hello():
#     return f"<p>Hello {__name__}!!!</p>"

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return '<h1>Hello, World</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id + 100}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/v1/<var>')
def show_user_profile1(var):
    return f'{var}'

@app.route('/v2/<var>')
def show_user_profile2(var):
    return f'{escape(var)}'

