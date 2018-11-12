# coding=utf-8

from marshmallow import Schema, fields, post_load

class UserRequest(object):
    def __init__(self, **data):
        self.login = data['login']
        self.password = data['password']

class UserRequestSchema(Schema):
    login = fields.String()
    password = fields.String()

    @post_load
    def makeUserRequest(self, data):
        return UserRequest(**data)
