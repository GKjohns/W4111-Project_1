# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, flash,\
                  session, redirect, url_for, g
from forms import LoginForm, RegistrationForm,\
                  AddShowReviewForm, AddEpisodeReviewForm
import datetime
from model import *
import json
import sqlalchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'comsw4111'
app.config['DATABASE'] = 'postgresql://gkj2106:g5d4w@104.196.175.120:5432/postgres'
app.debug = True


@app.before_request
def before_request():
    engine = get_connection(app.config['DATABASE'])
    g.db = engine.connect()
    print 'connected to database'

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
        print 'disconnected from database'


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
    # process all the data
    if RegistrationForm(form).validate():
        response = register_user(g.db, form['username'], form['password'],
                     form['first_name'], form['last_name'])

        if response:
            flash('Successfully registered!')
            return login()
        else:
            flash('Someone has already chosen that username!')
            return registration_page()
    else:
        flash('There was a problem with your registration')
        return registration_page()


@app.route('/attempt_login', methods=['GET', 'POST'])
def attempt_login():
    form = request.form
    username = form['username']
    password = form['password']

    # if True:
    #     session['username'] = form['username']
    #     session['logged_in'] = True
    #     flash('logged in as {}'.format(username))

    if check_password(g.db, username, password):
        session['username'] = form['username']
        session['logged_in'] = True
        flash('logged in as {}'.format(username))

    else:
        flash('username and/or password is incorrect')
        return login()
    return select_show_episode()

@app.route('/add_show_review', methods=['POST', 'GET'])
def add_show_review():
    form = AddShowReviewForm()
    # the choices are backwards. unbackwards them
    show_choices = [(sid, name) for name, sid in get_all_shows(g.db)]
    form.show.choices = show_choices
    return render_template('add_show_review.html', form=form)

@app.route('/add_episode_review', methods=['POST', 'GET'])
def add_episode_review():
    form = AddEpisodeReviewForm()
    rows = get_all_episodes(g.db)
    episode_choices = [( row[4], '{}: {} s.{} ep. {}'.format(*row[:4]))
                       for row in rows]
    form.episode.choices = episode_choices
    return render_template('add_episode_review.html', form=form)


@app.route('/process_review', methods=['POST', 'GET'])
def process_review():
    form = request.form

    uid = get_uid_from_username(g.db, session['username'])
    review_text = form['review_text']
    rating = form['rating']

    if form.get('show', False):
        show_name = get_name_from_sid(g.db, form['show'])
        sid = form['show']

        add_review_for_show(g.db, uid, sid, rating, review_text)
        flash('Review of {} added!'.format(show_name))

    if form.get('episode', False):
        episode_name = get_name_from_eid(g.db, form['episode'])
        eid = form['episode']
        add_review_for_episode(g.db, uid, eid, rating, review_text)
        flash('Review of {} added!'.format(episode_name))

    return select_show_episode()



@app.route('/select_show_episode', methods=['GET', 'POST'])
def select_show_episode():

    # transform raw rows into lists of dicts
    shows = [{'name': row[0], 'sid': row[1]} for row in get_all_shows(g.db)]
    raw_rows = get_episodes_from_sids(g.db)

    sid_to_episodes = {}
    for row in raw_rows:
        if row[0] not in sid_to_episodes:
            sid_to_episodes[row[0]] = []
        sid_to_episodes[row[0]].append({
            'eid': row[1],
            'name': row[2],
            'season': row[3],
            'episode_number': row[4]
        })

    return render_template('select_show_episode.html', shows=shows,
                           sid_to_episodes=sid_to_episodes)

@app.route('/show_reviews', methods=['GET', 'POST'])
def show_reviews():
    sid = request.args['sid']
    show_name = request.args['show_name']

    # prevent injection
    if not sid.isdigit():
        flash('error retrieving data, please try again')
        select_show_episode()

    contrib_rows = get_contributors_from_sid(g.db, sid)
    contributors = [{'role': row[0], 'name': row[1]} for row in contrib_rows]

    review_rows = get_reviews_for_show(g.db, sid)
    reviews = [{
        'user_name': '{} {}'.format(row[0], row[1]),
        'review_time': row[2].strftime('%B %d, %Y'),
        'text': row[3],
        'rating': row[4],
    } for row in review_rows]
    return render_template('show_reviews.html', reviews=reviews,
                           show_name=show_name, contributors=contributors)

@app.route('/episode_reviews', methods=['GET', 'POST'])
def episode_reviews():

    eid = request.args['eid']
    show_name = request.args['show_name']
    print show_name

    # prevent injection
    if not eid.isdigit():
        flash('error retrieving data, please try again')
        select_show_episode()

    contrib_rows = get_contributors_from_eid(g.db, eid)
    contributors = [{'role': row[0], 'name': row[1]} for row in contrib_rows]

    reviews = get_reviews_for_episode(g.db, eid)
    reviews_formatted = [{
        'show_name': show_name,
        'episode_name': row[0],
        'season': row[1],
        'episode_number': row[2],
        'user_name': '{} {}'.format(row[3], row[4]),
        'review_time': row[5].strftime('%B %d, %Y'),
        'text': row[6],
        'rating': row[7]} for row in reviews]   # an ugly, but useful list comprehension
    return render_template('episode_reviews.html',
                            reviews=reviews_formatted,
                            contributors=contributors)

if __name__ == '__main__':
    app.run()
