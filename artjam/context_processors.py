from flask import session
from artjam import app, db, lm
from artjam.models import User, Jam, Art


def get_user(uid):
    '''Returns a user with the requested user ID, or None.'''
    return User.query.filter_by(user_id=uid).first()


def get_art(uid):
    '''Returns a user with the requested user ID, or None.'''
    return Art.query.filter_by(art_id=uid).first()


def get_jam(uid):
    '''Returns a user with the requested user ID, or None.'''
    return Jam.query.filter_by(jam_id=uid).first()


@app.context_processor
def context_processors():
    return dict(get_user=get_user,
                get art=get_art,
                get_jam=get_jam,
                current=dict(
                    #TODO: Write the before_request functions which populate
                    #the session.
                    user=get_user(session['_current_user']),
                    ART=get_art(session['_current_art']),
                    JAM=get_jam(session['_current_jam'])
                    )
                )
