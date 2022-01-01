from flask import Flask, render_template, session, request, redirect, url_for
import os

app = Flask(__name__)

key = os.urandom(21)
app.secret_key = key

id_pwd = {'root': '12345678'}


@app.route('/')
def index():
    return 'Hello demon Slayer'


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logincheck', methods=['POST'])
def logincheck():
    user_id = request.form['user_id']
    password = request.form['password']

    if user_id in id_pwd:
        if password == id_pwd[user_id]:
            session['login'] = True
        else:
            session['login'] = False
    else:
        session['login'] = False

    if session['login']:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)