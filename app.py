# app.py

from flask import Flask, render_template, redirect, url_for, jsonify, request
from talk_mashup_bot import talk_mashup_bot

app = Flask(__name__)

@app.route('/')
def hello():
    return "Michael Jackson's Off the Wall album, then Thriller are excellent!!"

@app.route('/talk/new')
def new_talk():
    talk_title = talk_mashup_bot.generateTitle()
    return talk_title
    
if __name__ == '__main__':
    app.run(debug=True)