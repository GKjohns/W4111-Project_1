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

    print cursor.fetchall()


def get_episodes_from_sid(db):
    '''
    returns a list of tuples in the following format

    (show.name, show.sid, episode.name, episode.eid)

    no arguments
    '''

    pass


def get_reviews_for_show(self, sid):
    '''
    returns a list of reviews

    arguments: a show's sid
    '''

    pass


def get_episodes_from_sid(self, eid):
    '''
    returns a list of reviews
    Ex: [('episode.name', eid)...('episode.name', eid)]

    arguments: an episode's eid
    '''

    pass


def add_review_for_show(self, uid, sid, rating, review_text):
    '''
    returns True if review was successfully added
    arguments: user's uid, show's sid, rating, the review's text
    '''

    pass


def add_review_for_eipsode(self, uid, eid, rating, review_text):
    '''
    returns True if review was successfully added
    arguments: user's uid, episode's sid, rating, the review's text
    '''

    pass
