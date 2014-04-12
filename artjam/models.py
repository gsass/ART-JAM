from artjam import db


#Utility functions to make db helper tables.

def make_users_helper(name):
    return db.Table(name,
        db.Column('jam_id', db.Integer, db.ForeignKey('users.id')),
        db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
        )

#Utility Tables for Many-to-Many Relationships

'''Helper table representing friendships, used to handle the many-to-many
nature of this relaitonship.  The user with the friendly_id foreign key
befriends the user with the invited_id foreign key.'''
friends = db.Table('Friends',
        db.Column('friend_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('invited_id', db.Integer, db.ForeignKey('user.id'))
        )

'''Many-to-many utility table to determine which users are participating in
which jams.'''
jam_users = make_users_helper('JamUsers')
'''Many-to-many utility table to determine which users are allowed to access
which jams.'''
allowed_users = make_users_helper('AllowedUsers')

#ART JAM models

class User(db.Model):
    '''Model for our table of user account data.'''
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(24))
    acccount_type = db.Column(db.String(200))
    email = db.Column(db.String(60))
    #TODO: USer login creds should go here?
    friended = db.relationship('User', secondary=friends,
            backref=db.backref('friend_of', lazy='dynamic'),
            lazy='dynamic')
    jams_created = db.relationship('Jam', backref='creator_id',
            lazy='dynamic')
    jams_participating = db.relationship('Jam', secondary=jam_users,
            backref=db.backref('participants', lazy='dynamic'),
            lazy='dynamic')
    arts_created = db.relationship('Art', backref='creator_id',
            lazy='dynamic')
    arts_received = db.relationship('Art', backref='recipient_id',
            lazy='dynamic')

    def __init__(self, name, acccount_type, email):
        self.user_name = name
        self.acccount_type = acccount_type
        self.email = email

    def __repr__(self):
        return '<User %(name)s, with ID %(id)d>' % \
                {name: self.user_name, id: self.user_id}

class Jam(db.Model):
    '''Model for our table of JAMs '''
    __tablename__ = 'JAMs'

    #JAM ID attributes
    jam_id = db.Column(db.Integer, primary_key=True)
    jam_name = db.Column(db.String(60))
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    #Security attributes
    is_secured = db.Column(db.Boolean)
    pwd_hash = db.Column(db.String(60))
    #TODO: add a method to hash this password.
    allowed_users = db.relationship('User', secondary=allowed_users,
                        backref=db.backref('jams_allowed', lazy='dynamic'))

    def __init__(self, page_number, text, img_ref):
        self.page_number = page_number
        self.text = text
        self.image_ref = image_ref
        self.story = story

    def __repr__(self):
        return '<%JAM (name)s, with ID %(id)d>' % \
                {name: self.jam_name, id: self.jam_id}

class Art(db.Model):
    '''Model for our ART library.'''
    __tablename__ = 'ARTs'
    art_id = db.Column(db.Integer, primary_key=True)
    art_name = db.Column(db.String(60))
    art_medium = db.Column(db.String(60))
    artist_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    adjective = db.Column(db.String(60))
