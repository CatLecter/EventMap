from datetime import datetime

from db import db
from event.models import Event
from flask_login import UserMixin
from tag.models import Tag  # noqa
from werkzeug.security import check_password_hash, generate_password_hash

users_tags = db.Table(
    'user_tags',
    db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    address = db.Column(db.String)
    tag = db.relationship('Tag', secondary=users_tags, backref='user', lazy='dynamic')
    path_to_avatar = db.Column(
        db.String,
        default='https://e7.pngegg.com/pngimages/207/508/png-clipart-computer-icons-youtube-avatar-user-avatar-mammal-face.png',
    )
    role = db.Column(db.String(10), index=True, default='user')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_my_events(self, login):
        my_events = Event.query.filter_by(creator_login=login).all()
        return my_events

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f'<Login: {self.login} id={self.id}>'
