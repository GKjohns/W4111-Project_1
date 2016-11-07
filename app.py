# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, flash,\
                  session, redirect, url_for
from forms import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'comsw4111'
app.debug = True

@app.route('/')
def login():
    return render_template('login.html', form=LoginForm())

@app.route('/attempt_login', methods=['POST'])
def attempt_login():

    form = request.form
    print form

    user_is_valid = form['username'] == 'username'
    pw_is_correct = form['password'] == 'password'

    if user_is_valid and pw_is_correct:
        session['username'] = form['username']
        session['logged_in'] = True

    else:
        # this is gonna change a ton
        if not user_is_valid:
            flash('not a registered username ¯\_(ツ)_/¯')
        elif pw_is_correct:
            flash('password is incorrect')
        return login()
    return select_show_movie()

@app.route('/select_show_movie', methods=['POST'])
def select_show_movie():


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

    return render_template('select_show_movie.html', shows=fake_shows,
                           sid_to_episodes=sid_to_episodes)


if __name__ == '__main__':
    app.run()
