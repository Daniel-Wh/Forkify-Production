import os

from flask import Flask, render_template, send_from_directory, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():

    return render_template('index.html')


@app.route('/img/icons.svg', methods=['GET'])
def svg_loader():

    return redirect('/static/img/icons.svg')


if __name__ == '__main__':
    app.run()
