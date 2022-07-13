from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

tasks = []


@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        tasks.append(request.form.get('item'))
    return redirect(url_for('home'))


@app.route('/delt', methods=['POST'])
def delt():
    if request.method == 'POST':
        item = request.form.get('item')
        tasks.pop(tasks.index(item))
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
