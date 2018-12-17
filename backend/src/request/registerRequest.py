# coding=utf-8

from marshmallow import Schema, fields, post_load

class RegisterRequest(object):
    def __init__(self, **data):
        self.login = data['login']
        self.password = data['password']
        self.first_name = data['first_name']
        self.last_name = data['last_name']

class RegisterRequestSchema(Schema):
    login = fields.String()
    password = fields.String()
    first_name = fields.String()
    last_name = fields.String()

    @post_load
    def makeRegisterRequest(self, data):
        return RegisterRequest(**data)
