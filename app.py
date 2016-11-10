# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, flash,\
                  session, redirect, url_for
from forms import LoginForm, RegistrationForm, AddShowReviewForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'comsw4111'
app.debug = True

@app.route('/')
def login():
    return render_template('login.html', form=LoginForm())


@app.route('/registration_page', methods=['GET', 'POST'])
def registration_page():
    form = RegistrationForm()
    return render_template('registration.html', form=form)


@app.route('/attempt_register', methods=['POST'])
def attempt_register():
    form = request.form
    form_is_good = True
    # process all the data
    if form_is_good:
        flash('Successfully registered!')
        return login()
    else:
        flash('There was a problem with your registration')
        return registration_page()


@app.route('/attempt_login', methods=['POST'])
def attempt_login():
    form = request.form

    user_is_valid = form['username'] == 'username'
    pw_is_correct = form['password'] == 'password'

    if user_is_valid and pw_is_correct:
        session['username'] = form['username']
        session['logged_in'] = True

    else:
        # this is gonna change a ton
        if not user_is_valid:
            flash('not a registered username')
        elif not pw_is_correct:
            flash('password is incorrect')
        return login()
    return select_show_episode()

@app.route('/add_show_review', methods=['POST', 'GET'])
def add_show_review():
    form = AddShowReviewForm()
    return render_template('add_show_review.html', form=form)

@app.route('/process_review', methods=['POST', 'GET'])
def process_review():
    form = request.form

    # Use the model to pull data from the database


    flash('Review of {} added!'.format(form['show']))

    return select_show_episode()



@app.route('/select_show_episode', methods=['POST'])
def select_show_episode():


    ######

    # All this stuff will change

    ######



    fake_shows = [{'name':'Family Matters',
                       'sid': 0},
                  {'name': 'Boy Meets world',
                   'sid': 1},
                  {'name': 'Power Rangers',
                   'sid': 2}]


    sid_to_episodes = {
        0: [{'name': 'Something Happy',
             'sid': 11},
            {'name': 'A Show',
             'sid': 3}],
        1: [{'name': 'Person Dies',
            'sid': 54},
            {'name': 'Love Blooms',
             'sid': 20}],
        2: [{'name': 'Accident Happens',
             'sid': 3}]
    }

    return render_template('select_show_episode.html', shows=fake_shows,
                           sid_to_episodes=sid_to_episodes)


if __name__ == '__main__':
    app.run()
