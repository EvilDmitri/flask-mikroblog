from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Dimas' }
    posts = [ #fake array of posts
        {
            'author': { 'nickname': 'John'},
            'body': "It's raining today"
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
        ]
    return render_template("index.html",
                title = 'Home',
                user = user,
                posts = posts)