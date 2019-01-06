# coding=utf-8

from marshmallow import Schema, fields, post_load
import uuid

class LoginResponse(object):
    def __init__(self, **data):
        self.auth_token = uuid.uuid4()
        self.display_name = data['display_name']
        self.login = data['login']

class LoginResponseSchema(Schema):
    auth_token = fields.String()
    display_name = fields.String()
    login = fields.String()

    @post_load
    def makeLoginResponse(self, data):
        return LoginResponse(**data)
