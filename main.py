from flask import Flask, render_template, request
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    # This line uses the render_template() interface to render the submitted_form.html template with submitted form information.
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)