from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),   nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    first_name = db.Column(db.String(), unique=False, nullable=True)
    phone = db.Column(db.String(), unique=False, nullable=True)

    def __repr__(self):
        return f'<User: {self.id} - {self.email}>'
        #        <User: 1 - admin@example>

    def serialize(self):
        # Do not serialize the password, its a security breach
        return {'id': self.id,
                'email': self.email,
                'is_active': self.is_active,
                'first_name': self.first_name,
                'phone': self.phone}


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=False, nullable=False)
    description = db.Column(db.String(), unique=False, nullable=False)
    body = db.Column(db.String(), unique=False, nullable=True)
    date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)  # TODO: default !?
    image_url = db.Column(db.String(), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_to = db.relationship('Users', foreign_keys=[user_id], backref=db.backref('posts_to', lazy='select'))

    def __repr__(self):
        return f'<Post: {self.id} - {self.title}>'

    def serialize(self):
        return {'id': self.id,
                'title': self.title,
                'description': self.description,
                'body': self.body,
                'date': self.date,
                'image_url': self.image_url,
                'user_id': self.user_id}

class Medias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media_type = db.Column(db.Enum('image', 'video', 'podcast', name='media_type'), unique=False, nullable=False)
    url = db.Column(db.String(),   nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), unique=True)
    post_to = db.relationship('Posts', foreign_keys=[post_id], backref=db.backref('media_to'), lazy='select')



class Followers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_to = db.relationship('Users', foreign_keys=[follower_id], backref=db.backref('followers_to', lazy='select'))
    following_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    following_to = db.relationship('Users', foreign_keys=[following_id], backref=db.backref('followings_to', lazy='select'))

    def __repr__(self):
        return f'<Follower: {self.follower_id} - Following {self.following_id}>'
        
class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    birth_year = db.Column(db.String(20), nullable=True)
    gender = db.Column(db.String(20), nullable=False)
    height = db.Column(db.Integer, nullable=True)
    mass = db.Column(db.Integer, nullable=True)
    homeworld_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    
    homeworld_to = db.relationship('Planet', foreign_keys=[homeworld_id], backref=db.backref('characters_from', lazy='select'))
    
    def __repr__(self):
        return f'<Character {self.id} - {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_year': self.birth_year,
            'gender': self.gender,
            'height': self.height,
            'mass': self.mass,
            'homeworld_id': self.homeworld_id
        }

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(120), nullable=True)
    terrain = db.Column(db.String(120), nullable=True)
    population = db.Column(db.BigInteger, nullable=True)
    
    def __repr__(self):
        return f'<Planet {self.id} - {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'population': self.population
        }

class Starship(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    model = db.Column(db.String(120), nullable=False)
    manufacturer = db.Column(db.String(120), nullable=True)
    length = db.Column(db.Float, nullable=True)
    crew = db.Column(db.Integer, nullable=True)
    
    def __repr__(self):
        return f'<Starship {self.id} - {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'length': self.length,
            'crew': self.crew
        }