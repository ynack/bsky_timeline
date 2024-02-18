from flask import render_template, request
from bskytimeline import app
from atproto import Client

client = Client()
client.login('ユーザ名', 'パスワード')

@app.route('/')
def index():
    res = client.get_timeline()

    return render_template('bskytimeline/bsky_timeline.html', timeline = res)
