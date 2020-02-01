from flask import Flask
from flask import render_template, flash, redirect, url_for, request
from forms import TextBox, MatchForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    drugs = [
        {
            'name': 'drug X',
            'target': 'alpherion',
            'action': 'reduction'
        },
        {
            'name': 'drug Y',
            'target': 'betalux',
            'action': 'increase'
        }
    ]
    return render_template('index.html', title='Home', user=user, drugs=drugs)


@app.route('/match', methods=['GET', 'POST'])
def match():
    form = TextBox()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('match.html', title='Match', form=form)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    data = request.form['cancer']
    # send data to model, then format JSON response
    return data

@app.route('/newmatch', methods=['GET', 'POST'])
def newmatch():
    cancer_suggestion = 'cancer'
    drug_suggestion = 'aspirin'
    form = MatchForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('newmatch.html', title='New Match', form=form)