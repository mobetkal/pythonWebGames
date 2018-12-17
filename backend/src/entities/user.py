# coding=utf-8

from sqlalchemy import Column, String
from marshmallow import Schema, fields

from .entity import Entity, Base


class User(Entity, Base):
    __tablename__ = 'users'

    login = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    display_name = Column(String)

    def __init__(self, login, password, first_name, last_name):
        Entity.__init__(self)
        self.login = login
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.display_name = first_name + " " + last_name

class UserSchema(Schema):
    id = fields.Number()
    login = fields.Str()
    password = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    display_name = fields.Str()
    created_at = fields.DateTime()
