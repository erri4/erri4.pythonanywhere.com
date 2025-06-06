from flask import Flask, render_template, redirect, url_for
import requests
from forms import ContactForm
import DBConnectionPool as db


class Message:
    def __init__(self, name, email, content, datetime):
        self.name = name
        self.email = email
        self.content = content
        self.datetime = datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b0d5357ad5888c382a8462562fd80a47b70cd08d7ee18970411c2ba9ed0e9af4'
HOST: str = 'localhost'
USER: str = 'root'
PASSWORD: str = '033850900reefmysql'
DATABASE: str = 'site_contact'
PORT: int = 3300
pool = db.ConnectionPool(PASSWORD, USER, HOST, PORT, DATABASE)

GITHUB_USERNAME = "Erri4"


def fetch_github_repos():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []


def fetch_leaved_messages() -> list[Message]:
    sql = '''select mname, email, message, datentime from messages order by datentime'''
    msgs = []
    with pool.select(sql) as s:
        for i in range(s.sqlres.length):
            msg = s.sqlres.get(row=i)
            name = msg['mname']
            email = msg['email']
            content = msg['message']
            datetime = msg['datentime']
            msgs.append(Message(name, email, content, datetime))
    return msgs


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/projects')
def projects():
    repos = fetch_github_repos()
    return render_template('projects.html', repos=repos)


@app.route('/adminreadcontact')
def adminreadcontact():
    messages = fetch_leaved_messages()
    messages.reverse()
    return render_template('adminreadcontact.html', messages=messages)


@app.route('/mandle')
def mandle():
    return render_template('mandlebrot.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        sql = 'insert into messages (mname, email, message, datentime) values (%s, %s, %s, current_timestamp)'
        placeholders = (name, email, message)
        pool.runsql(sql, placeholders)
        return redirect(url_for('home'))
    return render_template('contact.html', form=form)


@app.route('/<page404>')
def pagenotfound(page404):
    return redirect(url_for('home'))
