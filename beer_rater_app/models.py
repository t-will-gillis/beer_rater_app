# from app import db, login_manager
from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Beer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), index = True, unique = True)
    style = db.Column(db.String(30), index = True, unique = False)
    abv = db.Column(db.Float(2), index = True, unique = False, default=0.0)
    avg_score = db.Column(db.Float(2), index = True, unique = False, default=0)
    num_reviews = db.Column(db.Integer, index = True, unique = False, default=0)
    beer_notes = db.Column(db.String(255), index = False, unique = False, default='Brewery notes about beer')
    brewery_id = db.Column(db.Integer, db.ForeignKey('brewery.id'))
    
    reviews = db.relationship('Review', backref='beer', lazy='dynamic')

    def __repr__(self):
        return f"{self.name} by {self.brewery_id}"


class Brewery(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    brewery_name = db.Column(db.String(50), index = True, unique = True)
    brewery_city = db.Column(db.String(30), index = True, unique = False)
    brewery_state = db.Column(db.String(16), index = True, unique = False)
    brewery_url = db.Column(db.String(40), index = True, unique = True)

    beers = db.relationship('Beer', backref='brewery', lazy='dynamic')


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    city = db.Column(db.String(32), index = True, unique = False)
    state = db.Column(db.String(2), index = True, unique = False)
    email = db.Column(db.String(40), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    joined_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)

    reviews = db.relationship('Review', backref='user', lazy='dynamic')

    def __repr__(self):
        return f"User: {self.username}"
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        print('inside def check_password')
        return check_password_hash(self.password_hash, password)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.String, index = True, unique = False)
    container = db.Column(db.String, index = True, unique = False)
    size = db.Column(db.String, index = True, unique = False)
    overall = db.Column(db.Float(1), index = True, unique = False, default=0.0)
    look = db.Column(db.Float(1), index = False, unique = False, default=0.0)
    smell = db.Column(db.Float(1), index = False, unique = False, default=0.0)
    taste = db.Column(db.Float(1), index = False, unique = False, default=0.0)
    feel = db.Column(db.Float(1), index = False, unique = False, default=0.0)
    notes = db.Column(db.String(255), index = False, unique = False, default='Tasting notes')
    beer_id = db.Column(db.Integer, db.ForeignKey('beer.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    review_time = db.Column(db.DateTime(), index=True, default=datetime.utcnow)


    def __repr__(self):
        return f"Review: {self.overall}" 


