from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"  # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(120), index=True, nullable=False)
    # password is never stored in the DB, an encrypted password is stored
    # the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    comments = db.relationship("Comment", backref="user")


class Comment(db.Model):
    __tablename__ = "comments"  # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)
    create_at = created_at = db.Column(db.DateTime, default=datetime.now())
    # Foreign Keys
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))
    destination_id = db.Column(db.Integer(), db.ForeignKey("destinations.id"))

    # def __repr__(self):
    #     str = "Text {1}"
    #     str.format(self.user, self.text)
    #     return str


class Destination(db.Model):

    __tablename__ = "destinations"  # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, nullable=False, unique=True)
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))
    # relationship
    comments = db.relationship("Comment", backref="dest")

    # def set_comments(self, comment):
    #     self.comments.append(comment)

    # def __repr__(self):
    #     str = "Name {0} , Currency {1}"
    #     str.format(self.name, self.currency)
    #     return str
