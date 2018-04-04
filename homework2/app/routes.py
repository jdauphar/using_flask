from app import app
from flask import render_template

@app.route('/user/<name>')
def index(name=None):
    user = {'username': 'Steve'}
    if name:
        user = {'username': name}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Jack is great'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'John is right'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
