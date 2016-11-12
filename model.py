import sqlalchemy as sql  # I'll import more selectively at some point
import app

def get_connection(database_path):
    ''' downstream will connect to app.config['DATABASE']'''
    return sql.create_engine(database_path)  # connects to the database


def check_password(self, username, password):
    '''
    # Note: we can hash the passwords

    returns True if the username's password matches the password

    returns False if the user is not in the database or the password
            doesn't match

    arguments: what the user entered at the login screen
    '''


    pass


def get_all_shows(db):
    '''
    returns a list of tuples in the following format

    (show.name, show.sid)

    Ex: [('The Walking Dead', 1), ('Family Matters', 2)...('Boy Meets World', 54)]

    no arguments
    '''

    query = '''
        SELECT name, sid
        FROM shows
    '''
    cursor = db.execute(query)

    return cursor.fetchall()


def get_episodes_from_sids(db):
    '''
    returns a list of tuples in the following format

    (show.name, show.sid, episode.name, episode.eid)

    no arguments
    '''
    query = '''
        SELECT sid, eid, name, season, episodeNumber
        FROM episodes
    '''
    cursor = db.execute(query)

    return cursor.fetchall()


def get_reviews_for_show(db, sid):
    '''
    Arguments:
        db: an connected database (engine.connection().connect())
        sid: (int) a show's sid
    Returns:
        list of tuples as rows
        [(user_last_name, user_last_name, review_time, review_text, review_rating)]
    '''

    query = '''
        SELECT
          u.firstname AS user_first_name,
          u.lastname AS user_last_name,
          show_rev.ts AS review_time,
          show_rev.review_text AS review_text,
          show_rev.rating AS review_rating

        FROM
          (SELECT a.name, b.review_text, b.rating, b.ts, b.uid
           FROM shows a JOIN show_reviews b
           ON a.sid = b.sid AND b.sid = {}) show_rev
        JOIN
          users u
        ON
          show_rev.uid = u.uid;
    '''.format(sid)
    cursor = db.execute(query)

    return cursor.fetchall()


def get_reviews_for_episode(db, eid):
    '''
    returns a list of reviews
    Ex: [('episode.name', eid)...('episode.name', eid)]

    arguments: an episode's eid
    '''

    query = '''
        SELECT
          episode_rev.name AS episode_name,
          episode_rev.season AS season,
          episode_rev.episodenumber AS episode_number,
          u.firstname AS user_first_name,
          u.lastname AS user_last_name,
          episode_rev.ts AS review_time,
          episode_rev.review_text AS review_text,
          episode_rev.rating AS review_rating

        FROM
          (SELECT a.name, a.season, a.episodenumber, b.review_text,
                  b.rating, b.ts, b.uid
           FROM episodes a JOIN episode_reviews b
           ON a.eid = b.eid AND b.eid = {}) episode_rev
        JOIN
          users u
        ON
          episode_rev.uid = u.uid;
    '''.format(eid)
    cursor = db.execute(query)

    return cursor.fetchall()


def add_review_for_show(db, uid, sid, rating, review_text):
    '''
    returns True if review was successfully added
    arguments: user's uid, show's sid, rating, the review's text
    '''

    pass


def add_review_for_eipsode(db, uid, eid, rating, review_text):
    '''
    returns True if review was successfully added
    arguments: user's uid, episode's sid, rating, the review's text
    '''

    pass
